import matplotlib.pyplot as plt
import numpy as np

# Визначення параметрів
n = 5  # встановлене значення n
num_elements = 100 - n

# Створення вектора x арифметичної прогресії
x = np.linspace(-(n + 1) / n, (n + 1) / n, num_elements)

# Створення функцій f(x)
y1 = x
y2 = x**2
y3 = x**(0.6 * n)

# Побудова графіків
plt.plot(x, y1, marker=5, color=f'C{n+10}', linewidth=3, linestyle='--', label=f'f(x) = x')
plt.plot(x, y2, marker=6, color=f'C{n+11}', linewidth=3, linestyle='-.', label=f'f(x) = x^2')
plt.plot(x, y3, marker=7, color=f'C{n+12}', linewidth=3, linestyle='-.', label=f'f(x) = x^(0.6n)')

# Додавання легенди
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Додаткові налаштування графіка
plt.title('Графіки функцій залежностей від x')
plt.xlabel('x')
plt.ylabel('f(x)')

# Показ графіка
plt.show()
