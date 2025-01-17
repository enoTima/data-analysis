import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
n = 5


#1) Побудувати таблицю даних, що п'ять серій спостережень умовної залежності концентрації певного реагенту від часу в
# хімічній реакції. Перший рядок таблиці повинен містити імена стовпчиків – серія, час, концентрація. Перший стовпчик
# має містити номери серій. Другий стовпчик має містити п'ять однакових послідовностей моментів спостережень, що
# відповідають різним серіям спостережень. Ці дані треба сформувати як послідовності від 0 до 12 + n довжиною по n + 13
# елементів. Третій стовпчик призначений для запису результатів спостережень, що відповідають вказаним у попередніх
# стовпчиках серії та моменту часу. Їх треба розрахувати як квадратні корені з суми елементів перших двох стовпчиків
# відповідного рядка. Для цієї таблиці побудувати:
#- графік, що зображує залежності концентрації від часу для кожної серії;
#- графік, що зображує залежність середньої концентрації від часу.
#Позначити на графіках назви координатних осей.
print('-'*20)
print('#1')

series_numbers = np.arange(1, 6)

# Створення таблиці даних
data = {'Серія': np.repeat(series_numbers, n + 13),
        'Час': np.tile(np.arange(0, 13 + n), len(series_numbers)),
        'Концентрація': np.nan}

df = pd.DataFrame(data)

# Розрахунок концентрації за заданою умовною формулою
df['Концентрація'] = np.sqrt(df['Серія'] + df['Час'])

# Виведення таблиці
print(df)

# Побудова графіків
plt.figure(figsize=(12, 6))

# Графік для кожної серії
for series in series_numbers:
    subset = df[df['Серія'] == series]
    plt.plot(subset['Час'], subset['Концентрація'], label=f'Серія {series}')

plt.title('Залежність концентрації від часу для кожної серії')
plt.xlabel('Час')
plt.ylabel('Концентрація')
plt.legend()
plt.show()

# Графік середньої концентрації
average_concentration = df.groupby('Час')['Концентрація'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(average_concentration['Час'], average_concentration['Концентрація'], color='red', marker='o')
plt.title('Середня концентрація від часу')
plt.xlabel('Час')
plt.ylabel('Середня концентрація')
plt.show()


#2. Для отриманої при виконанні попереднього завдання залежності середньої концентрації від часу побудувати в одному вікні основні типи графіків (крім графіка типу "n"). При цьому використати кольори з номерами від n до n + 4. Крім того:
#- для першого графіка задати діапазон значень за віссю абсцис від 5 до n + 10, а за віссю ординат – від 2 до 2n;
#- для другого графіка не вказувати підписи осей;
#- для третього графіка не вказувати підписи осей та не будувати координатні осі;
#- четвертий графік побудувати, використовуючи логарифмічну вісь абсцис;
#- п’ятий графік побудувати, використовуючи логарифмічну вісь ординат;
#- шостий графік побудувати у логарифмічній системі координат.

# Побудова графіків для другого завдання
plt.figure(figsize=(18, 12))

# Графік 1: тип "line", задані діапазони для вісей
plt.subplot(2, 3, 1)
plt.loglog(average_concentration['Час'], average_concentration['Концентрація'], color='C5', marker='o')
plt.title('Графік 1')
plt.xlim(5, n + 10)  # діапазон для вісі абсцис
plt.ylim(2, 2 * n)  # діапазон для вісі ординат

# Графік 2: без підписів осей
plt.subplot(2, 3, 2)
plt.semilogy(average_concentration['Час'], average_concentration['Концентрація'], color='C6', marker='o')
plt.title('Графік 2')

# Графік 3: без координатних осей
plt.subplot(2, 3, 3)
plt.plot(average_concentration['Час'], average_concentration['Концентрація'], color='C7', marker='o')
plt.title('Графік 3')
plt.axis('off')

# Графік 4: логарифмічна вісь абсцис
plt.subplot(2, 3, 4)
plt.semilogx(average_concentration['Час'], average_concentration['Концентрація'], color='C8', marker='o')
plt.title('Графік 4')

# Графік 5: логарифмічна вісь ординат
plt.subplot(2, 3, 5)
plt.loglog(average_concentration['Час'], average_concentration['Концентрація'], color='C9', marker='o')
plt.title('Графік 5')

# Графік 6: логарифмічна система координат
plt.subplot(2, 3, 6)
plt.plot(average_concentration['Час'], average_concentration['Концентрація'], color='C10', marker='o')
plt.title('Графік 6')
plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.show()

