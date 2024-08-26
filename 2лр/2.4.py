import matplotlib.pyplot as plt
import matplotlib.patches as patches

n = 5  # встановлене значення n

# Побудова графіка
fig, ax = plt.subplots(figsize=(10, 6))

# Побудова першої трапеції
trap1 = patches.Polygon([(n, n),(4 * n, n),  (3.25 * n, 3 * n), (1.75 * n, 3 * n)],
                        closed=True, edgecolor='C10', linewidth=4, linestyle='-', joinstyle='round', facecolor='none')
ax.add_patch(trap1)

# Побудова другої трапеції
trap2 = patches.Polygon([(1.2 * n, 1.2 * n), ((1.2+2.6) * n, 1.2 * n), ((1.2+2.6*0.75) * n, (1.2+1.6) * n),
                         ((1.2+2.6*0.25) * n, (1.2+1.6) * n)], closed=True, edgecolor='C10', linewidth=4,
                        linestyle='-', joinstyle='round', facecolor='none')
ax.add_patch(trap2)

# Побудова третьої трапеції
trap3 = patches.Polygon([(1.5 * n, 1.5 * n), (3.5 * n, 1.5 * n), (3 * n, 2.5 * n), (2 * n, 2.5 * n)],
                        closed=True, edgecolor='C10', linewidth=4, linestyle='-', joinstyle='round', facecolor='none')
ax.add_patch(trap3)

# Додаткові налаштування графіка
ax.set_xlim(0, 4 * n)
ax.set_ylim(0, 4 * n)
ax.set_aspect('equal', 'box')  # Одиничне співвідношення масштабів осей

# Відображення графіка
plt.show()
