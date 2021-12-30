# Write your MySQL query statement below
with stat as (select id, salary from Employee order by salary desc)

select case when min(salary) <> max(salary) then min(salary)
else null
end as 
SecondHighestSalary from (
select salary from stat limit 2
)res;