# Write your MySQL query statement below
delete p
from Person p, Person q
where p.Id>q.id AND q.Email = p.Email