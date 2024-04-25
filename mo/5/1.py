import pandas as pn
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

dataset = pn.read_csv('reglab1.txt', sep='\t').to_numpy()
scaler = StandardScaler()
scaler.fit(dataset)
dataset = scaler.transform(dataset)
z = dataset[:, 0]
x = dataset[:, 1]
y = dataset[:, 2]
zx = dataset[:, :2]
xy = dataset[:, 1:]
zy = dataset[:, [0, 2]]
print("y(x): ", LinearRegression().fit(x.reshape(len(x), -1), y).score(x.reshape(len(x), -1), y))
print("x(y): ", LinearRegression().fit(y.reshape(len(y), -1), x).score(y.reshape(len(y), -1), x))
print("z(x): ", LinearRegression().fit(x.reshape(len(x), -1), z).score(x.reshape(len(x), -1), z))
print("x(z): ", LinearRegression().fit(z.reshape(len(z), -1), x).score(z.reshape(len(z), -1), x))
print("y(z): ", LinearRegression().fit(z.reshape(len(z), -1), y).score(z.reshape(len(z), -1), y))
print("z(y): ", LinearRegression().fit(y.reshape(len(y), -1), z).score(y.reshape(len(y), -1), z))

print("y(z, x): ", LinearRegression().fit(zx, y).score(zx, y))
print("z(x, y): ", LinearRegression().fit(xy, z).score(xy, z))
print("x(z, y): ", LinearRegression().fit(zy, x).score(zy, x))

print()
