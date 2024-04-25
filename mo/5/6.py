import pandas as pn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pn.read_csv('JohnsonJohnson.csv', sep=',').to_numpy()
q1 = []
q2 = []
q3 = []
q4 = []
q1year = []
q2year = []
q3year = []
q4year = []

for i in dataset:
    # print(i)
    if i[0][6] == '1':
        temp=[]
        temp.append(float(i[0].split()[0]))
        temp.append(float(i[1]))
        q1.append(temp)
        q1year.append(int(i[0][0:4]))
    if i[0][6] == '2':
        temp=[]
        temp.append(float(i[0].split()[0]))
        temp.append(float(i[1]))
        q2.append(temp)
        q2year.append(int(i[0][0:4]))
    if i[0][6] == '3':
        temp=[]
        temp.append(float(i[0].split()[0]))
        temp.append(float(i[1]))
        q3.append(temp)
        q3year.append(int(i[0][0:4]))
    if i[0][6] == '4':
        temp=[]
        temp.append(float(i[0].split()[0]))
        temp.append(float(i[1]))
        q4.append(temp)
        q4year.append(int(i[0][0:4]))
q1 = np.array(q1)
q2 = np.array(q2)
q3 = np.array(q3)
q4 = np.array(q4)

plt.plot(q1[:, 0], q1[:, 1], label="Q1")
plt.plot(q2[:, 0], q2[:, 1], label="Q2")
plt.plot(q3[:, 0], q3[:, 1], label="Q3")
plt.plot(q4[:, 0], q4[:, 1], label="Q4")
plt.xlabel("year")
plt.ylabel("profit")
plt.legend()
plt.show()


classif1 = LinearRegression().fit(q1[:, 0].reshape(len(q1[:, 0]), -1), q1[:, 1])
classif2 = LinearRegression().fit(q2[:, 0].reshape(len(q2[:, 0]), -1), q2[:, 1])
classif3 = LinearRegression().fit(q3[:, 0].reshape(len(q3[:, 0]), -1), q3[:, 1])
classif4 = LinearRegression().fit(q4[:, 0].reshape(len(q4[:, 0]), -1), q4[:, 1])

q1_predict = classif1.predict(q1[:, 0].reshape(len(q1[:, 0]), -1))
q2_predict = classif2.predict(q2[:, 0].reshape(len(q2[:, 0]), -1))
q3_predict = classif3.predict(q3[:, 0].reshape(len(q3[:, 0]), -1))
q4_predict = classif4.predict(q4[:, 0].reshape(len(q4[:, 0]), -1))

plt.plot(q1year, q1_predict , label="Q1")
plt.plot(q2year, q2_predict, label="Q2")
plt.plot(q3year, q3_predict, label="Q3")
plt.plot(q4year, q4_predict, label="Q4")
plt.xlabel("year")
plt.ylabel("profit")
plt.legend()
plt.show()

print("Q1: ", (q1_predict[00] - q1_predict[-1]) / (q1[0, 0] - q1[-1, 0]))
print("Q2: ", (q2_predict[00] - q2_predict[-1]) / (q2[0, 0] - q2[-1, 0]))
print("Q3: ", (q3_predict[00] - q3_predict[-1]) / (q3[0, 0] - q3[-1, 0]))
print("Q4: ", (q4_predict[00] - q4_predict[-1]) / (q4[0, 0] - q4[-1, 0]))

year_dataset = np.array(q1[:, 0]).reshape(len(q1[:, 0]),-1)
year_dataset = np.append(year_dataset,
                         np.array(q1[:, 1] + q2[:, 1] + q3[:, 1] + q4[:, 1]).reshape(len(q1[:, 1]), -1),
                         axis=1)
classif5 = LinearRegression().fit(year_dataset[:, 0].reshape(len(year_dataset[:, 0]), -1), year_dataset[:, 1])
plt.plot(year_dataset[:, 0], classif5.predict(year_dataset[:, 0].reshape(len(year_dataset[:, 0]), -1)))
plt.xlabel("year")
plt.ylabel("profit")
plt.legend()
plt.show()

print("profit in I - 2016: ", classif1.predict(np.array(2016).reshape(1, -1))[0])
print("profit in II - 2016: ", classif2.predict(np.array(2016).reshape(1, -1))[0])
print("profit in III - 2016: ", classif3.predict(np.array(2016).reshape(1, -1))[0])
print("profit in IV - 2016: ", classif4.predict(np.array(2016).reshape(1, -1))[0])
print("profit in 2016: ", classif5.predict(np.array(2016).reshape(1, -1))[0])

print("accuracy model - I: ", classif1.score(q1[:, 0].reshape(len(q1[:, 0]), -1), q1[:, 1]))
print("Тaccuracy model - II: ", classif2.score(q2[:, 0].reshape(len(q2[:, 0]), -1), q2[:, 1]))
print("accuracy model - III: ", classif3.score(q3[:, 0].reshape(len(q3[:, 0]), -1), q3[:, 1]))
print("accuracy model - IV: ", classif4.score(q4[:, 0].reshape(len(q4[:, 0]), -1), q4[:, 1]))
print("accuracy model - total: ", classif5.score(year_dataset[:, 0].reshape(len(year_dataset[:, 0]), -1), year_dataset[:, 1]))
print()
