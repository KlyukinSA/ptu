import random, math, numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import ks_2samp

N = 50
a = 0
b = 2
M = 1
q = 4

def generate_norm1(N):
    array = []
    for i in range (N):
        temp = M + norm_1() * q
        array.append(temp)
    return array

def norm_1():
    u1 = random.random()
    u2 = random.random()
    return math.sqrt(-2 * math.log(u2)) * math.cos(2 * math.pi * u1)

def m(u):
    m = 0
    for number in u:
        m += number
    m /= len(u)
    return m

def d(u, m):
    d = 0
    for number in u:
        d += (number - m) * (number - m)
    d /= len(u) - 1
    return d

# генерируем выборки
sample_X = np.random.triangular(left=a, mode=1, right=b, size=N)
sample_Y = generate_norm1(N)

# вычисляем статистику критерия знаков
# z = N - sum(1 for i in range(N) if sample_X[i] > sample_Y[i]) - sum(1 for i in range(N) if sample_X[i] < sample_Y[i])
# z /= np.sqrt(N)
z = sum(1 for i in range(N) if sample_X[i] < sample_Y[i])


M_X = m(sample_X)
M_Y = m(sample_Y)
D_X = d(sample_X, M_X)
D_Y = d(sample_Y, M_Y)

t = (M_X - M_Y) * np.sqrt(N*(N - 1)) / np.sqrt((N-1)*D_X + (N-1)*D_Y)
# определяем критическое значение критерия знаков:
alpha = 0.05
z_crit = 32

# # выводим результаты теста

print(sample_X)
print(sample_Y)
print(z)
print(t)
# row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # plt.bar(row, F_X, 0.8)
# # plt.show()
# # plt.bar(row, F_Y, 0.8)
# # plt.show()

if np.abs(z) > z_crit:
    print("Гипотеза H0 отвергается на уровне значимости", alpha)
else:
    print("Гипотеза H0 не отвергается на уровне значимости", alpha)