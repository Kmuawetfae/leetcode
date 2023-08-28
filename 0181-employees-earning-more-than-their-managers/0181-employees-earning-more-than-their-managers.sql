# Write your MySQL query statement below
select em_table.name as Employee
from (
  select name, salary, managerID
from Employee
where managerID is not null
) as em_table 
left join (
  select id, name, salary
from Employee
) as mana_table
on em_table.managerId = mana_table.id
where em_table.salary > mana_table.salary