import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering

def plot_dendrogram(model, **kwargs):
    # Создайте матрицу связей, а затем постройте дендрограмму

    # создаем количество выборок под каждым узлом
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for temp, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # листовой узел
            else:
                current_count += counts[child_idx - n_samples]
        counts[temp] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Постройте соответствующую дендрограмму
    dendrogram(linkage_matrix, **kwargs)

dataset = pn.read_csv('votes.csv', sep=',').to_numpy()
dataset = np.nan_to_num(dataset, nan=0)

print(dataset)

# установка distance_threshold = 0 гарантирует, что мы вычислим полное дерево.
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None, linkage='single')

model = model.fit(dataset)
plt.title('dendogramm')
# строим три верхних уровня дендрограммы
plot_dendrogram(model, truncate_mode='level', p=10)
plt.show()
