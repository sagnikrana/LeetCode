# Write your MySQL query statement below

select A.name as Employee
from Employee A, Employee B
where A.managerId = B.id
and A.salary > B.salary;