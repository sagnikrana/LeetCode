# Write your MySQL query statement below

with stat as (select viewer_id, max(article_id) as max_id, min(article_id) as min_id, view_date
from Views
group by view_date, viewer_id
having max_id <> min_id
order by view_date desc, viewer_id, article_id)

select distinct(viewer_id) as id from stat order by id;