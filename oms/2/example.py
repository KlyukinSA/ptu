import numpy as np
import matplotlib.pyplot as plt

H = np.array([
	[0, 0, 1, 0, 0, 0, 4, 3],
	[0, 0, 1, 2, 3, 4, 5, 0],
	[2, 3, 2, 4, 0, 2, 6, 0],
	[0, 2, 3, 2, 1, -1, -2, 0],
	[0, 1, 2, 3, 1, -2, -1, 1],
	[0, 0, 1, 2, 1, 1, 1, 0],
	[-1, 0, 2, 0, 2, 3, -1, 0],
	[3, 0, 0, 4, 0, 4, 0, 3]
], int)
print(H.shape)
H = [[2, 1, 3, 2, 1, 0, 5, 4], [3, 2, 3, 2, 3, 0, 3, 0], [2, 1, 2, 1, 2, 3, 4, 4], [1, -1, 2, 1, -1, 0, 5, 0], [1, -1, 2, -2, 2, 3, 6, 5], [0, 1, 3, 1, 0, 0, 7, 0], [2, 2, 2, 3, 4, 4, 5, 8], [3, 4, 2, 4, 2, 5, 6, 5]]
H = np.array(H, int)
print(H.shape)

X = np.array([
	[0, 4, 3, 4, 3, 5, 0, 3],
	[2, 6, 3, 4, 0, 4, 0, 0],
	[5, 5, 5, 2, 2, 2, 3, 2],
	[2, 2, 2, 4, 0, 4, 3, 0],
	[4, 4, 4, 4, 3, 2, -1, 1],
	[3, 2, 3, 0, 3, 1, -2, 0],
	[3, 3, 3, 2, 2, 1, -1, 0],
	[0, 5, 5, 5, 0, 4, 0, 3]
], int)
print(X.shape)
X = [[4, 1, 3, 0, 3, 7, 0, 6], [3, 2, 3, 1, 0, 6, 0, 7], [4, 2, 3, 3, 2, 5, 5, 6], [3, 4, 3, 0, 3, 3, 0, 6], [0, 3, 4, 3, 0, 4, 4, 5], [2, 3, 2, 1, 3, 2, 2, 4], [1, 2, 4, 2, 0, 0, 3, 0], [4, 5, 0, 5, 3, 4, 0, 5]]
X = np.array(X, int)
print(X.shape)

H_ROWS, H_COLS = H.shape
X_ROWS, X_COLS = X.shape
Y_ROWS, Y_COLS = H_ROWS + X_ROWS - 1, H_COLS + X_COLS - 1

Y = np.zeros((Y_ROWS, Y_COLS), int)

for (i, j), m in np.ndenumerate(Y):
	for (k1, k2), h in np.ndenumerate(H):
		if 0 <= i - k1 < X_ROWS and 0 <= j - k2 < X_COLS:
			x = X[i-k1][j-k2]
			Y[i][j] += h*x
print('y(n1, n2) =')
print(Y)
Y = np.zeros((Y_ROWS, Y_COLS), int)

for (k1, k2), x in np.ndenumerate(X):
	temp = np.zeros((Y_ROWS, Y_COLS), int)
	for (m1, m2), h in np.ndenumerate(H):
		temp[m1 + k1][m2 + k2] = h * x
	Y += temp
	print('h(n1, n2) * x ({}, {})'.format(X_ROWS - k1, k2 + 1))
	print(temp)
	print()

print('y(n1, n2) = ')
print(Y)

Z = Y.T
X = np.arange(Y_ROWS)
Y = np.arange(Y_COLS)
X, Y = np.meshgrid(X, Y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, cmap='coolwarm')
plt.show()

fig, ax = plt.subplots()
ax.contour(X, Y, Z, levels=14, linewidths=0.5, colors='k')
cntr1 = ax.contourf(X, Y, Z, levels=14, cmap="RdBu_r")
fig.colorbar(cntr1, ax=ax)

plt.xticks(list(range(0,14+1)))
plt.yticks(list(range(0,14+1)))
plt.grid()
plt.show()
