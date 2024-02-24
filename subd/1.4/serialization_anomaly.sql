-- update tour set price = 300 where id = 2;
select * from tour;
---concurrent (threads A and B)
A
begin;
update tour set price = 300 where price < 200;
B
begin;
update tour set price = 100 where price > 200;
commit;
A
commit;
---end concurrent
select * from tour;
-- all should have became 100 https://dba.stackexchange.com/questions/315343/is-a-serialization-anomaly-only-possible-with-sum-count

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- causes error, all 100