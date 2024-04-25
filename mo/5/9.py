import pandas as pn
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error

def RSS(real, predicate):
    answer = 0
    for i in range(len(real)):
        answer += (real[i] - predicate[i]) * (real[i] - predicate[i])
    return answer

dataset = pn.read_csv('nsw74psid1.csv', sep=',').to_numpy()
dataset_answer = dataset[:, -1]
dataset = dataset[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]]

x_train, x_test, y_train, y_test = train_test_split(dataset, dataset_answer, train_size=0.8)

linear_regression = LinearRegression().fit(x_train, y_train)
linear_pred = linear_regression.predict(x_test)
linear_mse = np.sum(np.square(y_test - linear_pred))
print(1)

svr_regression = SVR(C=1, kernel="rbf", epsilon=0.01).fit(x_train, y_train)
svr_pred = svr_regression.predict(x_test)
svr_mse = np.sum(np.square(y_test - svr_pred))
print(1)

tree_regression = DecisionTreeRegressor().fit(x_train, y_train)
tree_pred = tree_regression.predict(x_test)
tree_mse = np.sum(np.square(y_test - tree_pred))
print(1)

print("linear regerssion determintaion: ", linear_regression.score(x_train, y_train))
print("SVR determination: ", svr_regression.score(x_train, y_train))
print("decision tree regression: ", tree_regression.score(x_train, y_train))
print()
print("linear regerssion determintaion: ", linear_regression.score(x_test, y_test))
print("SVR determination: ", svr_regression.score(x_test, y_test))
print("decision tree regression: ", tree_regression.score(x_test, y_test))
print()
print("linear regression RSS on train: ", linear_mse)
print("SVR regression RSS on train: ", svr_mse)
print("decision tree regression RSS on train: ", tree_mse)


linear_pred = linear_regression.predict(x_train)
linear_mse = np.sum(np.square(y_train - linear_pred))

svr_pred = svr_regression.predict(x_train)
svr_mse = np.sum(np.square(y_train - svr_pred))

tree_pred = tree_regression.predict(x_train)
tree_mse = np.sum(np.square(y_train - tree_pred))
print()

print("linear regression RSS on train: ", linear_mse)
print("SVR regression RSS on train: ", svr_mse)
print("decision tree regression RSS on train: ", tree_mse)
