# Write your MySQL query statement below

with stat as (select managerId, count(managerId) as reportCounts
from Employee
group by managerID
having reportCounts > 4)

select name from Employee where id in (select distinct managerId as managerId from stat);
