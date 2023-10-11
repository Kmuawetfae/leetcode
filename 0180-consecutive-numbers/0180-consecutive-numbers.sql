/* Write your PL/SQL query statement below */
-- select num, count(*) 
-- from (select logs.*,
--              (row_number() over (order by id) -
--               row_number() over (partition by num order by id)
--              ) as grp
--       from logs
--      ) t
-- group by grp, num;

select distinct(num) as ConsecutiveNums
from (
  select num, count(*) as cnt
  from (select logs.*,
              (row_number() over (order by id) -
                row_number() over (partition by num order by id)
              ) as grp
        from logs
      ) t
  group by grp, num
) 
where cnt >= 3