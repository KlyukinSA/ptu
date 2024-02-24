---concurrent (threads A and B)
A
begin;
select * from tour where id = 1;
B
begin;
update tour set price = price + 3 where id = 1;
commit;
A
select * from tour where id = 1;
commit;
---end concurrent
