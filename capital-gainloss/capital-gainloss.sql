# Write your MySQL query statement below
with stat as (select stock_name, operation, -1 * sum(price) as tran
from Stocks
where operation = 'Buy'
group by stock_name
union
select stock_name, operation, sum(price) as tran
from Stocks
where operation = 'Sell' 
group by stock_name       
)

select 
stock_name,
sum(tran) as capital_gain_loss
from stat
group by stock_name;