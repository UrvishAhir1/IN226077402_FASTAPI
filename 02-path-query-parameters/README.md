# FastAPI Task 2

This task continues building REST API endpoints using **FastAPI**.  
It focuses on query parameters, path parameters, Pydantic validation, POST requests, and business logic.

All tasks are implemented in a single `main.py` file.

---

## 1. Filter Products by Minimum Price

### Scenario
The app wants a **Premium Products** section that shows only items above a certain price.  
A `min_price` filter should be added so users can filter products starting from a minimum price.

### Your Tasks
- Update the existing endpoint: `GET /products/filter`
- Add a new query parameter: `min_price: int`
- When `min_price` is provided, return only products whose price is **greater than or equal to** that value
- Ensure the new filter works together with the existing filters such as `max_price` and `category`

---

## 2. Get Only the Price of a Product

### Scenario
The cart page only needs to know a product's **name and price**, not the full product details.  
A lightweight endpoint should return only these two fields for a given product.

### Your Tasks
- Create a new endpoint: `GET /products/{product_id}/price`
- Return only:
  - `name`
  - `price`
- Do **not** return the full product dictionary
- If the product ID does not exist, return:  
  `{"error": "Product not found"}`

---

## 3. Accept Customer Feedback

### Scenario
After receiving their order, customers want to leave a **rating and optional comment** for the product they purchased.  
The API must validate the feedback before accepting it.

### Your Tasks
- Create a **Pydantic model** `CustomerFeedback` with:
  - `customer_name` (string, minimum 2 characters)
  - `product_id` (integer greater than 0)
  - `rating` (integer between 1 and 5)
  - `comment` (optional string, maximum 300 characters)

- Create endpoint: `POST /feedback`
- Accept feedback using the Pydantic model
- Save the feedback to a list called `feedback = []`
- Return a confirmation message with the saved feedback and total feedback count

---

## 4. Build a Product Summary Dashboard

### Scenario
The business owner wants a **dashboard endpoint** that quickly provides store statistics including product counts, stock information, pricing extremes, and available categories.

### Your Tasks
- Create endpoint: `GET /products/summary`
- Return:
  - `total_products`
  - `in_stock_count`
  - `out_of_stock_count`
- Return:
  - `most_expensive` product (name and price only)
  - `cheapest` product (name and price only)
- Return a list of **unique category names** available in the store

---

## 5. Validate & Place a Bulk Order

### Scenario
A corporate client wants to place **bulk orders** for office supplies.  
They send their company name, contact email, and a list of items containing product IDs and quantities.  
The API must validate the order, check product availability, and calculate the total bill.

### Your Tasks
- Create a **Pydantic model** `OrderItem` with:
  - `product_id` (integer greater than 0)
  - `quantity` (integer between 1 and 50)

- Create another **Pydantic model** `BulkOrder` with:
  - `company_name` (string, minimum 2 characters)
  - `contact_email` (string, minimum 5 characters)
  - `items` (list of `OrderItem`, at least one item)

- Create endpoint: `POST /orders/bulk`
- Loop through each order item
- Check whether the product exists and is in stock
- Calculate subtotal and total price
- If a product fails validation or is out of stock, include it in a **failed list**
- Return a summary containing confirmed items, failed items, and the grand total

---

## 6. Order Status Tracker

### Scenario
Orders should not be confirmed immediately.  
Instead, they should start with a **pending** status and only move to **confirmed** after approval by the warehouse.

### Your Tasks
- Modify the existing `POST /orders` endpoint so that new orders start with:  
  `status = "pending"`

- Create endpoint: `GET /orders/{order_id}`
  - Return a single order by its ID
  - If the order does not exist, return:  
    `{"error": "Order not found"}`

- Create endpoint: `PATCH /orders/{order_id}/confirm`
  - Change the order status from `"pending"` to `"confirmed"`

- If the order ID does not exist in the PATCH endpoint, return:  
  `{"error": "Order not found"}`