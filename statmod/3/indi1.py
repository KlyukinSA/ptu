import numpy as np

def rayleigh_distribution():
    u1 = np.random.normal()
    u2 = np.random.normal()
    return np.sqrt(u1**2 + u2**2)

data = [rayleigh_distribution() for _ in range(100)]
print(data)

import matplotlib.pyplot as plt

plt.hist(data, bins=10, color='skyblue', edgecolor='black')  # Построение гистограммы
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Распределение случайных чисел')
plt.show()


from scipy.stats import rayleigh
from scipy.stats import kstest

# Вычислите параметры распределения Рэлея (в данном случае среднее и стандартное отклонение)
params = rayleigh.fit(data)

# Выполните тест Колмогорова-Смирнова
ks_statistic, p_value = kstest(data, 'rayleigh', args=params)

# Выведите результаты теста
print(f'Статистика Колмогорова-Смирнова: {ks_statistic}')
print(f'p-значение: {p_value}')

if p_value < 0.05:
    print('Отвергаем нулевую гипотезу - данные не соответствуют закону Рэлея')
else:
    print('Принимаем нулевую гипотезу - данные соответствуют закону Рэлея')
