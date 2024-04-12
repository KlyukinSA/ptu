from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

answer = {'van': 0,
          'saab': 1,
          'bus': 2,
          'opel': 3}
dataset = pn.read_csv('vehicle.csv', sep=',').to_numpy()[:, :-1]
dataset_answer = np.array(pn.read_csv('vehicle.csv', sep=','))[:, -1]
for i in range(len(dataset_answer)):
    dataset_answer[i] = answer[dataset_answer[i]]
dataset_answer = dataset_answer.astype(int)
classifiers = (SVC(probability=True), DecisionTreeClassifier(), GaussianNB(), )
titles = ("SVC", "decision tree", "gaussian nb")
for m, title in zip(classifiers, titles):
    accuracy = []
    for i in range(1, 10):
        print(i)
        adaBoost = AdaBoostClassifier(estimator=m, n_estimators=i)
        adaBoost.fit(dataset, dataset_answer)
        accuracy.append(adaBoost.score(dataset, dataset_answer))
    plt.title(title)
    plt.xlabel("classifiers count")
    plt.ylabel("accyracy")
    plt.plot(accuracy)
    plt.show()

print()
