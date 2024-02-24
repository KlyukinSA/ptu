---concurrent (threads A and B)
A
begin;
select * from tour;
B
begin;
INSERT INTO Tour (price, place) VALUES (400, 'Pariss');
commit;
A
select * from tour;
commit;
---end concurrent
