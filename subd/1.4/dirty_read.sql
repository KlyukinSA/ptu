select * from tour where id = 2;
---concurrent (threads A and B)
A
begin;
update tour set price = price + 3 where id = 2;
select * from tour where id = 2;
B
begin;
select * from tour where id = 2;
commit;
A
rollback; 
---end concurrent
select * from tour where id = 2;
