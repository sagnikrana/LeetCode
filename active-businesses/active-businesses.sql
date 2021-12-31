# Write your MySQL query statement below

# with stat as(select business_id, event_type, occurences,
# AVG(occurences) over (partition by event_type) as average
# from Events)

# select business_id from stat where
# stat.occurences > stat.average
# count(distinct(event_type)) = (select count(distinct(event_type)) from Events)
# group by business_id
# select * from stat;

select a.business_id
from events as a inner join

(select event_type, avg(occurences) as 'avg_occurences'
from events
group by event_type) as b
on a.event_type = b.event_type
where a.occurences > b.avg_occurences
group by a.business_id
having count(a.event_type) > 1