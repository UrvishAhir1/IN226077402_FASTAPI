# FastAPI Assignment 4

This assignment focuses on building a **shopping cart system** using FastAPI.  
The API simulates a simple e-commerce workflow where users can add items to a cart, review them, remove items, and complete checkout.

All tasks are implemented in a single `main.py` file.

---

## 1. Add Items to the Cart

### Scenario
A customer visits the store and wants to purchase multiple products. They add a **Wireless Mouse** and a **Notebook** to their cart using the cart API.

### Your Tasks
- Use the endpoint `POST /cart/add`
- Add **Wireless Mouse** with quantity 2
- Add **Notebook** with quantity 1
- Ensure each request returns a confirmation message
- Confirm the subtotal for each item is calculated correctly

---

## 2. View the Cart and Verify the Total

### Scenario
Before placing the order, the customer wants to review the contents of the cart and confirm the total price.

### Your Tasks
- Use the endpoint `GET /cart`
- Confirm that both items appear in the cart
- Verify that the cart returns:
  - list of items
  - item count
  - grand total of the cart
- Ensure the total matches the sum of all item subtotals

---

## 3. Try Adding an Out-of-Stock Product

### Scenario
The customer attempts to add a product that is currently **out of stock**. The system must reject this request and return a proper error.

### Your Tasks
- Attempt to add **USB Hub** to the cart using `POST /cart/add`
- Confirm the API returns an **out-of-stock error**
- Attempt to add a product with an **invalid product ID**
- Confirm the API returns a **product not found error**
- Verify the cart contents remain unchanged

---

## 4. Add More Quantity of an Existing Cart Item

### Scenario
The customer decides to purchase one more **Wireless Mouse**. Instead of creating a duplicate entry, the cart should update the existing item's quantity.

### Your Tasks
- Use `POST /cart/add` to add the same product again
- Confirm the API updates the quantity instead of creating a new entry
- Verify the new quantity and subtotal are updated correctly
- Confirm the number of unique cart items remains unchanged
- Verify the updated grand total

---

## 5. Remove an Item Then Checkout

### Scenario
The customer changes their mind about one item and removes it from the cart before proceeding to checkout.

### Your Tasks
- Use `DELETE /cart/{product_id}` to remove the product from the cart
- Confirm the item is removed successfully
- Verify the updated cart total
- Use `POST /cart/checkout` to place the order
- Confirm the cart is cleared after checkout
- Use `GET /orders` to verify the order was recorded

---

## 6. Full Cart System Flow

### Scenario
Two customers use the system sequentially. Each customer adds items, modifies their cart if needed, and completes checkout. The system should correctly track all orders.

### Your Tasks
- Restart the server to simulate a new session
- Customer 1:
  - Add items to the cart
  - Verify cart total
  - Complete checkout
- Customer 2:
  - Add different items
  - Remove an item from the cart
  - Complete checkout
- Use `GET /orders` to confirm all orders are recorded correctly

---

## 7. Checkout with an Empty Cart

### Scenario
A user attempts to checkout without adding any items to the cart. The API should handle this case gracefully.

### Your Tasks
- Confirm the cart is empty using `GET /cart`
- Attempt to checkout using `POST /cart/checkout`
- Ensure the API returns a proper error response
- Confirm no new orders are created