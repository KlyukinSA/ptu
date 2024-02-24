import psycopg2
addr="dbname=ptu user=stepan"
conn1 = psycopg2.connect(addr)
conn2 = psycopg2.connect(addr)
cur1 = conn1.cursor()
cur2 = conn2.cursor()
new_isolation_level_to_try="READ COMMITTED"
conn1.set_session(new_isolation_level_to_try)
conn2.set_session(new_isolation_level_to_try)

def seeall():
    cur1.execute("SELECT * FROM tour;")
    print(cur1.fetchall())
    conn1.commit()

print("dirty read")

seeall()
cur1.execute("update tour set price = price + 3 where id = 1;")
cur1.execute("select * from tour where id = 1;")
print(cur1.fetchall())

cur2.execute("select * from tour where id = 1;")
print(cur2.fetchall())
conn2.commit()

conn1.rollback()
seeall()

print("non-repeatable read")
cur1.execute("select * from tour where id = 1;")
print(cur1.fetchall())
cur2.execute("update tour set price = price + 3 where id = 1;")
conn2.commit()
cur1.execute("select * from tour where id = 1;")
print(cur1.fetchall())
conn1.commit()
seeall()
