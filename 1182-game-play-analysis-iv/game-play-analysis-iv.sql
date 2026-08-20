# Write your MySQL query statement below
select round(count(diff)/(select count(distinct player_id) from activity),2) as fraction
from(
    select player_id, event_date, 
    datediff(event_date, (min(event_date) over (partition by player_id))) as diff 
    from activity
)t

where diff=1;
