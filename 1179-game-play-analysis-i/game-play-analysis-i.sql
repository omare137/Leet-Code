# Write your MySQL query statement below
select event_date as first_login, player_id
from(
    select event_date, player_id, row_number() over (partition by player_id order by event_date asc) first
    from activity
)t
where first=1;