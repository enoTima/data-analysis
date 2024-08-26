import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot
import scipy


# Зчитуємо файл output.csv
data = pd.read_csv('output.csv')
# Отримаємо вектор(список) для нашого варіанту де дані це English Institution Name,2011,2012,...,2020
data = data.values.tolist()


                                                            # №1
# Отримаймо роки та дані для парних років
years = [2012, 2014, 2016, 2018, 2020]
data_pairs = [row[1::2] for row in data]

# Ініціалізуймо графік
plt.figure(figsize=(10, 6))

# Побудуймо емпіричні функції розподілу для парних років
for i in range(0, len(data_pairs[0])):
    year = years[i]
    values = [row[i] for row in data_pairs]

    # Створемо емпіричну функцію розподілу за допомогою numpy
    x = np.sort(values)
    y = np.arange(1, len(x) + 1) / len(x)

    # Побудуймо графік для кожного парного року
    plt.plot(x, y, label=f'Empirical CDF {year}')

# Налаштуймо графік
plt.title('Empirical Cumulative Distribution Functions for Paired Years')
plt.xlabel('Values')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)

plt.show()

                                                            # №2
# Отримаймо дані для всіх років
data_all_years = [row[1:] for row in data]
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Переробимо data_all_years
transformed_data = list(map(list, zip(*data_all_years)))
transformed_data = [
    [value for value in row if value != 0] for row in transformed_data
]

# Ініціалізуймо графік
plt.figure(figsize=(10, 6))

# Побудуймо діаграму "ящик з вусами" для всіх років
plt.boxplot(transformed_data, labels=[str(year) for year in years])

# Налаштуймо графік
plt.title('Boxplot for All Years')
plt.xlabel('Years')
plt.ylabel('Values')

plt.show()

                                                            # № 4
# Розрахуймо квартилі для всіх років
quartiles = np.percentile(data_all_years, [25, 50, 75], axis=0)

# Виведемо результати
for i, year in enumerate(range(2011, 2021)):
    print(f"\nQuartiles for {year}:")
    print(f"Q1: {quartiles[0, i]}")
    print(f"Q2 (Median): {quartiles[1, i]}")
    print(f"Q3: {quartiles[2, i]}")


                                                            # № 5
data_2020 = np.array(list(filter(lambda x: x != 0, [row[10] for row in data[1:]])))
data_2016 = np.array(list(filter(lambda x: x != 0, [row[6] for row in data[1:]])))
data_2015 = np.array(list(filter(lambda x: x != 0, [row[5] for row in data[1:]])))
data_2011 = np.array(list(filter(lambda x: x != 0, [row[1] for row in data[1:]])))

# Побудуймо Q-Q діаграми
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, data, year in zip(axes, [data_2020, data_2016, data_2015, data_2011], [2020, 2016, 2015, 2011]):
    _, (_, _, r) = probplot(data, plot=ax, fit=True, dist='norm')
    ax.set_title(f'Q-Q Plot for {year} (R-squared: {r**2:.4f})')

plt.tight_layout()
plt.show()



print('\n'*5)
                                                            # № 6

# не знайшов функції для Ліллієфорса тому використав Колмагорова-Смірнова

# Перевірка відповідності нормальному розподілу за критерієм Шапіро-Уїлка
stat_shapiro, p_shapiro = scipy.stats.shapiro(data_2020)
print(f'Shapiro-Wilk Test for 2020: Statistic={stat_shapiro:.4f}, p-value={p_shapiro:.4f}')
if p_shapiro > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')


# Перевірка відповідності нормальному розподілу за критерієм Андерсона-Дарлінга
result_anderson = scipy.stats.anderson(data_2020)
print(f'Anderson-Darling Test for 2020: Statistic={result_anderson.statistic:.4f}, Critical Value={result_anderson.critical_values[2]}, Significance Level={result_anderson.significance_level[2]}')
if result_anderson.statistic > result_anderson.critical_values[2]:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')


# Перевірка відповідності нормальному розподілу за критерієм Ліллієфорса
stat_kstest, p_kstest = scipy.stats.kstest(data_2020, 'norm')
print(f'Kolmogorov-Smirnov Test for 2020: Statistic={stat_kstest:.4f}, p-value={p_kstest:.4f}')
if p_kstest > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

print('\n'*2)

# Перевірка відповідності нормальному розподілу за критерієм Шапіро-Уїлка
stat_shapiro, p_shapiro = scipy.stats.shapiro(data_2016)
print(f'Shapiro-Wilk Test for 2016: Statistic={stat_shapiro:.4f}, p-value={p_shapiro:.4f}')
if p_shapiro > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Андерсона-Дарлінга
result_anderson = scipy.stats.anderson(data_2016)
print(
    f'Anderson-Darling Test for 2016: Statistic={result_anderson.statistic:.4f}, Critical Value={result_anderson.critical_values[2]}, Significance Level={result_anderson.significance_level[2]}')
if result_anderson.statistic > result_anderson.critical_values[2]:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Ліллієфорса
stat_kstest, p_kstest = scipy.stats.kstest(data_2016, 'norm')
print(f'Kolmogorov-Smirnov Test for 2016: Statistic={stat_kstest:.4f}, p-value={p_kstest:.4f}')
if p_kstest > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

print('\n' * 2)

# Перевірка відповідності нормальному розподілу за критерієм Шапіро-Уїлка
stat_shapiro, p_shapiro = scipy.stats.shapiro(data_2015)
print(f'Shapiro-Wilk Test for 2015: Statistic={stat_shapiro:.4f}, p-value={p_shapiro:.4f}')
if p_shapiro > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Андерсона-Дарлінга
result_anderson = scipy.stats.anderson(data_2015)
print(
    f'Anderson-Darling Test for 2015: Statistic={result_anderson.statistic:.4f}, Critical Value={result_anderson.critical_values[2]}, Significance Level={result_anderson.significance_level[2]}')
if result_anderson.statistic > result_anderson.critical_values[2]:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Ліллієфорса
stat_kstest, p_kstest = scipy.stats.kstest(data_2015, 'norm')
print(f'Kolmogorov-Smirnov Test for 2015: Statistic={stat_kstest:.4f}, p-value={p_kstest:.4f}')
if p_kstest > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

print('\n' * 2)

# Перевірка відповідності нормальному розподілу за критерієм Шапіро-Уїлка
stat_shapiro, p_shapiro = scipy.stats.shapiro(data_2011)
print(f'Shapiro-Wilk Test for 2011: Statistic={stat_shapiro:.4f}, p-value={p_shapiro:.4f}')
if p_shapiro > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Андерсона-Дарлінга
result_anderson = scipy.stats.anderson(data_2011)
print(
    f'Anderson-Darling Test for 2011: Statistic={result_anderson.statistic:.4f}, Critical Value={result_anderson.critical_values[2]}, Significance Level={result_anderson.significance_level[2]}')
if result_anderson.statistic > result_anderson.critical_values[2]:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')

# Перевірка відповідності нормальному розподілу за критерієм Ліллієфорса
stat_kstest, p_kstest = scipy.stats.kstest(data_2011, 'norm')
print(f'Kolmogorov-Smirnov Test for 2011: Statistic={stat_kstest:.4f}, p-value={p_kstest:.4f}')
if p_kstest > 0.05:
    print('можна припустити що дані розподілено нормально з рівнем значимості 0.05')
else:
    print('не можна припустити що дані розподілено нормально з рівнем значимості 0.05')

print('\n' * 2)

                                                            # № 7
from scipy.stats import ttest_ind, f_oneway, ks_2samp, mannwhitneyu, ansari, shapiro


# Перевірка нормальності за критерієм Шапіро-Уїлка (необхідно вже перевірити перед використанням критеріїв Уелча та Фішера)
_, p_shapiro_2020 = shapiro(data_2020)
_, p_shapiro_2015 = shapiro(data_2015)
_, p_shapiro_2016 = shapiro(data_2016)
_, p_shapiro_2011 = shapiro(data_2011)

# Визначення однорідності за критеріями Уелча та Фішера (якщо всі вибірки нормальні)
if all(p > 0.05 for p in [p_shapiro_2020, p_shapiro_2015, p_shapiro_2016, p_shapiro_2011]):
    # Перевірка за критерієм Уелча
    stat_welch, p_welch = ttest_ind(data_2020, data_2015, equal_var=False)
    print(f'Welch Test for 2020 and 2015: Statistic={stat_welch:.4f}, p-value={p_welch:.4f}')
    if p_welch > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    # Перевірка за критерієм Уелча
    stat_welch, p_welch = ttest_ind(data_2016, data_2011, equal_var=False)
    print(f'Welch Test for 2016 and 2011: Statistic={stat_welch:.4f}, p-value={p_welch:.4f}')
    if p_welch > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    # Перевірка за критерієм Фішера
    stat_f, p_f = f_oneway(data_2020, data_2015, data_2016, data_2011)
    print(f'Fisher Test for all pairs: Statistic={stat_f:.4f}, p-value={p_f:.4f}')
    if p_f > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

else:
    print('Не всі вибірки мають нормальний розподіл.')

    # Перевірка однорідності за критеріями Колмогорова-Смірнова, Уілкоксона та Ансарі-Бредлі
    stat_ks, p_ks = ks_2samp(data_2020, data_2015)
    print(f'Kolmogorov-Smirnov Test for 2020 and 2015: Statistic={stat_ks:.4f}, p-value={p_ks:.4f}')
    if p_ks > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    stat_mw, p_mw = mannwhitneyu(data_2020, data_2015, alternative='two-sided')
    print(f'Mann-Whitney U Test for 2020 and 2015: Statistic={stat_mw:.4f}, p-value={p_mw:.4f}')
    if p_mw > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    stat_ansari, p_ansari = ansari(data_2020, data_2015)
    print(f'Ansari-Bradley Test for 2020 and 2015: Statistic={stat_ansari:.4f}, p-value={p_ansari:.4f}')
    if p_ansari > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    # Перевірка однорідності за критеріями Колмогорова-Смірнова, Уілкоксона та Ансарі-Бредлі
    stat_ks, p_ks = ks_2samp(data_2016, data_2011)
    print(f'Kolmogorov-Smirnov Test for 2016 and 2011: Statistic={stat_ks:.4f}, p-value={p_ks:.4f}')
    if p_ks > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    stat_mw, p_mw = mannwhitneyu(data_2016, data_2011, alternative='two-sided')
    print(f'Mann-Whitney U Test for 2016 and 2011: Statistic={stat_mw:.4f}, p-value={p_mw:.4f}')
    if p_mw > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')

    stat_ansari, p_ansari = ansari(data_2016, data_2011)
    print(f'Ansari-Bradley Test for 2016 and 2011: Statistic={stat_ansari:.4f}, p-value={p_ansari:.4f}')
    if p_ansari > 0.05:
        print('Можна припустити однорідність.')
    else:
        print('Не можна припустити однорідність.')