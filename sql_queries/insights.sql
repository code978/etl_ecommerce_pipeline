-- Get Top 10 Best-Selling Products
SELECT product_id, SUM(total_revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;

-- Get Top 10 High-Value Customers
SELECT customer_id, SUM(total_revenue) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
