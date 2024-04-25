import pandas as pn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pn.read_csv('cars.csv', sep=',').to_numpy()
classif = LinearRegression().fit(dataset[:, 0].reshape(len(dataset[:, 0]), -1), dataset[:, 1])

dataset_predict = classif.predict(dataset[:, 0].reshape(len(dataset[:, 0]), -1))

plt.plot(dataset[:, 0], dataset_predict)
plt.xlabel("speed")
plt.ylabel("lenght")

plt.scatter(dataset[:, 0], dataset[:, 1])
plt.legend('lr')
plt.show()

print("accuracy: ", classif.score(dataset[:, 0].reshape(len(dataset[:, 0]), -1), dataset[:, 1]))
print("predicted: ", classif.predict(np.array(40).reshape(1, -1))[0])
