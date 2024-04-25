import pandas as pn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = pn.read_csv('eustock.csv', sep=',').to_numpy()
plt.plot(dataset[:, 0])
plt.plot(dataset[:, 1])
plt.plot(dataset[:, 2])
plt.plot(dataset[:, 3])
plt.legend(['dax', 'smi', 'cac', 'ftse'])
plt.show()

data1 = np.array(range(len(dataset[:, 0]))).reshape(len(dataset[:, 0]), -1)
data2 = np.array(range(len(dataset[:, 1]))).reshape(len(dataset[:, 1]), -1)
data3 = np.array(range(len(dataset[:, 2]))).reshape(len(dataset[:, 2]), -1)
data4 = np.array(range(len(dataset[:, 3]))).reshape(len(dataset[:, 3]), -1)
data5 = np.array(range(len(dataset[:, 3]))).reshape(len(dataset[:, 3]), -1)
classif1 = LinearRegression().fit(data1, dataset[:, 0])
classif2 = LinearRegression().fit(data2, dataset[:, 1])
classif3 = LinearRegression().fit(data3, dataset[:, 2])
classif4 = LinearRegression().fit(data4, dataset[:, 3])

temp_dataset = []
for i in range(len(dataset[:, 3])):
    temp_dataset.append(np.sum(dataset[i]))
temp_dataset = np.array(temp_dataset).reshape(len(temp_dataset), -1)
classif5 = LinearRegression().fit(data5, temp_dataset)
plt.plot(classif1.predict(data1))
plt.plot(classif2.predict(data2))
plt.plot(classif3.predict(data3))
plt.plot(classif4.predict(data4))
plt.legend(['dax', 'smi', 'cac', 'ftse'])
plt.show()

plt.plot(classif5.predict(data5))
plt.show()
