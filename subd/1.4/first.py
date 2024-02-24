import psycopg2
addr="dbname=ptu user=stepan"
conn1 = psycopg2.connect(addr)
conn2 = psycopg2.connect(addr)
cur1 = conn1.cursor()
cur2 = conn2.cursor()

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

# new_isolation_level_to_try="SERIALIZABLE"
# conn1.set_session(new_isolation_level_to_try)
# conn2.set_session(new_isolation_level_to_try)
# cur1.execute("update tour set price = 300 where price < 200;")
# cur2.execute("update tour set price = 100 where price > 200;")
# conn2.commit()
# try:
#     conn1.commit()
# except Exception:
#     pass

# print("try")
# seeall()
