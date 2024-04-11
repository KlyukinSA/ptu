import numpy as np
import pandas as pn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score

# берем данные из pluton.csv
dataset = pn.read_csv('pluton.csv', sep=',')

# print(dataset)
model = KMeans(n_clusters=3, max_iter=100)
model.fit(dataset.values)
print(model.predict(dataset.values))
print(model.n_iter_)
print(davies_bouldin_score(dataset.values, model.labels_))
print(silhouette_score(dataset.values, model.labels_))
print(calinski_harabasz_score(dataset.values, model.labels_))
dataset_1 = np.insert(dataset.values, 4, model.predict(dataset.values), 1)
plt.scatter(dataset_1[dataset_1[:, 4] == 0][:, 2], dataset_1[dataset_1[:, 4] == 0][:, 3])
plt.scatter(dataset_1[dataset_1[:, 4] == 1][:, 2], dataset_1[dataset_1[:, 4] == 1][:, 3])
plt.scatter(dataset_1[dataset_1[:, 4] == 2][:, 2], dataset_1[dataset_1[:, 4] == 2][:, 3])
plt.title("standartization off")
plt.show()

scaler = StandardScaler()
scaler.fit(dataset.values)
new_data = scaler.transform(dataset.values)
new_model = KMeans(n_clusters=3, max_iter=100)
new_model.fit(new_data)
print(new_model.predict(new_data))
print(new_model.n_iter_)
print(davies_bouldin_score(new_data, new_model.labels_))
print(silhouette_score(new_data, new_model.labels_))
print(calinski_harabasz_score(new_data, new_model.labels_))
new_data_1 = np.insert(new_data, 4, new_model.predict(new_data), 1)
plt.scatter(new_data_1[new_data_1[:, 4] == 0][:, 2], new_data_1[new_data_1[:, 4] == 0][:, 3])
plt.scatter(new_data_1[new_data_1[:, 4] == 1][:, 2], new_data_1[new_data_1[:, 4] == 1][:, 3])
plt.scatter(new_data_1[new_data_1[:, 4] == 2][:, 2], new_data_1[new_data_1[:, 4] == 2][:, 3])
plt.title("standartization on")
plt.show()
