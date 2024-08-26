from scipy.stats import norm

# Заданные параметры
mu = 0        # математическое ожидание
sigma = 1     # стандартное отклонение
k = 0.5       # отклонение от математического ожидания

# Вычисление вероятности
probability = norm.cdf(k, loc=mu, scale=sigma) - norm.cdf(-k, loc=mu, scale=sigma)

print("Вероятность отклонения не более чем на 0.5: {:.4f}".format(probability))
