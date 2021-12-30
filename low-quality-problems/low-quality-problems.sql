# Write your MySQL query statement below
select problem_id from Problems where (likes/(likes+dislikes)) < 0.60
order by problem_id;