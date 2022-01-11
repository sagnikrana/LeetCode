# Write your MySQL query statement below
WITH stat AS (
SELECT seller_id, SUM(price) AS total_sales_price FROM Sales GROUP BY seller_id
)
, top_seller AS (
SELECT seller_id, RANK() OVER(ORDER by total_sales_price DESC) as rnk FROM stat
) SELECT seller_id FROM top_seller WHERE rnk = 1