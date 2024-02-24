---concurrent (threads A and B)
A
begin;
select * from tour where id = 2;
B
begin;
update tour set price = price + 3 where id = 2;
commit;
A
select * from tour where id = 2;
commit;
---end concurrent
