from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field

app = FastAPI()

# Products list (temp database)
products = [
    {"id": 1, "name": "Smartphone", "price": 19999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Bluetooth Speaker", "price": 2999, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Running Shoes", "price": 3999, "category": "Fashion", "in_stock": True},
    {"id": 4, "name": "Backpack", "price": 1499, "category": "Accessories", "in_stock": True},
]


# --- Helper Function ---
def find_product(product_id: int):
    """Find product by ID."""
    for p in products:
        if p["id"] == product_id:
            return p
    return None


# --- Pydantic Model ---
class NewProduct(BaseModel):  # Day 4 style
    name: str = Field(..., min_length=2, max_length=100)
    price: int = Field(..., gt=0)
    category: str = Field(..., min_length=2)
    in_stock: bool = True


# Home --- Endpoint 0 ---
@app.get("/")
def home():
    return {"message": "FastAPI Is Working"}


# Q1 --- Add Product ---
@app.post("/products")
def add_product(new_product: NewProduct):

    # check duplicate name
    existing_names = [p["name"].lower() for p in products]

    if new_product.name.lower() in existing_names:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this name already exists",
        )

    # generate next id
    next_id = max(p["id"] for p in products) + 1

    product = {
        "id": next_id,
        "name": new_product.name,
        "price": new_product.price,
        "category": new_product.category,
        "in_stock": new_product.in_stock,
    }

    products.append(product)

    return {"message": "Product added", "product": product}


# Q5 --- Products Audit ---
@app.get("/products/audit")
def product_audit():

    in_stock_list = [p for p in products if p["in_stock"]]
    out_stock_list = [p for p in products if not p["in_stock"]]

    stock_value = sum(p["price"] * 10 for p in in_stock_list)

    priciest = max(products, key=lambda p: p["price"])

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock_list),
        "out_of_stock_names": [p["name"] for p in out_stock_list],
        "total_stock_value": stock_value,
        "most_expensive": {
            "name": priciest["name"],
            "price": priciest["price"]
        }
    }


# Q6 --- Category Discount ---
@app.put("/products/discount")
def bulk_discount(
    category: str = Query(..., description="Category to discount"),
    discount_percent: int = Query(..., ge=1, le=99, description="Discount percentage"),
):

    updated = []

    for p in products:
        if p["category"].lower() == category.lower():

            p["price"] = int(p["price"] * (1 - discount_percent / 100))

            updated.append({
                "name": p["name"],
                "new_price": p["price"]
            })

    if not updated:
        return {"message": f"No products found in category: {category}"}

    return {
        "message": f"{discount_percent}% discount applied to {category}",
        "updated_count": len(updated),
        "updated_products": updated
    }


# Q2 --- Update Product ---
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    price: int = Query(None, description="Update product price"),
    in_stock: bool = Query(None, description="Update stock status"),
):

    product = find_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if price is not None:
        product["price"] = price

    if in_stock is not None:
        product["in_stock"] = in_stock

    return {"message": "Product updated", "product": product}


# Q3 --- Delete Product ---
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    product = find_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    products.remove(product)

    return {"message": f"Product '{product['name']}' deleted"}
