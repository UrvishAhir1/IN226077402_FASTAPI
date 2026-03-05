from fastapi import FastAPI

app = FastAPI()

# Products list (temp database)
products = [
    {"id": 1, "name": "Smartphone", "price": 19999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Bluetooth Speaker", "price": 2999, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Running Shoes", "price": 3999, "category": "Fashion", "in_stock": True},
    {"id": 4, "name": "Backpack", "price": 1499, "category": "Accessories", "in_stock": True},

    # Q1 Added products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Home --- Endpoint 0 ---
@app.get("/")
def home():
    return {"message": "FastAPI Is Working"}

# Q1 --- Endpoint 1 ---
@app.get("/products")
def get_products():

    return {
        "products": products,
        "total": len(products)
    }

# Q2 --- Endpoint 2 ---
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    # filter products by category
    products_by_category = [p for p in products if p["category"].lower() == category_name.lower()]

    # If no products found
    if not products_by_category:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": products_by_category,
        "total": len(products_by_category)
    }

# Q3 --- Endpoint 3 ---
@app.get("/products/instock")
def get_instock_products():

    # filter products where in_stock is True
    instock_products = [p for p in products if p["in_stock"]]

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }

# Q4 --- Endpoint 4 ---
@app.get("/store/summary")
def store_summary():

    # count instock
    in_stock = len([p for p in products if p["in_stock"]])

    # count out of stock
    out_of_stock = len([p for p in products if not p["in_stock"]])

    # list all categories (remove duplicates using set)
    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

# Q5 --- Endpoint 5 ---
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    # case insensitive search
    matched_products = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    # if nothing matched
    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "matched_products": matched_products,
        "total_matches": len(matched_products)
    }

# Q6 --- Endpoint 6 ---
@app.get("/products/deals")
def product_deals():

    # find cheapest product
    best_deal = min(products, key=lambda p: p["price"])

    # find most expensive product
    premium_pick = max(products, key=lambda p: p["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }