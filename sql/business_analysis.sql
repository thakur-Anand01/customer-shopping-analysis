
-- =====================================================
-- CUSTOMER SHOPPING BEHAVIOR ANALYSIS
-- SQL BUSINESS ANALYSIS
-- =====================================================

USE customer_shopping_analysis;


-- Q1. DATA VALIDATION

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT `Customer ID`) AS unique_customers
FROM customer_shopping;


-- Q2. CATEGORY PERFORMANCE

SELECT
    Category,
    COUNT(*) AS purchase_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY Category
ORDER BY total_purchase_amount DESC;


-- Q3. SPENDING BY GENDER

SELECT
    Gender,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY Gender
ORDER BY total_purchase_amount DESC;


-- Q4. SUBSCRIPTION ANALYSIS

SELECT
    `Subscription Status`,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY `Subscription Status`; 


-- Q5. DISCOUNT ANALYSIS

SELECT
    `Discount Applied`,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY `Discount Applied`;


-- Q6. PAYMENT METHOD PREFERENCES

SELECT
    `Payment Method`,
    COUNT(*) AS record_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_shopping),
        2
    ) AS percentage
FROM customer_shopping
GROUP BY `Payment Method`
ORDER BY record_count DESC;


-- Q7. SEASONAL SPENDING

SELECT
    Season,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY Season
ORDER BY avg_purchase DESC;


-- Q8. PURCHASE FREQUENCY ANALYSIS

SELECT
    `Frequency of Purchases`,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY `Frequency of Purchases`
ORDER BY record_count DESC;


-- Q9. CATEGORY ANALYSIS USING HAVING
-- Show categories with more than 500 records

SELECT
    Category,
    COUNT(*) AS purchase_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
FROM customer_shopping
GROUP BY Category
HAVING COUNT(*) > 500
ORDER BY purchase_count DESC;


-- Q10. CUSTOMER AGE SEGMENTS USING CASE

SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        WHEN Age BETWEEN 56 AND 65 THEN '56-65'
        ELSE '66-70'
    END AS age_group,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM customer_shopping
GROUP BY age_group
ORDER BY MIN(Age);


-- Q11. CUSTOMER LOYALTY PROXY
-- Group customers by previous purchase history

SELECT
    CASE
        WHEN `Previous Purchases` BETWEEN 1 AND 10 THEN 'Low'
        WHEN `Previous Purchases` BETWEEN 11 AND 25 THEN 'Medium'
        ELSE 'High'
    END AS purchase_history_segment,
    COUNT(*) AS record_count,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase,
    ROUND(AVG(`Review Rating`), 2) AS avg_rating
FROM customer_shopping
GROUP BY purchase_history_segment
ORDER BY avg_purchase DESC;


-- Q12. REVIEW RATINGS BY CATEGORY

SELECT
    Category,
    COUNT(`Review Rating`) AS rated_records,
    ROUND(AVG(`Review Rating`), 2) AS avg_rating
FROM customer_shopping
GROUP BY Category
ORDER BY avg_rating DESC;


-- Q13. HIGH-AVERAGE-SPEND CATEGORIES
-- Find categories with an average above the overall average

SELECT
    Category,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS avg_purchase
FROM customer_shopping
GROUP BY Category
HAVING AVG(`Purchase Amount (USD)`) >
       (SELECT AVG(`Purchase Amount (USD)`)
        FROM customer_shopping)
ORDER BY avg_purchase DESC;


-- Q14. DISCOUNT USAGE BY AGE GROUP

SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        WHEN Age BETWEEN 56 AND 65 THEN '56-65'
        ELSE '66-70'
    END AS age_group,
    `Discount Applied`,
    COUNT(*) AS record_count
FROM customer_shopping
GROUP BY age_group, `Discount Applied`
ORDER BY MIN(Age), `Discount Applied`;
