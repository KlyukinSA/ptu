import numpy as np
import pandas as pn
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

dataset1 = pn.read_csv('clustering_1.csv', sep='\t').to_numpy()
dataset2 = pn.read_csv('clustering_2.csv', sep='\t').to_numpy()
dataset3 = pn.read_csv('clustering_3.csv', sep='\t').to_numpy()
x1 = dataset1[:, 0]
y1 = dataset1[:, 1]
x2 = dataset2[:, 0]
y2 = dataset2[:, 1]
x3 = dataset3[:, 0]
y3 = dataset3[:, 1]
plt.scatter(x1, y1)
plt.title("clustering_1.csv")
plt.show()
plt.scatter(x2, y2)
plt.title("clustering_2.csv")
plt.show()
plt.scatter(x3, y3)
plt.title("clustering_3.csv")
plt.show()

# 1 AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=2)
model.fit(dataset1)
dataset_1 = np.insert(dataset1, 2, model.fit_predict(dataset1), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.title("clustering_1.csv agglomerative_clustering")
plt.show()

# 2 AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=3)
model.fit(dataset2)
dataset_1 = np.insert(dataset2, 2, model.fit_predict(dataset2), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
plt.title("clustering_2.csv agglomerative_clustering")
plt.show()

# 3 AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=2, linkage='ward') # 'single' uses the minimum of the distances between all observations of the two sets.
model.fit(dataset3)
dataset_1 = np.insert(dataset3, 2, model.fit_predict(dataset3), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.title("clustering_3.csv agglomerative_clustering")
plt.show()

# 1 k-means
model = KMeans()
model.fit(dataset1)
print(model.n_iter_)
print(silhouette_score(dataset1, model.labels_))
predicat = model.predict(dataset1)
dataset_1 = np.insert(dataset1, 2, model.predict(dataset1), 1)
if 0 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
if 1 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
if 2 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
if 3 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 3][:, 0], dataset_1[dataset_1[:, 2] == 3][:, 1])
if 4 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 4][:, 0], dataset_1[dataset_1[:, 2] == 4][:, 1])
if 5 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 5][:, 0], dataset_1[dataset_1[:, 2] == 5][:, 1])
if 6 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 6][:, 0], dataset_1[dataset_1[:, 2] == 6][:, 1])
if 7 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 7][:, 0], dataset_1[dataset_1[:, 2] == 7][:, 1])
plt.title("clustering_1.scb kMeans, no count")
plt.show()

# 2 k-means
model = KMeans()
model.fit(dataset2)
print(model.n_iter_)
print(silhouette_score(dataset2, model.labels_))
predicat = model.predict(dataset2)
dataset_1 = np.insert(dataset2, 2, model.predict(dataset2), 1)
if 0 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
if 1 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
if 2 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
if 3 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 3][:, 0], dataset_1[dataset_1[:, 2] == 3][:, 1])
if 4 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 4][:, 0], dataset_1[dataset_1[:, 2] == 4][:, 1])
if 5 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 5][:, 0], dataset_1[dataset_1[:, 2] == 5][:, 1])
if 6 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 6][:, 0], dataset_1[dataset_1[:, 2] == 6][:, 1])
if 7 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 7][:, 0], dataset_1[dataset_1[:, 2] == 7][:, 1])
plt.title("clustering_2.csv kMeans, no count")
plt.show()


# 3 k-means
model = KMeans()
model.fit(dataset3)
print(model.n_iter_)
print(silhouette_score(dataset3, model.labels_))
predicat = model.predict(dataset3)
dataset_1 = np.insert(dataset3, 2, model.predict(dataset3), 1)
if 0 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
if 1 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
if 2 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
if 3 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 3][:, 0], dataset_1[dataset_1[:, 2] == 3][:, 1])
if 4 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 4][:, 0], dataset_1[dataset_1[:, 2] == 4][:, 1])
if 5 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 5][:, 0], dataset_1[dataset_1[:, 2] == 5][:, 1])
if 6 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 6][:, 0], dataset_1[dataset_1[:, 2] == 6][:, 1])
if 7 in predicat:
    plt.scatter(dataset_1[dataset_1[:, 2] == 7][:, 0], dataset_1[dataset_1[:, 2] == 7][:, 1])
plt.title("clustering_3.csv kMeans, no count")
plt.show()

# 1 k-means
model = KMeans(n_clusters=2)
model.fit(dataset1)
print(model.n_iter_)
print(silhouette_score(dataset1, model.labels_))
dataset_1 = np.insert(dataset1, 2, model.predict(dataset1), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.title("clustering_1.csv kMeans")
plt.show()

# 2 k-means
model = KMeans(n_clusters=3)
model.fit(dataset2)
print(model.n_iter_)
print(silhouette_score(dataset2, model.labels_))
dataset_1 = np.insert(dataset2, 2, model.predict(dataset2), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
plt.title("clustering_2.csv kMeans")
plt.show()

# 3 k-means
model = KMeans(n_clusters=5)
model.fit(dataset3)
print(model.n_iter_)
print(silhouette_score(dataset3, model.labels_))
dataset_1 = np.insert(dataset3, 2, model.predict(dataset3), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 3][:, 0], dataset_1[dataset_1[:, 2] == 3][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 4][:, 0], dataset_1[dataset_1[:, 2] == 4][:, 1])
plt.title("clustering_3.csv kMeans")
plt.show()

# 1 DBSCAN
model = DBSCAN()
model.fit(dataset1)
dataset_1 = np.insert(dataset1, 2, model.fit_predict(dataset1), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.title("clustering_1.csv DBSCAN")
plt.show()

# 2 DBSCAN
model = DBSCAN()
model.fit(dataset2)
dataset_1 = np.insert(dataset2, 2, model.fit_predict(dataset2), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 2][:, 0], dataset_1[dataset_1[:, 2] == 2][:, 1])
plt.title("clustering_2.csv DBSCAN")
plt.show()

# 3 DBSCAN
model = DBSCAN()
model.fit(dataset3)
dataset_1 = np.insert(dataset3, 2, model.fit_predict(dataset3), 1)
plt.scatter(dataset_1[dataset_1[:, 2] == 0][:, 0], dataset_1[dataset_1[:, 2] == 0][:, 1])
plt.scatter(dataset_1[dataset_1[:, 2] == 1][:, 0], dataset_1[dataset_1[:, 2] == 1][:, 1])
plt.title("clustering_3.csv DBSCAN")
plt.show()
