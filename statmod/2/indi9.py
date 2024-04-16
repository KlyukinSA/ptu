from scipy.stats import chi2
import math, random

def binomial(N, p):
    if N >= 100:
        return round(normal_binomial(N, p) + 0.5)
    M = random.random()
    r = 0
    P = pow(1 - p, N)
    M -= P
    while M >= 0:
        P *= ((N - r) / (r + 1)) * (p / (1 - p))
        M -= P
        r += 1
    return r

def generate_bin(N, n, p):
    array = [binomial(n, p) for i in range(N)]
    return array

def normal_binomial(N, p):
    m = N * p # матожидание
    s = N * p * (1 - p) ** 0.5 # ско
    x = random.gauss(0, 1) # стандартное нормальное распределение
    return m + x * s

def interval_test(e, m, a, b):
    print(e)

    # Вычисляем длину интервала
    interval_length = b - a + 1
    
    # Разбиваем область значений на интервалы
    num_intervals = math.ceil((2 ** m) / interval_length)
    intervals = [a + i * interval_length for i in range(num_intervals)]
    print(intervals)
    # Считаем количество попаданий значений в заданный интервал
    total = 0
    counts = [0] * m
    for i in range(len(e)):
        if (intervals[0] <= e[i] <= intervals[0] + interval_length - 1):
            for j in range (i,len(e)):
                if(intervals[0] <= e[j] <= intervals[0] + interval_length - 1):
                    if (j - i <= m):
                        if (j == 0):
                            counts[0] += 1
                        elif (j != i):
                            counts[j-i-1] += 1
                        else:
                            continue
                        total += 1
    print(counts)                                                
    # Ожидаемое количество попаданий в каждый интервал для равномерного распределения
    expected_counts = (b - a) / 2**m
    
    # Считаем статистику теста - сумму квадратов отклонений от ожидаемого количества попаданий
    statistic = 0
    for i in range (m):
        temp = total * expected_counts * (1 - expected_counts) ** i
        statistic += (counts[i] - temp) ** 2 / temp

    # Вычисляем критическое значение для заданного уровня значимости
    alpha = 0.05
    degrees_of_freedom = num_intervals - 1
    critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    
    # Сравниваем статистику теста с критическим значением
    if statistic < critical_value:
        print('хи2 = ', statistic, 'хи2_крит = ', critical_value, "\nПоследовательность прошла тест на случайность")
    else:
        print('хи2 = ', statistic, 'хи2_крит = ', critical_value, "\nПоследовательность не прошла тест на случайность")

# Задаем параметры теста
N = 50
e = generate_bin(50, 10, 0.5)
m = 3
a = 0
b = 2

# Проверяем последовательность на случайность с помощью теста на интервалы
interval_test(e, m, a, b)