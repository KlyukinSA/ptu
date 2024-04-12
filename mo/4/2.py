from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

dataset = pn.read_csv('vehicle.csv', sep=',').to_numpy()
X = dataset[:, :-1]
Y = dataset[:, -1]

answer = {
    'van': 0,
    'saab': 1,
    'bus': 2,
    'opel': 3
}
for i in range(len(Y)):
    Y[i] = answer[Y[i]]
Y = Y.astype(int)

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8)

classifiers = (SVC(probability=True), DecisionTreeClassifier(), GaussianNB())
titles = ("SVC", "decision tree", "gaussian nb")
start = 1
for m, title in zip(classifiers[start:], titles[start:]):
    accuracy = []
    n = [i for i in range(1, 101, 1)]
    for i in n:
        if i % 51 == 0:
            print(i)
        adaBoost = AdaBoostClassifier(estimator=m, n_estimators=i)
        adaBoost.fit(x_train, y_train)
        accuracy.append(adaBoost.score(x_test, y_test))
    plt.title(title)
    plt.xlabel("classifiers count")
    plt.ylabel("accyracy")
    plt.plot(n, accuracy)
    plt.show()

print()
