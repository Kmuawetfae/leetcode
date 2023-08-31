# Write your MySQL query statement below

WITH table_1 AS (
  select id, temperature, lag(temperature) over (order by recordDate) as prev_temp, lag(recordDate) over (order by recordDate) as prev_date, recordDate
  from Weather
), table_2 as (
  select id, datediff(recordDate, prev_date) as day_diff, prev_temp, temperature

  FROM table_1
)
select 
id
FROM table_2 
where day_diff = 1 and prev_temp < temperature