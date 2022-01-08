# Write your MySQL query statement below
with recursive reports as (
select employee_id from employees where manager_id=1 and employee_id!=1
union
select employees.employee_id from reports
inner join employees on reports.employee_id=employees.manager_id
)
select employee_id from reports