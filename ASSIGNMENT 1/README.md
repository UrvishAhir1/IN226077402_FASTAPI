# FastAPI Assignment 1

This assignment focuses on building REST API endpoints using **FastAPI**.  
All tasks are implemented in a single `main.py` file.

---

## 1. Add 3 More Products

### Scenario
Your client just added 3 new items to their store - **Laptop Stand**, **Mechanical Keyboard**, and **Webcam**.  
The mobile app needs to show them.

### Your Tasks
- Create endpoint: `GET /products`
- Add **3 new products** to the `products` list in `main.py` with IDs **5, 6, 7**
- Each product must have:
  - `id`
  - `name`
  - `price`
  - `category`
  - `in_stock`

---

## 2. Add a Category Filter Endpoint

### Scenario
The mobile app wants to show only **Electronics** on one page and only **Stationery** on another.  
A new endpoint is required to filter products based on their category.

### Your Tasks
- Create a new endpoint: `GET /products/category/{category_name}`
- It should return only products where the `category` matches the given name
- If no products are found for that category, return: `{"error": "No products found in this category"}`

---

## 3. Show Only In-Stock Products

### Scenario
Customers are complaining they can see products that are out of stock and then get disappointed.  
The app team wants a separate endpoint that returns **only available products**.

### Your Tasks
- Create endpoint: `GET /products/instock`
- Return only products where `in_stock = True`
- Also return a **count** of how many in-stock products there are

---

## 4. Build a Store Info Endpoint

### Scenario
The mobile app's home screen needs to show a **summary of the store** total products, how many are in stock, and all available categories.

### Your Tasks
- Create endpoint: `GET /store/summary`
- Return:
  - Total products count
  - In-stock products count
  - Out-of-stock products count
  - A list of unique categories available in the store

---

## 5. Search Products by Name

### Scenario
Users want to search for products. When they type a keyword in the search bar, the app should show all products whose **name contains that word**.

### Your Tasks
- Create endpoint: `GET /products/search/{keyword}`

- Search should be **case-insensitive**
- Return matched products
- If no products match the search, return: `{"message": "No products matched your search"}`
- Return total number of matches

---

## 6. Cheapest & Most Expensive Product

### Scenario
The app wants to show a **"Best Deal"** section (cheapest product) and a **"Premium Pick"** section (most expensive product) on the home screen.

### Your Tasks
- Create endpoint: `GET /products/deals`
- Return:
  - the product with the lowest price as "best_deal"
  - the product with the highest price as "premium_pick"