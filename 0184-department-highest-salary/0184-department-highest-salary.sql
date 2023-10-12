/* Write your PL/SQL query statement below */
-- select departmentId, max(salary)
-- from Employee
-- group by departmentId

-- select *
-- from (
--   select departmentId, max(salary) as salary
--   from Employee
--   group by departmentId
-- ) natural join Employee

select d.name as Department, a.name as Employee, Salary
from (
  select *
  from (
    select departmentId, max(salary) as salary
    from Employee
    group by departmentId
  ) natural join Employee
) a join department d
on a.departmentId = d.id