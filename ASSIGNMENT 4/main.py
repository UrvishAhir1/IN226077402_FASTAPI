from fastapi import FastAPI, Query, Response, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# Products list (temp database)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},  # out of stock
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]

# Cart storage
orders = []
order_counter = 1
cart = []


# --- Helper Function ---
def find_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return None

def calculate_total(product: dict, quantity: int):
    return product["price"] * quantity


# --- Pydantic Model ---
class CheckoutRequest(BaseModel):
    customer_name: str = Field(..., min_length=2)
    delivery_address: str = Field(..., min_length=10)


# Home --- Endpoint 0 ---
@app.get("/")
def home():
    return {"message": "FastAPI Is Working"}


# Q1,Q3,Q4 --- Add to cart/Out-of-stock error/Update quantity ---
@app.post("/cart/add")
def add_to_cart(
    product_id: int = Query(..., description="Product ID"),
    quantity: int = Query(1, description="Quantity")
):

    # find the product from the product list
    product = find_product(product_id)

    # if product id doesn't exist -> return 404 error
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # check if the product is available in stock
    if not product["in_stock"]:
        raise HTTPException(status_code=400, detail=f"{product['name']} is out of stock")

    # quantity must be at least 1
    if quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be at least 1")

    # If product already exists in cart -> update quantity
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            # recalculate subtotal after quantity change
            item["subtotal"] = calculate_total(product, item["quantity"])

            return {
                "message": "Cart updated",
                "cart_item": item
            }

    # New cart item
    # if product not already in cart -> create a new cart entry
    cart_item = {
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "subtotal": calculate_total(product, quantity)
    }

    # add new item to cart
    cart.append(cart_item)

    return {
        "message": "Added to cart",
        "cart_item": cart_item
    }


# Q2 --- View cart ---
@app.get("/cart")
def view_cart():

    # if cart is empty return a friendly message
    if not cart:
        return {"message": "Cart is empty", "items": [], "grand_total": 0}

    # calculate total value of the cart
    grand_total = sum(item["subtotal"] for item in cart)

    return {
        "items": cart,
        "item_count": len(cart),
        "grand_total": grand_total
    }


# Q5 --- Checkout ---
@app.post("/cart/checkout")
def checkout(checkout_data: CheckoutRequest, response: Response):

    global order_counter

    # checkout should not happen if cart is empty
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty — add items first")

    placed_orders = []
    grand_total = 0

    # create one order for each item in the cart
    for item in cart:

        order = {
            "order_id": order_counter,
            "customer_name": checkout_data.customer_name,
            "product": item["product_name"],
            "quantity": item["quantity"],
            "delivery_address": checkout_data.delivery_address,
            "total_price": item["subtotal"],
            "status": "confirmed"
        }

        orders.append(order)
        placed_orders.append(order)

        grand_total += item["subtotal"]
        order_counter += 1

    # clear the cart after successful checkout
    cart.clear()

    response.status_code = status.HTTP_201_CREATED

    return {
        "message": "Checkout successful",
        "orders_placed": placed_orders,
        "grand_total": grand_total
    }



# Q5 --- Remove item from cart ---
@app.delete("/cart/{product_id}")
def remove_from_cart(product_id: int, response: Response):

    # find the product inside the cart
    for item in cart:
        if item["product_id"] == product_id:
            cart.remove(item)
            return {"message": f"{item['product_name']} removed from cart"}

    # if product not found in cart
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Product not in cart"}


# --- View all orders ---
@app.get("/orders")
def get_orders():
    return {
        "orders": orders,
        "total_orders": len(orders)
    }