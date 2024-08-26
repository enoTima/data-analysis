import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з Excel-файлу
df = pd.read_excel('КНТ-811.xlsx')

# Відфільтровуємо дані для країни FI (5 варіант)
df_fi = df[df['Country Code'] == 'FI']

# Групуєємо дані за роками та інститутами, обчислюємо суму студентів
df_grouped = df_fi.groupby(['Reference year', 'English Institution Name']).agg({'Total students enrolled ISCED 5-7': 'sum'}).reset_index()

# Перетворюємо таблицю для отримання кінцевого формату
df_pivot = df_grouped.pivot(index='English Institution Name', columns='Reference year', values='Total students enrolled ISCED 5-7').fillna(0)

# Зберігаємо таблицю у файл CSV
df_pivot.to_csv('output.csv', sep=',')

odd_years_data = df_pivot[df_pivot.columns[df_pivot.columns % 2 != 0]]
ax = odd_years_data.plot(kind='bar', colormap='Paired', stacked=True, rot=0, figsize=(12, 6))
ax.set_ylabel('Number of Students')
ax.set_xlabel('Institution')
ax.set_title('Number of Students in Higher Education Institutions (Odd Years) - {}'.format('FI'))
ax.legend(title='Year')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('odd_years_plot.png')

plt.show()

even_years_data = df_pivot[df_pivot.columns[df_pivot.columns % 2 == 0]]
ax = even_years_data.plot(kind='bar', colormap='Paired', stacked=True, rot=0, figsize=(12, 6))
ax.set_ylabel('Number of Students')
ax.set_xlabel('Institution')
ax.set_title('Number of Students in Higher Education Institutions (Even Years) - {}'.format('FI'))
ax.legend(title='Year')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.savefig('even_years_plot.png')

# Show the plot
plt.show()
