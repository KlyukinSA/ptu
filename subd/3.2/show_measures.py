from psycopg2 import connect
# from numpy import arange, power, concatenate
import matplotlib.pyplot as plt

addr="dbname=lab32 user=stepan"
conn = connect(addr)
cur = conn.cursor()




# cur.execute("SELECT id, pg_column_size(roles_name) as size_v FROM actor ORDER BY size_v desc limit 1")
# top_id, top_size = cur.fetchone()
# print(top_id, top_size)
top_size = 152223
# linear = arange(1, 0, -1 / sample_size)
# print(linear)
# nonl = power(linear, 0.7) * top_size
# border = 0.05
# nonl = concatenate((power(arange(1, border, -1/30), 0.5), arange(border, 0, -1/5000)))
# nonl = nonl * top_size
# print(nonl)

# interval_size = 100
# for size_interval_left in nonl:
#     interval = [int(size_interval_left - 1), int(size_interval_left + interval_size)]
#     print(interval)
#     cur.execute("SELECT id, pg_column_size(roles_name) as size_v FROM actor WHERE pg_column_size(roles_name) between %s and %s limit 1", interval)
#     for id, size in cur:
#         print(id, size)

# print(ids)

# for id in ids:
#     cur.execute("SELECT roles_name as size_v FROM actor WHERE id = %s ORDER BY pg_column_size(roles_name) desc", [id])
#     print(cur.fetchall())
#     print(id)
#     break

times = []
row_sizes = []
cur.execute("SELECT time, row_size FROM access_time")
i=0
prev_row_size = 0
for time, row_size in cur:
    if row_size > prev_row_size:
        times.append(time.total_seconds())
        row_sizes.append(row_size)
    else:
        if i > 100:
            times.append(time.total_seconds())
            row_sizes.append(row_size)
            i = 0
        i+=1
    prev_row_size = row_size

plt.scatter(row_sizes, times)
plt.show()
