from psycopg2 import connect
import matplotlib.pyplot as plt

addr="dbname=lab32 user=stepan"
conn = connect(addr)
cur = conn.cursor()

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
