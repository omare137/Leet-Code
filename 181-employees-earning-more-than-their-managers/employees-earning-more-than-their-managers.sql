# Write your MySQL query statement below
select e.name as employee 
from Employee e
left join Employee m on e.managerid=m.id
where m.salary<e.salary



