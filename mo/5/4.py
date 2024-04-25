import pandas as pn
from matplotlib import pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def RSS(real, predicate):
    answer = 0
    for i in range(len(real)):
        answer += (real[i] - predicate[i]) * (real[i] - predicate[i])
    return answer

def MAE(real, predicate):
    answer = 0
    for i in range(len(real)):
        answer += abs(real[i] - predicate[i])
    return answer / (len(real))

dataset = pn.read_csv('longley.csv', sep=',').to_numpy()
dataset = dataset[:, [0, 1, 2, 3, 5, 6]]
dataset_answer = dataset[:, -1]
dataset_test, dataset_train, dataset_answer_test, dataset_answer_train \
    = train_test_split(dataset, dataset_answer, train_size=0.5)

classif1 = LinearRegression().fit(dataset_train, dataset_answer_train)
print("1 score train: ", classif1.score(dataset_train, dataset_answer_train))
print("1 score test: ", classif1.score(dataset_test, dataset_answer_test))
print("1 RSS train: ", RSS(dataset_answer_train, classif1.predict(dataset_train)))
print("1 RSS test: ", RSS(dataset_answer_test, classif1.predict(dataset_test)))
print("1 MAE train: ", mean_absolute_error(dataset_answer_train, classif1.predict(dataset_train)))
print("1 MAE test: ", mean_absolute_error(dataset_answer_test, classif1.predict(dataset_test)), "\n\n")

classif2 = LinearRegression().fit(dataset_answer_train.reshape(len(dataset_answer_train), -1), dataset_train)
print("2 score train: ", classif2.score(dataset_answer_train.reshape(len(dataset_answer_train), -1), dataset_train))
print("2 score test: ", classif2.score(dataset_answer_test.reshape(len(dataset_answer_test), -1), dataset_test))
print("2 RSS train: ",
      RSS(dataset_train, classif2.predict(dataset_answer_train.reshape(len(dataset_answer_train), -1))))
print("2 RSS test: ", RSS(dataset_test, classif2.predict(dataset_answer_test.reshape(len(dataset_answer_test), -1))))
print("2 MAE train: ",
      mean_absolute_error(dataset_train, classif2.predict(dataset_answer_train.reshape(len(dataset_answer_train), -1))))
print("2 MAE test: ",
      mean_absolute_error(dataset_test, classif2.predict(dataset_answer_test.reshape(len(dataset_answer_test), -1))))

accuracy_train = []
accuracy_test = []
l = []
for i in range(26):
    l.append(10 ** (-3 + 0.2 * i))
    ridge = Ridge(alpha=l[-1])
    ridge.fit(dataset_train, dataset_answer_train)
    accuracy_train.append(mean_absolute_error(dataset_answer_train, ridge.predict(dataset_train)))
    accuracy_test.append(mean_absolute_error(dataset_answer_test, ridge.predict(dataset_test)))
plt.plot(l, accuracy_train, l, accuracy_test)
plt.legend(['train', 'test'])
plt.show()
