# Write your MySQL query statement below
select pr.firstName, pr.lastName, ad.city, ad.state
from Person as pr
left join Address as ad
on pr.personId = ad.personId