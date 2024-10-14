import numpy as np
import matplotlib.pyplot as plt


# # var1
# period = np.array([[True, True, True, False], 
#                    [True, True, False, False], 
#                    [True, True, True, False], 
#                    [True, False, True, False]])
# v1 = np.array([5, -4])
# v2 = np.array([6, 7])

# var2
period = np.array([[True, True, True, True], 
                   [True, True, False, False], 
                   [True, False, True, False], 
                   [False, False, False, True]])
v1 = np.array([4, 7])
v2 = np.array([-3, 5])
# v1 = np.array([-4, -7])
# v2 = np.array([5, 19])

rows, cols = period.shape
sts = 50
store=(rows * sts, cols * sts)
shs = 10
show =(rows * shs, cols * shs)
sequence = np.zeros(store, dtype=bool)

s = np.array(store) // 2
bs = 7
for a in range(-bs, bs+1):
    for b in range(-bs, bs+1):
        x = a * v1 + b * v2
        x[1]*=-1
        x += s
        for i in range(rows):
            for j in range(cols):
                sequence[x[1] + i, x[0] + j] = period[i, j]

sh = np.array(show) // 2
plt.imshow(sequence[s[0]-sh[0]:s[0]+sh[0], s[1]-sh[1]:s[1]+sh[1]], cmap='gray_r')
def get_vector_plot(v):
    return [sh[0], sh[0]+v[0]], [sh[1], sh[1]-v[1]]
def get_moved_vector_plot(v, base):
    return [sh[0]+base[0], sh[0]+base[0]+v[0]], [sh[1]-base[1], sh[1]-base[1]-v[1]]
plt.plot(*get_vector_plot(v1), c='b')
plt.plot(*get_vector_plot(v2), c='b')
plt.plot(*get_moved_vector_plot(v2, v1), c='b', linestyle='dashed')
v3, v4 = -v1, v2 + 2 * v1
plt.plot(*get_vector_plot(v3), c='r')
plt.plot(*get_vector_plot(v4), c='r')
plt.plot(*get_moved_vector_plot(v3, v4), c='r', linestyle='dashed')
ax = plt.gca()
ax.set_xticks(np.arange(-.5, show[0], 1))
ax.set_yticks(np.arange(-.5, show[1], 1))
ax.grid(color='k', linestyle='-', linewidth=1)
plt.title('Построенная последовательность')
plt.show()

# forbids = (v1, v2, v1+v2, v1-v2, v2-v1, [0, 0])
# for x in xs:
#     if not np.any([np.array_equal(x, y) for y in forbids]):
#         print(x)

print(v1+v2, v1-v2, v2-v1)
print(v3, v4)
