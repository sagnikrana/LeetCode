# Write your MySQL query statement below

with stat as (select student_id, course_id,
             max(grade) over (partition by student_id ) as max_score
              from Enrollments
              order by course_id
              ),
              
              
# select enroll.student_id, enroll.course_id, max(stat.max_score) as grade
# from Enrollments enroll, stat
# where enroll.student_id = stat.student_id and stat.course_id = enroll.course_id and enroll.grade = stat.max_score
# group by enroll.student_id
# having enroll.course_id = max(enroll.course_id)
# ;
result as (
select enroll.student_id, enroll.course_id, stat.max_score as grade,
row_number() over (partition by enroll.student_id order by stat.max_score, enroll.course_id) as grade_rank
from Enrollments enroll, stat
where enroll.student_id = stat.student_id and stat.course_id = enroll.course_id and enroll.grade = stat.max_score)

select result.student_id, result.course_id, result.grade as grade
from result
where grade_rank = 1;