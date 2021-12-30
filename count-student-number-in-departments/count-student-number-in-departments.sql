# Write your MySQL query statement below
with stat as (select dept_id, count(dept_id) as student_number from Student group by dept_id)

select dept_name, coalesce(student_number, 0) as student_number from stat right join Department d on stat.dept_id = d.dept_id
order by student_number desc, dept_name