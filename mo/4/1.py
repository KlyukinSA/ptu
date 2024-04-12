from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pn
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

classifiers = (DecisionTreeClassifier(), GaussianNB(), KNeighborsClassifier(), SVC())
titles = ("decision tree", "gaussian nb", "K-neighbors", "SVC")
dataset = pn.read_csv('glass.csv', sep=',').to_numpy()[:, 1:-1]
dataset_answer = pn.read_csv('glass.csv', sep=',').to_numpy()[:, -1]
for m, title in zip(classifiers, titles):
    accuracy = []
    for i in range(1, 101):
        print(i)
        bagging = BaggingClassifier(estimator=m, n_estimators=i)
        bagging.fit(dataset, dataset_answer)
        accuracy.append(bagging.score(dataset, dataset_answer))
    plt.title(title)
    plt.xlabel("classifiers count")
    plt.ylabel("accuracy")
    plt.plot(accuracy)
    plt.show()
print()
