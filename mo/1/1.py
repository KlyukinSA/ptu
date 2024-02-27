from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt

data_base_dir = "./"

def graphs(set_values, accuracy, title):
    plt.plot(set_values, accuracy)
    plt.title(title)
    plt.xlabel('training / all')
    plt.ylabel('accuracy')
    plt.show()
    plt.plot(set_values, accuracy, scaley=False)
    plt.title(title)
    plt.xlabel('training / all')
    plt.ylabel('accuracy')
    plt.show()

gnb = GaussianNB()
f = open(data_base_dir + "tic_tac_toe.txt", "r")
lines = f.readlines()
f.close()
values = []
labels = []
values_map = {
    'x': 0,
    'o': 1,
    'b': 2
}
labels_map = {
    'positive': 0,
    'negative': 1
}
for i in range(0, len(lines)):
    line = lines[i]
    line = line.rstrip("\n")
    array = line.split(",")
    value = list(map(lambda v: values_map[v], array[:9]))
    label = list(map(lambda l: labels_map[l], array[9:]))
    values.append(value)
    labels.extend(label)

start_train_size = 0.1
set_values = []
accuracy = []
for i in range(1, 10):
    set_values.append(start_train_size * i)
    v, test_v, l, test_l = train_test_split(values, labels, train_size=(set_values[-1]))
    gnb.fit(v, l)
    predicted = gnb.predict(test_v)
    accuracy.append(accuracy_score(test_l, predicted))
graphs(set_values, accuracy, "tic-tac-toe")

labels_map = {
    'spam': 0,
    'nonspam': 1
}

def prepareData(lines):
    values = []
    labels = []
    for line in lines:
        tmp = line
        tmp = tmp.rstrip("\n")
        tmp = tmp.replace('"', "")
        lines = tmp.split(",")
        values.append(lines[1:-1])
        labels.append(labels_map[lines[-1]])
    return (np.array(values).astype(np.float), labels)

f = open(data_base_dir + "spam.csv", "r")
lines = f.readlines()
f.close()
values, labels = prepareData(lines[1:])
set_values = []
accuracy = []
start = 0.1
for i in range(1, 10):
    set_values.append(start * i)
    v, test_v, l, test_l = train_test_split(values, labels, test_size=set_values[-1])
    gnb.fit(v, l)
    predicted = gnb.predict(test_v)
    accuracy.append(accuracy_score(test_l, predicted))
graphs(set_values, accuracy, "spam")