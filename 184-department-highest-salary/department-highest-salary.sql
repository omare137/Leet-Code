WITH JoinedData AS (
select d.name as Department, e.name as employee, e.salary as Salary
from Employee e
left join Department d on e.departmentid=d.id)

SELECT employee, department, salary
FROM JoinedData
WHERE (department, salary) IN (
    SELECT department, MAX(salary)
    FROM joineddata
    GROUP BY department
);
