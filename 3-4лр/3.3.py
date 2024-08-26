import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з Excel-файлу
df = pd.read_excel('КНТ-811.xlsx')


df_fi = df[df['Country Code'] == 'FI']

df_filtered = df_fi[(df_fi['Reference year'] == 2020)]

df_sorted = df_filtered.sort_values(by='Total students enrolled ISCED 5-7', ascending=False)

top_5 = df_sorted.head(5)

# Сумуємо дані для решти закладів і створюємо рядок "інші"
other_data = pd.Series({'English Institution Name': 'other', 'Total students enrolled ISCED 5-7': df_sorted.iloc[5:]['Total students enrolled ISCED 5-7'].sum()})

plot_data = pd.concat([top_5, pd.DataFrame([other_data])])

plt.figure(figsize=(8, 8))
plt.pie(plot_data['Total students enrolled ISCED 5-7'], labels=plot_data['English Institution Name'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Розподіл студентів за закладами (рік 2020, рівень ISCED 5-7)')
plt.show()