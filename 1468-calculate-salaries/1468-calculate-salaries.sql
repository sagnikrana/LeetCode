# Write your MySQL query statement below
with stat as (select *,
             max(salary) over (partition by company_id) as max_salary
             from Salaries)
             
             
select company_id, employee_id, employee_name,
case
when max_salary >= 1000 and max_salary <= 10000 then round(salary * (1-.24), 0)
when max_salary > 10000                         then round(salary * (1-.49), 0)
else round(salary,0) end as salary
from stat;