import pandas as pn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def RSS(real, predicate):
    answer = 0
    for i in range(len(real)):
        answer += (real[i] - predicate[i]) * (real[i] - predicate[i])
    return answer

dataset = pn.read_csv('reglab.txt', sep='\t').to_numpy()
y = dataset[:, 0]
x1 = dataset[:, 1]
x2 = dataset[:, 2]
x3 = dataset[:, 3]
x4 = dataset[:, 4]
x12 = dataset[:, [1, 2]]
x13 = dataset[:, [1, 3]]
x14 = dataset[:, [1, 4]]
x23 = dataset[:, [2, 3]]
x24 = dataset[:, [2, 4]]
x34 = dataset[:, [3, 4]]
x123 = dataset[:, [1, 2, 3]]
x124 = dataset[:, [1, 2, 4]]
x134 = dataset[:, [1, 3, 4]]
x234 = dataset[:, [2, 3, 4]]

print("y(x1): ", LinearRegression().fit(x1.reshape(len(x1), -1), y).score(x1.reshape(len(x1), -1), y), "\t",
      RSS(y, LinearRegression().fit(x1.reshape(len(x1), -1), y).predict(x1.reshape(len(x1), -1))))
mse = mean_squared_error(y, LinearRegression().fit(x1.reshape(len(x1), -1), y).predict(x1.reshape(len(x1), -1))) * (len(x1))
print("RSS:  ", mse)
print("y(x2): ", LinearRegression().fit(x2.reshape(len(x2), -1), y).score(x2.reshape(len(x2), -1), y), "\t",
      RSS(y, LinearRegression().fit(x2.reshape(len(x2), -1), y).predict(x2.reshape(len(x2), -1))))
print("y(x3): ", LinearRegression().fit(x3.reshape(len(x3), -1), y).score(x3.reshape(len(x3), -1), y), "\t",
      RSS(y, LinearRegression().fit(x3.reshape(len(x3), -1), y).predict(x3.reshape(len(x3), -1))))
print("y(x4): ", LinearRegression().fit(x4.reshape(len(x4), -1), y).score(x4.reshape(len(x4), -1), y), "\t",
      RSS(y, LinearRegression().fit(x4.reshape(len(x4), -1), y).predict(x4.reshape(len(x4), -1))))

print("y(x1, x2): ", LinearRegression().fit(x12.reshape(len(x12), -1), y).score(x12.reshape(len(x12), -1), y), "\t",
      RSS(y, LinearRegression().fit(x12.reshape(len(x12), -1), y).predict(x12.reshape(len(x12), -1))))
print("y(x1, x3): ", LinearRegression().fit(x13.reshape(len(x13), -1), y).score(x13.reshape(len(x13), -1), y), "\t",
      RSS(y, LinearRegression().fit(x13.reshape(len(x13), -1), y).predict(x13.reshape(len(x13), -1))))
print("y(x1, x4): ", LinearRegression().fit(x14.reshape(len(x14), -1), y).score(x14.reshape(len(x14), -1), y), "\t",
      RSS(y, LinearRegression().fit(x14.reshape(len(x14), -1), y).predict(x14.reshape(len(x14), -1))))
print("y(x2, x3): ", LinearRegression().fit(x23.reshape(len(x23), -1), y).score(x23.reshape(len(x23), -1), y), "\t",
      RSS(y, LinearRegression().fit(x23.reshape(len(x23), -1), y).predict(x23.reshape(len(x23), -1))))
print("y(x2, x4): ", LinearRegression().fit(x24.reshape(len(x24), -1), y).score(x24.reshape(len(x24), -1), y), "\t",
      RSS(y, LinearRegression().fit(x24.reshape(len(x24), -1), y).predict(x24.reshape(len(x24), -1))))
print("y(x3, x4): ", LinearRegression().fit(x34.reshape(len(x34), -1), y).score(x34.reshape(len(x34), -1), y), "\t",
      RSS(y, LinearRegression().fit(x34.reshape(len(x34), -1), y).predict(x34.reshape(len(x34), -1))))

print("y(x1, x2, x3): ", LinearRegression().fit(x123.reshape(len(x123), -1), y).score(x123.reshape(len(x123), -1), y), "\t",
      RSS(y, LinearRegression().fit(x123.reshape(len(x123), -1), y).predict(x123.reshape(len(x123), -1))))
print("y(x1, x2, x4): ", LinearRegression().fit(x124.reshape(len(x124), -1), y).score(x124.reshape(len(x124), -1), y), "\t",
      RSS(y, LinearRegression().fit(x124.reshape(len(x124), -1), y).predict(x124.reshape(len(x124), -1))))
print("y(x1, x3, x4): ", LinearRegression().fit(x134.reshape(len(x134), -1), y).score(x134.reshape(len(x134), -1), y), "\t",
      RSS(y, LinearRegression().fit(x134.reshape(len(x134), -1), y).predict(x134.reshape(len(x134), -1))))
print("y(x2, x3, x4): ", LinearRegression().fit(x234.reshape(len(x234), -1), y).score(x234.reshape(len(x234), -1), y), "\t",
      RSS(y, LinearRegression().fit(x234.reshape(len(x234), -1), y).predict(x234.reshape(len(x234), -1))))
