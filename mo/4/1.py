from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pn
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

dataset = pn.read_csv('glass.csv', sep=',').to_numpy()
x_train, x_test, y_train, y_test = train_test_split(dataset[:, 1:-1], dataset[:, -1], train_size=0.8)

classifiers = (DecisionTreeClassifier(), GaussianNB(), KNeighborsClassifier(), SVC())
titles = ("decision tree", "gaussian nb", "K-neighbors", "SVC")
for m, title in zip(classifiers, titles):
    accuracy = []
    for i in range(1, 101):
        bagging = BaggingClassifier(estimator=m, n_estimators=i)
        bagging.fit(x_train, y_train)
        accuracy.append(bagging.score(x_test, y_test))
    plt.title(title)
    plt.xlabel("classifiers count")
    plt.ylabel("accuracy")
    plt.plot(accuracy)
    plt.show()
print()
