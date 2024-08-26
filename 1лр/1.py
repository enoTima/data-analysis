import numpy as np
n=5

#1. За допомогою функції с() сформувати вектор, що містить:
# а) всі цілі числа від 15n до n у спадному порядку;
# б) вектор, елементами якого є літери Вашого прізвища.
print('-'*20)
print('#1')

def ca(n):
    return [*range(15*n, n, -1)]
print(ca(n))

def cb(str):
    return list(str)
print(cb('Погодаєв'))


#2. За допомогою функції seq() створити:
#а) вектор, що містить 40 - n чисел, що є елементами арифметичної прогресії з першим елементом 3n - 1 та останнім елементом n;
#б) вектор, що містить взяті з кроком 0,2 числа від 2n до 6n.
print('-'*20)
print('#2')

def seqa(n):
    return [3*n - 1 + i*(1 - 2*n)/(39 - n) for i in range(40-n)]
print(seqa(n))

def seqb(n):
    m = []
    value = 2*n
    while value <= 6*n:
        m.append(value)
        value = round(value+0.2, 1)
    return m
print(seqb(n))

#3. За допомогою функції matrix() сформувати;
#а) з елементів першого вектора попереднього завдання матрицю, що містить 4 рядки та 3 стовпчики;
#б) матрицю, що містить 4n рядків та 3 стовпчики з векторів, що є взятими у висхідному порядку послідовностями всіх цілих чисел від 1 до n + 7 та від n - 8 до 2n, відповідно.
print('-'*20)
print('#3')

def matrixa(n):
    m = []
    q = seqa(n)
    for i in range(4):
        m.append([])
        for j in range(3):
            m[i].append(q[i*4+j])
    return m

print(matrixa(n))


def matrixb(n):
    vector1 = np.arange(1, n + 9)
    vector2 = np.arange(n - 8, 2 * n + 1)
    matrix = np.zeros((4 * n, 3))
    combined_vector = np.concatenate((vector1, vector2))
    while True:
        for i in range(4 * n):
            for j in range(3):
                matrix[i][j] = combined_vector[(j*4*n+i)%len(combined_vector)]
        break
    return matrix

print(matrixb(n))


#4. Знайти:
#а) суму другого елемента першого стовпчика та першого елемента другого стовпчика отриманої в останньому завданні матриці;
#б) вектор, елементи якого є сумами відповідних елементів другого та третього стовпчиків цієї матриці.
print('-'*20)
print('#4')

matr = matrixb(n)
print(matr[1][0]+matr[0][1])
matrix4b = []
for i in range(4*n):
    matrix4b.append(matr[i][0] + matr[i][1] + matr[i][2])
print(matrix4b)

#5.
#а) Створити матрицю розмірності 5*4, елементами якої є цілі числа від n + 5 до n + 24;
#б) вивести елементи першого рядка цієї матриці;
#в) присвоїти цим елементам значення n + 3 та вивести результат перетворення;
#г) прирівняти до n/2 всі елементи, які є більшими, ніж 2n та вивести результат перетворення.
print('-'*20)
print('#5a')
matrix5a = np.arange(n + 5, n + 25).reshape(5, 4)
print(matrix5a)
print('#5b')
print(matrix5a[0])
print('#5c')
matrix5c = matrix5a
matrix5c[0, :] = n + 3
print(matrix5c)
print('#5d')
matrix5c[matrix5c > 2 * n] = n / 2
print(matrix5c)

#6. Побудувати масив у вигляді таких трьох матриць розмірності n*3:
#перша матриця містить послідовність цілих чисел від 1 до 3n, взятих у спадному порядку;
#друга матриця – послідовність цілих чисел від 3n + 1 до 6n;
#третя матриця – послідовність цілих чисел від n - 10 до 4n - 11;
print('-'*20)
print('#6')

vector = np.concatenate((np.arange(1, 3*n+1), np.arange(3*n+1, 6*n+1), np.arange(n-10, 4*n-10)))
print(vector)

#7. Побудувати транспоновану матрицю для матриці із завдання 5а. Зберегти отриманий масив у вигляді файлу
# формату *.csv, зчитати його в R та визначити суму і добуток всіх елементів отриманої матриці.
print('-'*20)
print('#7')

matrix7 = np.transpose(matrix5a)
file_path = "output_matrix.csv"
# Збереження матриці у файл
np.savetxt(file_path, matrix7, delimiter=",")
# Зчитуємо матрицю з файлу
read_matrix = np.loadtxt(file_path, delimiter=",")
# Визначаємо суму та добуток
sum_of_elements = np.sum(read_matrix)
product_of_elements = np.prod(read_matrix)
print("Сума всіх елементів:", sum_of_elements)
print("Добуток всіх елементів:", product_of_elements)

#8. Створити список, що містить такі компоненти:
#v1 – вектор назв видів промислової продукції (взяти назви видів з n + 5-го до n + 8 –го із таблиці за посиланням (при визначенні номерів враховувати тільки рядки з даними):
#http://ukrstat.gov.ua/operativ/operativ2006/pr/prm_ric/xls/vov20XX_u.xls;
#v2 – вектор одиниць вимірювання обсягів виробництва для тих самих видів продукції (одиниці, що повторюються, дублювати не треба);
#v3 – обсяги виробництва для відповідних видів продукції у 2018 р.
#Вивести отриманий список на консоль та визначити його структуру
print('-'*20)
print('#8')

import xlrd

n = 5
start_row = n + 5 + 4
end_row = n + 9 + 4
file_name = 'vov20XX_u.xls'
# Відкриваємо файл та зчитуємо дані
try:
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)

    # Ініціалізація векторів
    v1 = []
    v2 = []
    v3 = []

    # Зчитуємо назви, одиниці вимірювання та обсяги виробництва
    for row in range(start_row, end_row + 1):
        industrial_product = sheet.cell_value(row, 0)
        unit_of_measurement = sheet.cell_value(row, 2)
        production_volume_2018 = sheet.cell_value(row, 10)

        # Додаємо дані до відповідних векторів
        v1.append(industrial_product)
        v2.append(unit_of_measurement)
        v3.append(production_volume_2018)

except Exception as e:
    print(f"Помилка при читанні файлу: {e}")

# Виведення результату
print("v1 (Назви видів промислової продукції):", v1)
print("v2 (Одиниці вимірювання обсягів виробництва):", v2)
print("v3 (Обсяги виробництва у 2018 р.):", v3)


#9. Зберегти дані зазначеної у попередньому завданні таблиці у форматі *.csv зчитати п’ять рядків таблиці
# даних, починаючи з n-го. Для обраних видів продукції визначити:
#обсяг виробництва у 2018 р. у відсотках до відповідного показника 2011 р.;
#абсолютний приріст обсягу виробництва у 2018 р. по відношенню до відповідного показника 2011 р.
print('-'*20)
print('#9')

import csv
import pandas as pd

n = 4
start_row = n
end_row = n + 10

# Ім'я файлу
input_file_name = 'vov20XX_u.xls'
output_csv_file_name = 'output_data.csv'

# Зчитуємо дані з Excel і зберігаємо їх у файл CSV
try:
    workbook = xlrd.open_workbook(input_file_name)
    sheet = workbook.sheet_by_index(0)

    data = []
    for row in range(start_row, end_row + 1):
        data.append(sheet.row_values(row))

    # Збереження у файл CSV
    with open(output_csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
except Exception as e:
    print(f"Помилка при читанні файлу Excel: {e}")


# Читаємо п'ять рядків таблиці з CSV, починаючи з n-го
df = pd.read_csv('output_data.csv', skiprows=5, nrows=5, header=None)

# Виведення перших п'яти рядків
print("Перші п'ять рядків:")
print(df)

# Додаємо індекс до DataFrame
df.reset_index(inplace=True)

# Конвертація стовпців до числового формату (всі невірні значення замінюються на NaN)
df.iloc[:, 4] = pd.to_numeric(df.iloc[:, 4], errors='coerce')
df.iloc[:, 10] = pd.to_numeric(df.iloc[:, 10], errors='coerce')

# Обробка NaN значень та обчислення відсотків та абсолютного приросту
df['Відсоток 2018 від 2011'] = (
    (df.iloc[:, 10] - df.iloc[:, 4]) / df.iloc[:, 4] * 100
)

df['Абсолютний приріст'] = (
    df.iloc[:, 10] - df.iloc[:, 4]
)

# Виведення результатів
print("\nРезультати:")
print(df[['index', 4, 10, 'Відсоток 2018 від 2011', 'Абсолютний приріст']])


#10. Створити вектори: b1, який містить n + 50 випадкових чисел, що підпорядковуються нормальному розподілу
# із середнім значенням 2n та стандартним відхиленням 0,5n; b2, який містить 60 - n випадкових чисел, що
# підпорядковуються рівномірному розподілу на відрізку від n до 3n. Написати цикл, що створює вектор b3 за таким
# правилом: якщо b1i < b2i , то b3i = 2, у протилежному випадку b3i = 0.
print('-'*20)
print('#10')

n = 5

# Створюємо вектор b1 за нормальним розподілом
b1 = np.random.normal(2 * n, 0.5 * n, n + 50)

# Створюємо вектор b2 за рівномірним розподілом
b2 = np.random.uniform(n, 3 * n, 60 - n)

# Ініціалізуємо вектор b3
b3 = np.zeros_like(b1)

# Створюємо вектор b3 за вказаним правилом
for i in range(len(b1)):
    if b1[i] < b2[i]:
        b3[i] = 2

# Виведення результатів
print("b1:", b1)
print("b2:", b2)
print("b3:", b3)


#11. Написати функцію, яка визначає відстань від точки A з координатами (2n, -n) до середини відрізку BC, який задано точками B (2n, n/2)) та C (1 - n, n + 2).
print('-'*20)
print('#11')

def distance_from_A_to_midpoint(n):
    # Координати точок A, B, C
    A = np.array([2 * n, -n])
    B = np.array([2 * n, n / 2])
    C = np.array([1 - n, n + 2])

    # Знаходимо координати середини відрізку BC
    midpoint_BC = (B + C) / 2

    # Обчислюємо відстань між A і серединою BC
    distance = np.linalg.norm(A - midpoint_BC)

    return distance

result = distance_from_A_to_midpoint(n)
print(f"Відстань від точки A до середини відрізку BC: {result}")