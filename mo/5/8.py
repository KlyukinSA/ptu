import pandas as pn
from matplotlib import pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

dataset = pn.read_csv('svmdata6.txt', sep='\t').to_numpy()
epsilon_base = 0.01
MSE = []
epsilons = []
for i in range(1, 121):
    epsilon = epsilon_base * i
    epsilons.append(epsilon)
    classif = SVR(C=1, epsilon=epsilon, kernel="rbf").fit(dataset[:, 0].reshape(len(dataset[:, 0]), -1), dataset[:, 1])
    dataset_predict = classif.predict(dataset[:, 0].reshape(len(dataset[:, 0]), -1))
    MSE.append(mean_squared_error(dataset[:, 1], dataset_predict))
plt.plot(epsilons, MSE)
plt.xlabel("eps")
plt.ylabel("MSE")
plt.legend("error")
plt.show()
