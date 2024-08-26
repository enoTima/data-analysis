import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('output.csv')
vector_i = df['2018'].values
vector_j = df['2019'].values
vector_k = df['2020'].values

X = np.column_stack((vector_i, vector_j, vector_k))

# Використаємо метод суміжності для агломеративної кластеризації
linked = linkage(X, 'ward')

# Побудова дендрограми
plt.figure(figsize=(10, 6))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Метод дендрограми')
plt.show()