import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.svm import SVC

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(clf, xx, yy, ax=plt, **params):
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    out = ax.contourf(xx, yy, z, **params)
    return out

def build_scatter(clf, x_t, y_t, t, x_label='X1', y_label='X2'):
    x0, x1 = x_t[:, 0], x_t[:, 1]
    xx, yy = make_meshgrid(x0, x1)
    plot_contours(clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(x0, x1, c=y_t, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(t)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def get_x_y(array):
    y = array[:, -1]
    y[y == 'red'] = 0
    y[y == 'green'] = 1
    y = y.astype('int')
    x = array[:, : - 1]
    x = x.astype('float')
    return x, y

def load_train_test(t):
    arr = pd.read_csv('svmdata_' + t + '.txt', delimiter='\t').to_numpy()
    arr_test = pd.read_csv('svmdata_' + t + '_test.txt', delimiter='\t').to_numpy()
    np.random.shuffle(arr)
    np.random.shuffle(arr_test)
    return arr, arr_test

np_arr, np_arr_test = load_train_test('a')
x_train, y_train = get_x_y(np_arr)
x_test, y_test = get_x_y(np_arr_test)
svm_lin = svm.SVC(kernel='linear', gamma='auto')
svm_lin.fit(x_train, y_train)
build_scatter(svm_lin, x_test, y_test, t='Svm linear', x_label='X1', y_label='X2')
y_pred = svm_lin.predict(x_test)
print(confusion_matrix(y_test, y_pred)) #
print('Confusion matrix: ')

confusion_m = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_m)
disp.plot(cmap=plt.cm.Blues)
plt.show()
print(disp.confusion_matrix)
print('Support vectors size: ', svm_lin.support_vectors_.size)

np_arr, np_arr_test = load_train_test('b')
x_train, y_train = get_x_y(np_arr)
x_test, y_test = get_x_y(np_arr_test)
accuracy_test = []
accuracy_train = []
c = [_ for _ in np.arange(0.1, 600)]
for i in c:
    svm_lin = svm.SVC(kernel='linear', C=i)
    svm_lin.fit(x_train, y_train)
    accuracy_test.append(accuracy_score(y_test, svm_lin.predict(x_test)))
    accuracy_train.append(accuracy_score(y_train, svm_lin.predict(x_train)))

plt.plot(c, accuracy_test)
plt.title('Test data')
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.show()
plt.plot(c, accuracy_train)
plt.title('Train data')
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.show()
svm_lin = svm.SVC(kernel='linear', C=189)
svm_lin.fit(x_train, y_train)
print('Optimal :')
print(accuracy_score(y_test, svm_lin.predict(x_test)))

np_arr, np_arr_test = load_train_test('c')
x_train, y_train = get_x_y(np_arr)
x_test, y_test = get_x_y(np_arr_test)
C = 1.0
classifiers = (svm.SVC(kernel='linear', C=C),
svm.SVC(kernel='rbf', C=C),
svm.SVC(kernel='sigmoid', C=C),
svm.SVC(kernel='poly', degree=1, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=2, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=3, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=4, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=5, gamma='auto', C=C))
titles = ('SVC with linear kernel',
'SVC with RBF kernel',
'SVC with Sigmoid kernel',
'SVC with polynomial (degree=1) kernel',
'SVC with polynomial (degree=2) kernel',
'SVC with polynomial (degree=3) kernel',
'SVC with polynomial (degree=4) kernel',
'SVC with polynomial (degree=5) kernel')
for svms, title in zip(classifiers, titles):
    svms.fit(x_train, y_train)
    build_scatter(svms, x_test, y_test, title, x_label='X1', y_label='X2')

np_arr, np_arr_test = load_train_test('d')
x_train, y_train = get_x_y(np_arr)
x_test, y_test = get_x_y(np_arr_test)
C = 1.0
classifiers = (svm.SVC(kernel='rbf', C=C),
svm.SVC(kernel='sigmoid', C=C),
svm.SVC(kernel='poly', degree=1, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=2, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=3, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=4, gamma='auto', C=C),
svm.SVC(kernel='poly', degree=5, gamma='auto', C=C))
titles = ('SVC with RBF kernel',
'SVC with Sigmoid kernel',
'SVC with polynomial (degree=1) kernel',
'SVC with polynomial (degree=2) kernel',
'SVC with polynomial (degree=3) kernel',
'SVC with polynomial (degree=4) kernel',
'SVC with polynomial (degree=5) kernel')
for svm, title in zip(classifiers, titles):
    svm.fit(x_train, y_train)
    build_scatter(svm, x_test, y_test, title, x_label='X1', y_label='X2')

np_arr, np_arr_test = load_train_test('e')
x_train, y_train = get_x_y(np_arr)
x_test, y_test = get_x_y(np_arr_test)

def e(svm, g):
    C = 1.0
    classifiers = (
        svm.SVC(kernel='rbf', gamma=g, C=C),
    svm.SVC(kernel='sigmoid', gamma=g, C=C),
    svm.SVC(kernel='poly', degree=1, gamma=g, C=C),
    svm.SVC(kernel='poly', degree=2, gamma=g, C=C),
    svm.SVC(kernel='poly', degree=3, gamma=g, C=C),
    svm.SVC(kernel='poly', degree=4, gamma=g, C=C),
    svm.SVC(kernel='poly', degree=5, gamma=g, C=C))
    titles = (
        'SVC with RBF kernel, gamma = ' + str(g),
    'SVC with Sigmoid kernel, gamma = ' + str(g),
    'SVC with polynomial (degree=1) kernel, gamma = ' + str(g),
    'SVC with polynomial (degree=2) kernel, gamma = ' + str(g),
    'SVC with polynomial (degree=3) kernel, gamma = ' + str(g),
    'SVC with polynomial (degree=4) kernel, gamma = ' + str(g),
    'SVC with polynomial (degree=5) kernel, gamma = ' + str(g))
    for svm, title in zip(classifiers, titles):
        print(1)
        svm.fit(x_train, y_train)
        build_scatter(svm, x_test, y_test, title, x_label='X1', y_label='X2')

e(svm, 10)
e(svm, 150)
e(svm, 300)
