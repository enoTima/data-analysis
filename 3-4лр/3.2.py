import numpy as np
import matplotlib.pyplot as plt

n = 5

# Генеруємо масив x1, що підпорядковується нормальному розподілу
x1 = np.random.normal(loc=3 * n, scale=0.35 * n, size=105 + n)
x2 = np.random.normal(loc=3.2 * n, scale=0.4 * n, size=80 + 2 * n)
x3 = np.random.normal(loc=3.5 * n, scale=0.4 * n, size=135 + 2 * n)
x4 = np.random.uniform(low=2.5 * n, high=3.5 * n, size=160 - 2 * n)

# Побудова boxplot діаграми
fig, ax = plt.subplots()

data = [x1, x2, x3, x4]
labels = ['x1', 'x2', 'x3', 'x4']
colors = ['r', 'g', 'b', 'y']

boxes = ax.boxplot(data, notch='True', vert=True, labels=labels, patch_artist=True, whis=1.2, flierprops=dict(markersize=1))

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Boxplot Діаграма з узагальненою статистикою')
ax.set_xlabel('Вектори x1, x2, x3, x4')
ax.set_ylabel('Значення')

plt.grid(True)
plt.show()
