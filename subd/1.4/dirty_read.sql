select * from tour where id = 1;
---concurrent (threads A and B)
A
begin;
update tour set price = price + 3 where id = 1;
select * from tour where id = 1;
B
begin;
select * from tour where id = 1;
commit;
A
rollback; 
---end concurrent
select * from tour where id = 1;
