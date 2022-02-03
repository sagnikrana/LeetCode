# Write your MySQL query statement below
with stat as (select customer_id, 
count(distinct (product_key)) as products_ordered
from Customer
group by customer_id
having products_ordered = (select count(distinct(product_key)) from Product))


select customer_id from stat;

