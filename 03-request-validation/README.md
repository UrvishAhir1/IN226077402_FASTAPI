# FastAPI Task 3

This task focuses on implementing **CRUD operations** using FastAPI.  
The tasks involve adding, updating, deleting, and summarizing product data using API endpoints.

All tasks are implemented in a single `main.py` file.

---

## 1. Add New Products Using POST

### Scenario
The store is expanding its catalogue. Two new products need to be added — **Laptop Stand** and **Sticky Notes**. These products should be added using the `POST /products` endpoint instead of manually modifying the products list.

### Your Tasks
- Use the endpoint `POST /products` to add a new product:
  - Name: Laptop Stand  
  - Price: 1299  
  - Category: Electronics  
  - In Stock: true  

- Use the same endpoint again to add another product:
  - Name: Sticky Notes  
  - Price: 49  
  - Category: Stationery  
  - In Stock: true  

- After each addition, call `GET /products` to confirm the product count increases and IDs are auto-generated.

- Attempt to add a duplicate product name (for example: Wireless Mouse) and confirm the API returns a **400 Bad Request** error.

---

## 2. Restock a Product Using PUT

### Scenario
The warehouse has received new inventory for a product that was previously unavailable. The product needs to be restocked and its price adjusted using the update endpoint.

### Your Tasks
- Use the endpoint `PUT /products/{product_id}` to update the stock status.
- Set `in_stock` to **true** for the selected product.
- Update the product price using the `price` query parameter.
- Perform an update where both the stock status and price are changed in a single request.
- Attempt to update a product ID that does not exist and confirm the API returns **404 Not Found**.

---

## 3. Delete a Product

### Scenario
A product has been permanently discontinued and must be removed from the store catalogue.

### Your Tasks
- Use the endpoint `DELETE /products/{product_id}` to remove the product from the list.
- Confirm the response message includes the product name that was deleted.
- Call `GET /products` afterward to verify the product was removed.
- Attempt to delete the same product again and confirm the API returns **404 Not Found**.
- Attempt to delete a product ID that never existed and confirm the API returns **404 Not Found**.

---

## 4. Complete a Full CRUD Workflow

### Scenario
A new product launch goes through the full lifecycle — it is created, updated after a pricing correction, and later removed when the launch is cancelled.

### Your Tasks
- Use `POST /products` to create a new product called **Smart Watch**.
- Call `GET /products` to identify the auto-generated product ID.
- Use `PUT /products/{product_id}` to correct the product price.
- Call `GET /products/{product_id}` to confirm the updated price.
- Use `DELETE /products/{product_id}` to remove the product.
- Finally, call `GET /products` again to verify the product has been removed from the list.

---

## 5. Build a Product Audit Endpoint

### Scenario
The store manager needs a daily summary of the product inventory including stock counts, product availability, and overall inventory value.

### Your Tasks
- Create a new endpoint: `GET /products/audit`
- Return the following information:
  - Total number of products
  - Number of products currently in stock
  - List of product names that are out of stock
  - Total stock value calculated as `price × 10` for in-stock products
  - The most expensive product (name and price)
- Ensure the `/products/audit` route is placed **above `/products/{product_id}`** in the file.

---

## 6. Apply Category Discount

### Scenario
A store-wide promotion is running and all products in a specific category need to receive a percentage-based discount.

### Your Tasks
- Create a new endpoint: `PUT /products/discount`
- Accept query parameters:
  - `category`
  - `discount_percent`
- Apply the discount to every product in the specified category.
- Update the price using the formula:
  `new_price = price × (1 - discount_percent / 100)`
- Return:
  - Number of products updated
  - The updated product prices
- If no products exist in the specified category, return a friendly message indicating that no products were found.