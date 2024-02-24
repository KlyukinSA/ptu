select * from tour;
---concurrent (threads A and B)
B
begin;
A
begin;
update tour set price = price + 1 where id = 1;
B
update tour set price = price + 2 where id = 1;
A
commit;
B
commit;
---end concurrent
select * from tour; --- += 3
