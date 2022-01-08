# Write your MySQL query statement below

# with stat as (select managerId
# from Employee
# group by managerID
# having count(managerId) > 4)

# select name from Employee where id in (select distinct managerId as managerId from stat);


select name from Employee emp inner join (select managerId
from Employee
group by managerID
having count(managerId) > 4) res on emp.id = res.managerId;
