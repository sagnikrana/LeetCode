# Write your MySQL query statement below
select customer_number from (
select customer_number, count(customer_number) as no_of_orders
from Orders
group by customer_number
order by no_of_orders desc
limit 1) res
;