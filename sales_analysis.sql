-- ============================================================
-- RETAIL SALES ANALYTICS
-- SQL ANALYSIS
-- ============================================================

-- 1. View complete dataset
SELECT *
FROM sales;


-- ============================================================
-- 2. KEY BUSINESS KPIs
-- ============================================================

-- Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- Total Quantity Sold
SELECT SUM(quantity) AS total_quantity
FROM sales;

-- Total Revenue
SELECT SUM(revenue) AS total_revenue
FROM sales;

-- Average Order Value
SELECT
    ROUND(SUM(revenue) / COUNT(DISTINCT order_id), 2)
    AS average_order_value
FROM sales;


-- ============================================================
-- 3. CATEGORY-WISE REVENUE
-- ============================================================

SELECT
    category,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;


-- ============================================================
-- 4. REGION-WISE REVENUE
-- ============================================================

SELECT
    region,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;


-- ============================================================
-- 5. PRODUCT-WISE REVENUE
-- ============================================================

SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;


-- ============================================================
-- 6. TOP 5 PRODUCTS
-- ============================================================

SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 5;


-- ============================================================
-- 7. PAYMENT METHOD ANALYSIS
-- ============================================================

SELECT
    payment_method,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY payment_method
ORDER BY total_revenue DESC;


-- ============================================================
-- 8. MONTHLY REVENUE TREND
-- ============================================================

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;


-- ============================================================
-- 9. CUSTOMER-WISE REVENUE
-- ============================================================

SELECT
    customer_name,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY customer_name
ORDER BY total_revenue DESC;


-- ============================================================
-- 10. TOP 5 CUSTOMERS
-- ============================================================

SELECT
    customer_name,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY customer_name
ORDER BY total_revenue DESC
LIMIT 5;


-- ============================================================
-- 11. PRODUCT PERFORMANCE
-- ============================================================

SELECT
    product,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;


-- ============================================================
-- 12. CATEGORY + REGION ANALYSIS
-- ============================================================

SELECT
    category,
    region,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY category, region
ORDER BY total_revenue DESC;


-- ============================================================
-- 13. PAYMENT METHOD + CATEGORY
-- ============================================================

SELECT
    payment_method,
    category,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY payment_method, category
ORDER BY total_revenue DESC;


-- ============================================================
-- 14. DAILY REVENUE
-- ============================================================

SELECT
    order_date,
    SUM(revenue) AS daily_revenue
FROM sales
GROUP BY order_date
ORDER BY order_date;


-- ============================================================
-- 15. HIGHEST REVENUE PRODUCT
-- ============================================================

SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 1;


-- ============================================================
-- 16. LOWEST REVENUE PRODUCT
-- ============================================================

SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue ASC
LIMIT 1;


-- ============================================================
-- 17. REGION PERFORMANCE
-- ============================================================

SELECT
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;


-- ============================================================
-- 18. HIGH-VALUE ORDERS
-- ============================================================

SELECT
    order_id,
    customer_name,
    product,
    revenue
FROM sales
WHERE revenue > 20000
ORDER BY revenue DESC;


-- ============================================================
-- END OF SQL ANALYSIS
-- ============================================================