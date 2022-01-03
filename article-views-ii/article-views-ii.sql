# Write your MySQL query statement below

with cte as(
select *, row_number() over(partition by article_id, author_id, viewer_id, view_date order by article_id, author_id, viewer_id, view_date) as row_num
from views
)

select distinct viewer_id as id from cte
where row_num=1
group by viewer_id, view_date
having count(article_id)>1
order by id;