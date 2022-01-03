# Write your MySQL query statement below
with stats as (
select person_name,
    turn,
sum(weight) over (order by turn) as cumsum
from Queue
order by turn)

select person_name from stats where cumsum <= 1000 order by turn desc limit 1