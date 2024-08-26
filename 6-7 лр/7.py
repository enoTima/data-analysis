from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output.csv')
vector_i = df['2018'].values
vector_j = df['2019'].values
vector_k = df['2020'].values

X = np.column_stack((vector_i, vector_j, vector_k))

# кількість кластерів
k = 4

# Створення та навчання моделі K-Means
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Отримання міток кластерів та центрів
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Візуалізація результатів в тривимірному просторі
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='viridis')
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], marker='X', s=200, color='red')
plt.show()
