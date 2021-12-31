# Write your MySQL query statement below
with stats as (select order_id, order_date, customer_id,
row_number() over(partition by customer_id order by order_date desc) as "rank" from Orders)

select name as customer_name, s.customer_id, order_id, order_date
from stats s left join Customers c
on c.customer_id = s.customer_id
where s.rank < 4
order by customer_name, s.customer_id, order_date desc;