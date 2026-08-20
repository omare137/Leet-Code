# Write your MySQL query statement below
with joineddata as (
    select e.name as Employee, e.salary as Salary, d.name Department
    from Employee e
    left join department d on e.departmentid=d.id
)
select Employee, Salary, Department 
from (
    select Employee, Salary, Department, DENSE_RANK() over (partition by Department order by Salary desc) as salary_rank
    from joineddata
    
)t
where salary_rank<=3;

