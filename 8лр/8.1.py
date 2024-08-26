import numpy as np
import matplotlib.pyplot as plt

n = 5
t = np.arange(0, 100 * n + 1, 1)
u = 100 + (5 * t * n) / (n + 2)
s = 50 * np.sin(5 + 2 * np.pi * t / (30 + 10 * n))
e = np.random.normal(loc=30 * n, scale=10 * n, size=len(t))
y = u + s + e

# Візуалізація ряду
plt.plot(t, y, label='t-y ряд')
plt.xlabel('Час (t)')
plt.ylabel('Значення')
plt.title('Графік ряду t-y')
plt.legend()
plt.show()

print(f'Хронологічне середнє: {np.mean(y)}')

chain_growth = np.abs(np.diff(y))
base_growth = np.abs(y - y[0])

mean_chain_growth = np.mean(chain_growth)
mean_base_growth = np.mean(base_growth)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(chain_growth)
plt.title('Графік ланцюгових приростів')

plt.subplot(2, 1, 2)
plt.plot(base_growth)
plt.title('Графік базисних приростів (відносно початкового рівня)')

plt.tight_layout()
plt.show()

print(f"Середнє ланцюгових приростів: {mean_chain_growth}")
print(f"Середнє базисних приростів: {mean_base_growth}")


chain_growth_rates = np.insert(y[1:] / y[:-1] * 100, 0, 100)
base_growth_rates = y / y[0] * 100

mean_chain_growth_rates = np.mean(chain_growth_rates)
mean_base_growth_rates = np.mean(base_growth_rates)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(chain_growth_rates)
plt.title('Графік ланцюгових Темпів зростань')

plt.subplot(2, 1, 2)
plt.plot(base_growth_rates)
plt.title('Графік базисних Темпів зростань (відносно початкового рівня)')

plt.tight_layout()
plt.show()

print(f"Середнє ланцюгових Темпів зростань: {mean_chain_growth_rates}")
print(f"Середнє базисних Темпів зростань: {mean_base_growth_rates}")


chain_increase_rates = np.insert(np.abs(np.diff(y)) / y[:-1] * 100, 0, 100)
base_increase_rates = np.abs(y - y[0]) / y[0] * 100

mean_chain_increase_rates = np.mean(chain_increase_rates)
mean_base_increase_rates = np.mean(base_increase_rates)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(chain_increase_rates)
plt.title('Графік ланцюгових Темпів приросту')

plt.subplot(2, 1, 2)
plt.plot(base_increase_rates)
plt.title('Графік базисних Темпів приросту (відносно початкового рівня)')

plt.tight_layout()
plt.show()

print(f"Середнє ланцюгових Темпів приросту: {mean_chain_increase_rates}")
print(f"Середнє базисних Темпів приросту: {mean_base_increase_rates}")


acceleration = np.gradient(np.gradient(y, t), t)

plt.plot(t, acceleration, label='Коефіцієнт прискорення')
plt.xlabel('Час')
plt.ylabel('Коефіцієнт прискорення')
plt.title('Графік коефіцієнта прискорення')
plt.legend()
plt.show()

mean_acceleration = np.mean(acceleration)
print(f"Середній коеф прискорення: {mean_acceleration}")


increasing_series = np.where(np.diff(y) > 0, 1, 0)
decreasing_series = np.where(np.diff(y) < 0, 1, 0)

count_increasing_series = np.sum(increasing_series)
count_decreasing_series = np.sum(decreasing_series)

print(f"Кількість висхідних серій: {count_increasing_series}")
print(f"Кількість низхідних серій: {count_decreasing_series}")

if count_increasing_series > count_decreasing_series:
    print("Є висхідний тренд.")
elif count_increasing_series < count_decreasing_series:
    print("Є низхідний тренд.")
else:
    print("Немає вираженого тренду.")
