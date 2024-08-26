import numpy as np
import matplotlib.pyplot as plt

n = 5

# Генеруємо дані для прикладу
x1 = np.random.normal(loc=3 * n, scale=0.35 * n, size=105 + n)
x2 = np.random.normal(loc=3.2 * n, scale=0.4 * n, size=80 + 2 * n)
x3 = np.random.normal(loc=3.5 * n, scale=0.4 * n, size=135 + 2 * n)
x4 = np.random.uniform(low=2.5 * n, high=3.5 * n, size=160 - 2 * n)

x1.resize(x4.shape)
x2.resize(x3.shape)

# Об'єднуємо вектори з допомогою concatenate
x1_plus_x4 = x1 + x4
x2_union_x4 = np.concatenate([x2, x4])
avg_x2_x3 = (x2 + x3) / 2

# Побудова boxplot діаграми для нових векторів
fig, ax = plt.subplots()

data = [x1_plus_x4, x2_union_x4, avg_x2_x3]
labels = ['x1 + x4', 'x2 union x4', '(x2 + x3)/2']
colors = ['cyan', 'magenta', 'yellow'] #кольори відповідні номерам 21-23 в мові Р

# Визначаємо кількість спостережень у групах
observations_counts = [len(x1_plus_x4), len(x2_union_x4), len(avg_x2_x3)]
widths = np.sqrt(observations_counts)
widths /= 45

boxprops = dict(linewidth=1.5, color='black')  # товщина ліній та колір контурів

boxes = ax.boxplot(data, notch=True, vert=True, labels=labels, patch_artist=True, widths=widths, whis=[0.9, n/(n+2)], boxprops=boxprops)

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Додаємо кольори ліній контурів та товщину ліній
for median in boxes['medians']:
    median.set(color='black', linewidth=1.5)

# Додавання узагальненої статистики
for i, d in enumerate(data):
    mean = np.mean(d)
    median = np.median(d)
    ax.text(i + 1, mean, f'Mean: {mean:.2f}', ha='center', va='bottom', fontweight='bold', color='black')
    ax.text(i + 1, median, f'Median: {median:.2f}', ha='center', va='top', fontweight='bold', color='black')

ax.set_title('Boxplot Діаграма')
ax.set_xlabel('Вектори x1 + x4, x2 union x4, (x2 + x3)/2')
ax.set_ylabel('Значення')

plt.grid(True)
plt.show()
