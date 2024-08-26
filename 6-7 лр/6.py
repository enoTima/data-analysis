import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats

df = pd.read_csv('output.csv')
vector_i = df['2018'].values
vector_j = df['2019'].values
vector_k = df['2020'].values

correlation_matrix = df[['2018', '2019', '2020']].corr()

# Побудова теплокарти кореляційної матриці
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix')
plt.show()

cor_coef_I_J = np.corrcoef(vector_i, vector_j)[0, 1]
cor_coef_K_J = np.corrcoef(vector_k, vector_j)[0, 1]
cor_coef_I_K = np.corrcoef(vector_i, vector_k)[0, 1]

print(f"\nКоефіцієнт кореляції Пірсона між I J: {cor_coef_I_J}")
print(f"Коефіцієнт кореляції Пірсона між K J: {cor_coef_K_J}")
print(f"Коефіцієнт кореляції Пірсона між I K: {cor_coef_I_K}")

# Розрахунок коефіцієнта рангової кореляції Спірмена
cor_coef_spearman_I_J, _ = scipy.stats.spearmanr(vector_i, vector_j)
cor_coef_spearman_I_K, _ = scipy.stats.spearmanr(vector_i, vector_k)
cor_coef_spearman_K_J, _ = scipy.stats.spearmanr(vector_k, vector_j)

print(f"\nКоефіцієнт рангової кореляції Спірмена між I J: {cor_coef_spearman_I_J}")
print(f"Коефіцієнт рангової кореляції Спірмена між I K: {cor_coef_spearman_I_K}")
print(f"Коефіцієнт рангової кореляції Спірмена між K J: {cor_coef_spearman_K_J}")

cor_coef_kendall_I_J, _ = scipy.stats.kendalltau(vector_i, vector_j)
cor_coef_kendall_I_K, _ = scipy.stats.kendalltau(vector_i, vector_k)
cor_coef_kendall_K_J, _ = scipy.stats.kendalltau(vector_k, vector_j)

print(f"\nКоефіцієнт рангової кореляції Кендала між I J: {cor_coef_kendall_I_J}")
print(f"Коефіцієнт рангової кореляції Кендала між I K: {cor_coef_kendall_I_K}")
print(f"Коефіцієнт рангової кореляції Кендала між K J: {cor_coef_kendall_K_J}")


# Функція для розрахунку R-squared

def calculate_r_squared(x, y):
    mean_x = np.mean(x)

    ss_x = np.sum((x - mean_x) ** 2)
    ss_residual = np.sum((x - y) ** 2)

    r_squared = 1 - (ss_residual / ss_x)

    return r_squared


# Розрахунок R-squared для всіх трьох пар
r_squared_i_j = calculate_r_squared(vector_i, vector_j)
r_squared_i_k = calculate_r_squared(vector_i, vector_k)
r_squared_j_k = calculate_r_squared(vector_j, vector_k)

print(f"\nКоефіцієнт детермінації (R-squared) між i та j: {r_squared_i_j}")
print(f"Коефіцієнт детермінації (R-squared) між i та k: {r_squared_i_k}")
print(f"Коефіцієнт детермінації (R-squared) між j та k: {r_squared_j_k}")
