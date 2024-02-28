from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

arr = pd.read_csv('glass.csv', delimiter=',').to_numpy()
X = arr[:, 1:-1]
X = X.astype('float')
Y = arr[:, -1]
Y = Y.astype('int')
n_neighbours = [_ for _ in range(1, 128)]
accuracy = []
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.6)
for i in n_neighbours:
    knc = KNeighborsClassifier(n_neighbors=i)
    knc.fit(x_train, y_train)
    accuracy.append(accuracy_score(y_test, knc.predict(x_test)))
plt.plot(n_neighbours, accuracy)
plt.ylabel('Accuracy')
plt.xlabel('Neighbours')
plt.show()

mink = []
ch = []
euc = []
man = []
for _ in range(0, 10):
    d = {'minkowski': 0, 'chebyshev': 0, 'euclidean': 0, 'manhattan': 0}
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)
    for _ in range(0, 100):
        for metric in ['minkowski', 'chebyshev', 'euclidean', 'manhattan']:
            knc = KNeighborsClassifier(metric=metric)
            knc.fit(x_train, y_train)
            y_pred = knc.predict(x_test)
            score = (accuracy_score(y_test, y_pred) + d.get(metric)) / 2
            d[metric] = score
    mink.append(d.get('minkowski'))
    ch.append(d.get('chebyshev'))
    euc.append((d.get('euclidean')))
    man.append((d.get('manhattan')))
print('euclidean', np.mean(euc))
print('minkowski', np.mean(mink))
print('manhattan', np.mean(man))
print('chebyshev', np.mean(ch))

classes = []
for i in n_neighbours:
    knc = KNeighborsClassifier(n_neighbors=i)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    knc.fit(x_train, y_train)
    classes.append(knc.predict([[1.516, 11.7, 1.01, 1.19, 72.59, 0.43, 11.44, 0.02, 0.1]])[0])
plt.plot(n_neighbours, classes, 'bo')
plt.ylabel('Classes')
plt.xlabel('Neighbours')
plt.show()
