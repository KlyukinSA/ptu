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
w = h = 15
sequence = np.zeros((rows * w, cols * h), dtype=bool)

s = np.array([rows * w//2, cols * h//2])
for a in range(-2, 3):
    for b in range(-2, 3):
        x = a * v1 + b * v2
        x[1]*=-1
        x += s
        for i in range(rows):
            for j in range(cols):
                sequence[x[1] + i, x[0] + j] = period[i, j]

plt.imshow(sequence, cmap='gray', interpolation='nearest')
plt.title('Построенная последовательность')
plt.show()

# forbids = (v1, v2, v1+v2, v1-v2, v2-v1, [0, 0])
# for x in xs:
#     if not np.any([np.array_equal(x, y) for y in forbids]):
#         print(x)

print(-v1, v2 + 2 * v1)
