import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Згенеруємо випадковий одновимірний вектор для прикладу
data = np.random.rand(100)

# Оформимо дані у вигляді двовимірного масиву
data_2d = data.reshape(-1, 1)

# Визначимо кількість кластерів
k = 3

# Застосуємо K-Means
kmeans = KMeans(n_clusters=k)
kmeans.fit(data_2d)

# Отримаємо мітки кластерів та центри
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Візуалізація результатів
plt.scatter(range(len(data)), data, c=labels, cmap='viridis')
plt.scatter(range(len(centers)), centers, marker='X', s=200, color='red')
plt.xlabel('Номер точки')
plt.ylabel('Значення')
plt.title('K-Means для одного вектора')
plt.show()
