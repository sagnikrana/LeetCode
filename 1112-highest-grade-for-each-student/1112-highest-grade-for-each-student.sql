# Write your MySQL query statement below

with stat as (select student_id, course_id, grade,
row_number() over (partition by student_id order by grade desc, course_id) as grade_rank
from Enrollments)

select student_id, course_id, grade
from stat
where grade_rank = 1
order by student_id
;