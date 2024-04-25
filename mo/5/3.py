import pandas as pn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pn.read_csv('cygage.txt', sep='\t').to_numpy()
age = dataset[:, 0]
depth = dataset[:, 1]

classif = LinearRegression().fit(depth.reshape(len(depth), -1), age, sample_weight=[1, 1, 1, 1, 1, 1, 1, 1, 1,2 , 3 , 1])
predict_age = classif.predict(depth.reshape(len(depth), -1))

print(classif.score(depth.reshape(len(depth), -1), age))
plt.xlabel("depth")
plt.ylabel("age")
plt.plot(depth, age, depth, predict_age)
plt.legend(["real", "model"])
plt.show()
