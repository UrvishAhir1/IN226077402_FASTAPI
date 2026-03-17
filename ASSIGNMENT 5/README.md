# FastAPI Assignment 5

This assignment focuses on implementing **Search, Sort, and Pagination** features in a FastAPI application.  
These are core functionalities used in real-world APIs.

All tasks are implemented in a single `main.py` file.

---

## 1. Test the Search Endpoint

### Scenario
A customer uses the search bar in the application to find products using different keywords. The system should return matching products regardless of case.

### Your Tasks
- Use the endpoint `GET /products/search`
- Search using different keywords
- Verify that search is case-insensitive
- Confirm matching products are returned correctly
- Ensure a proper message is shown when no products are found

---

## 2. Test All Sort Combinations

### Scenario
The application provides sorting options such as price and name. Users can sort products in ascending or descending order.

### Your Tasks
- Use the endpoint `GET /products/sort`
- Test sorting by price and name
- Test both ascending and descending order
- Verify correct ordering of products
- Ensure invalid sort parameters return an error message
- Check default behavior when no parameters are provided

---

## 3. Navigate Pages Like a Real User

### Scenario
Products are displayed in pages to improve user experience. Users navigate between pages to browse items.

### Your Tasks
- Use the endpoint `GET /products/page`
- Test different page and limit values
- Verify correct products appear on each page
- Confirm total pages are calculated correctly
- Check behavior when page exceeds available data
- Verify default pagination values

---

## 4. Search the Orders List

### Scenario
The store manager wants to find all orders placed by a specific customer using their name.

### Your Tasks
- Create multiple orders using `POST /orders`
- Implement `GET /orders/search`
- Search orders using customer name
- Ensure search is case-insensitive
- Return matching orders with count
- Return a friendly message if no orders are found

---

## 5. Sort Products by Category Then Price

### Scenario
The admin wants to view products grouped by category, and within each category, sorted by price.

### Your Tasks
- Create endpoint `GET /products/sort-by-category`
- Sort products first by category alphabetically
- Then sort by price within each category
- Return the sorted list of products

---

## 6. Search + Sort + Pagination in One Endpoint

### Scenario
A real-world API combines searching, sorting, and pagination into a single endpoint for efficiency.

### Your Tasks
- Create endpoint `GET /products/browse`
- Accept optional parameters:
  - keyword
  - sort_by
  - order
  - page
  - limit
- Apply operations in order:
  1. Search (if keyword provided)
  2. Sort results
  3. Paginate results
- Return filtered, sorted, and paginated data
- Include metadata such as total results and total pages

---

## 7. Paginate the Orders List

### Scenario
As the number of orders grows, the admin needs pagination to browse them efficiently.

### Your Tasks
- Create endpoint `GET /orders/page`
- Add pagination using page and limit parameters
- Return paginated list of orders
- Include total orders and total pages
- Ensure correct slicing of data per page