from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt
from numpy import polyfit

data_base_dir = "./"
avgc = 5
gnb = GaussianNB()

def graphs(set_values, accuracy, title):
    """
    plt.plot(set_values, accuracy)
    plt.title(title)
    plt.xlabel('training / all')
    plt.ylabel('accuracy')
    plt.show()
    """
    plt.plot(set_values, accuracy, scaley=False)
    plt.title(title)
    plt.xlabel('training / all')
    plt.ylabel('accuracy')
    plt.show()

def alter_proportion_show_graph(values, labels, name):
    start_train_size = 0.1
    set_values = []
    accuracy = []
    accuracy2 = []
    accuracy3 = []
    for i in range(1, 10):
        set_values.append(start_train_size * i)
        v, test_v, l, test_l = train_test_split(values, labels, train_size=(set_values[-1]))
        sum = 0
        for _ in range(avgc):
            gnb.fit(v, l)
            predicted = gnb.predict(test_v)
            sum += accuracy_score(test_l, predicted)
        accuracy.append(sum / avgc)
        sum2 = 0
        for _ in range(avgc):
            gnb.fit(v, l)
            predicted = gnb.predict(v)
            sum2 += accuracy_score(l, predicted)
        accuracy2.append(sum2 / avgc)
        accuracy3.append([sum / avgc, sum2 / avgc])
    graphs(set_values, accuracy, name)
    print(polyfit(set_values, accuracy, 1))
    graphs(set_values, accuracy2, name)
    print(polyfit(set_values, accuracy2, 1))
    graphs(set_values, accuracy3, name)

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

alter_proportion_show_graph(values, labels, "tic-tac-toe")


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
    return (np.array(values).astype(np.float64), labels)

f = open(data_base_dir + "spam.csv", "r")
lines = f.readlines()
f.close()
values, labels = prepareData(lines[1:])

alter_proportion_show_graph(values, labels, "spam")
