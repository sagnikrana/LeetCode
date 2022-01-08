# Write your MySQL query statement below
 with stat as (select project_id, project.employee_id,
dense_rank() over (partition by project_id order by experience_years desc) as employee_rank
from Project project left join Employee employee on project.employee_id = employee.employee_id)

select project_id, employee_id
from stat
where employee_rank = 1;