from sklearn.ensemble import StackingClassifier
from sklearn.impute import KNNImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pn

# готовим тренировочные данные
dataset_train = pn.read_csv('titanic_train.csv', sep=',')
# print(dataset_train.iloc[0])
dataset_train = dataset_train.drop(columns='Name')
dataset_train = dataset_train.drop(columns='Ticket')
dataset_train = dataset_train.drop(columns='Cabin')
dataset_train = dataset_train.drop(columns='Survived')
dataset_train = dataset_train.drop(columns='PassengerId')
dataset_train.loc[dataset_train['Sex'] == 'female', 'sex'] = 0
dataset_train.loc[dataset_train['Sex'] == 'male', 'sex'] = 1
dataset_train = dataset_train.drop(columns='Sex')
dataset_train.loc[dataset_train['Embarked'] == 'Q', 'Embarked'] = 0
dataset_train.loc[dataset_train['Embarked'] == 'S', 'Embarked'] = 1
dataset_train.loc[dataset_train['Embarked'] == 'C', 'Embarked'] = 2
dataset_train_answer = dataset_train['Pclass']
dataset_train = dataset_train.drop(columns='Pclass')
imputer = KNNImputer(n_neighbors=3)
dataset_train = imputer.fit_transform(dataset_train)

# готовим тестовые данные
dataset_test = pn.read_csv('titanic_test.csv', sep=',')
dataset_test = dataset_test.drop(columns='Name')
dataset_test = dataset_test.drop(columns='Ticket')
dataset_test = dataset_test.drop(columns='Cabin')
dataset_test = dataset_test.drop(columns='PassengerId')
dataset_test.loc[dataset_test['Sex'] == 'female', 'sex'] = 0
dataset_test.loc[dataset_test['Sex'] == 'male', 'sex'] = 1
dataset_test = dataset_test.drop(columns='Sex')
dataset_test.loc[dataset_test['Embarked'] == 'Q', 'Embarked'] = 0
dataset_test.loc[dataset_test['Embarked'] == 'S', 'Embarked'] = 1
dataset_test.loc[dataset_test['Embarked'] == 'C', 'Embarked'] = 2
dataset_test_answer = dataset_test['Pclass']
dataset_test = dataset_test.drop(columns='Pclass')
imputer = KNNImputer(n_neighbors=3)
dataset_test = imputer.fit_transform(dataset_test)

# строим классификатор
one_classifiers = [
    ("descision tree", DecisionTreeClassifier()),
    ("gaussian nb", GaussianNB()),
    ("SVC", SVC()),
    ("k-neighbors", KNeighborsClassifier())
]
titles = ("descision tree", "gaussian nb", "SVC", "k-neighbors")

for m, title in zip(one_classifiers, titles):
    klassificator = StackingClassifier(estimators=[m])
    klassificator.fit(dataset_train, dataset_train_answer)
    accuracy = klassificator.score(dataset_test, dataset_test_answer)
    print(title, accuracy)


t_g = [("descision tree", DecisionTreeClassifier()), ("gaussian nb", GaussianNB())]
t_s = [("descision tree", DecisionTreeClassifier()), ("SVC", SVC())]
t_n = [("k-neighbors", KNeighborsClassifier()), ("descision tree", DecisionTreeClassifier())]
g_s = [("gaussian nb", GaussianNB()), ("SVC", SVC())]
g_n = [("k-neighbors", KNeighborsClassifier()), ("gaussian nb", GaussianNB())]
s_n = [("k-neighbors", KNeighborsClassifier()), ("SVC", SVC())]
titles_2 = ("descision tree + gaussian nb", "descision tree + SVC", "descision tree + k-neighbors", "gaussian nb + SVC", "gaussian nb + k-neighbors", "SVC + k-neighbors")

for m, title in zip([t_g, t_s, t_n, g_s, g_n, s_n], titles_2):
    klassificator = StackingClassifier(estimators=m)
    klassificator.fit(dataset_train, dataset_train_answer)
    accuracy = klassificator.score(dataset_test, dataset_test_answer)
    print(title, accuracy)

t_g_s = [("descision tree", DecisionTreeClassifier()), ("gaussian nb", GaussianNB()), ("SVC", SVC())]
t_g_n = [("descision tree", DecisionTreeClassifier()), ("gaussian nb", GaussianNB()), ("k-neighbors", KNeighborsClassifier())]
g_s_n = [("gaussian nb", GaussianNB()), ("SVC", SVC()), ("k-neighbors", KNeighborsClassifier())]
t_s_n = [("descision tree", DecisionTreeClassifier()), ("SVC", SVC()), ("K-Neighbors", KNeighborsClassifier())]
titles_3 = ("descision tree + gaussian nb + SVC", "descision tree + gaussian nb + k-neighbors", "gaussian nb + SVC + k-neighbors", "descision tree + SVC + k-neighbors")

for m, title in zip([t_g_s, t_g_n, g_s_n, t_s_n], titles_3):
    klassificator = StackingClassifier(estimators=m)
    klassificator.fit(dataset_train, dataset_train_answer)
    accuracy = klassificator.score(dataset_test, dataset_test_answer)
    print(title, accuracy)

t_g_s_n = [("descision tree", DecisionTreeClassifier()), ("gaussian nb", GaussianNB()), ("SVC", SVC()), ("k-neighbors", KNeighborsClassifier())]
titles_4 = ("descision tree + gaussian nb + SVC + k-neighbors")

klassificator = StackingClassifier(estimators=t_g_s_n)
klassificator.fit(dataset_train, dataset_train_answer)
accuracy = klassificator.score(dataset_test, dataset_test_answer)
print(titles_4, accuracy)

print()
