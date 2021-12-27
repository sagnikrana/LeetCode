# Write your MySQL query statement below
with stat as (
select team_id, count(team_id) as team_size
    from Employee group by team_id
)

select e.employee_id, s.team_size from Employee e left join stat s on e.team_id = s.team_id;