import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Зчитуємо файл output.csv
data = pd.read_csv('output.csv')
data = data.values.tolist()
print(data)
for uni in data:
    uni[1:] = [sum(uni[1:])]

second_elements = [sublist[1] for sublist in data]

#довжину, мінімальне та максимальне значення;
print("Довжина списку:", len(second_elements))
print("Мінімальне значення серед других елементів:", min(second_elements))
print("Максимальне значення серед других елементів:", max(second_elements))

#квантилі порядку 0.15, 0.3, 0.7, 0.9;
print("Квантиль 0.15:", np.percentile(second_elements, 15))
print("Квантиль 0.30:", np.percentile(second_elements, 30))
print("Квантиль 0.70:", np.percentile(second_elements, 70))
print("Квантиль 0.90:", np.percentile(second_elements, 90))

#середні арифметичне, геометричне, гармонічне, квадратичне;
print("Середнє арифметичне:", sum(second_elements) / len(second_elements))
n = 1 / len(second_elements)
pr_res = 1
for i in second_elements:
    pr_res *= i ** n
print("Середнє геометричне:", pr_res)
print("Середнє гармонічне:", len(second_elements) / np.sum(1.0 / np.array(second_elements)))
print("Середнє квадратичне:", np.sqrt(np.mean(np.square(second_elements))))


print("Середнє медіана :", np.median(second_elements))
print("середній розмах :", (min(second_elements) + max(second_elements)) / 2)


print("дисперсія :", np.var(second_elements))
print("Стандартне відхилення:", np.std(second_elements))
print("Середнє відхилення:", np.mean(np.abs(second_elements - np.mean(second_elements))))
q75, q25 = np.percentile(second_elements, [75, 25])
interquartile_range = q75 - q25
print("Інтерквартильна відстань:", interquartile_range)


# Коефіцієнт ексцесу
mean = np.mean(second_elements)
std_deviation = np.std(second_elements)
excess_kurtosis = np.mean((second_elements - mean)**4) / std_deviation**4 - 3
print("Коефіцієнт ексцесу:", excess_kurtosis)
# Коефіцієнт асиметрії
mean = np.mean(second_elements)
std_deviation = np.std(second_elements)
skewness = np.mean((second_elements - mean)**3) / std_deviation**3
print("Коефіцієнт асиметрії:", skewness)


coefficient_of_variation = (std_deviation / mean) * 100
print("Коефіцієнт варіації:", coefficient_of_variation)


plt.hist(second_elements, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гістограма відносних частот')
plt.xlabel('Значення')
plt.ylabel('Відносні частоти')
plt.show()

# Графік емпіричної функції розподілу
sns.ecdfplot(data=second_elements)
plt.title('Емпірична функція розподілу')
plt.xlabel('Значення')
plt.ylabel('Ймовірність')
plt.show()

# Графік щільності розподілу
sns.kdeplot(second_elements, fill=True)
plt.title('Графік щільності розподілу')
plt.xlabel('Значення')
plt.ylabel('Щільність')
plt.show()

# Діаграма "ящик з вусами"
sns.boxplot(x=second_elements)
plt.title('Діаграма "ящик з вусами"')
plt.xlabel('Значення')
plt.show()