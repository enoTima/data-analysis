import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('output.csv')
vector_i = df['2018'].values
vector_j = df['2019'].values
vector_k = df['2020'].values
data = np.column_stack((vector_i, vector_j, vector_k))

possible_k = range(1, 11)
inertia = []
for k in possible_k:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    inertia.append(kmeans.inertia_)

plt.plot(possible_k, inertia, marker='o')
plt.xlabel('Кількість кластерів')
plt.ylabel('Сума квадратів відстаней')
plt.title('Метод ліктя')
plt.show()