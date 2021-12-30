# Write your MySQL query statement below

with stat as (
select name, departmentId, salary,
rank() over (partition by departmentId order by salary desc) as salary_rank
from Employee)

select d.name as Department,
stat.name as Employee,
stat.salary as Salary from Department d left join stat
on d.id = stat.departmentId where stat.salary_rank = 1;