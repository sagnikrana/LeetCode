# Write your MySQL query statement below

with userStat as (
select movie.user_id, users.name, count(movie.user_id) as ratings
from MovieRating movie left join Users users
on users.user_id = movie.user_id
group by movie.user_id
order by ratings desc, users.name
limit 1),

movieStat as (
select distinct(rating.movie_id), movie.title as title,
avg(rating) over (partition by rating.movie_id) as average
from MovieRating rating left join Movies movie
on rating.movie_id = movie.movie_id
where created_at between DATE("2020-02-01") and DATE("2020-02-28")
order by average desc, title
limit 1)

select name as results from UserStat
union
select title as results from movieStat;