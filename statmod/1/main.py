import random
import math
import matplotlib.pyplot as plt 

SIZE = 10
INTERVAL = 10
if __name__ == '__main__':
    col_correlation = [0] * SIZE
    row_number = [0] * SIZE
    randList = [0] * SIZE
    for i in range(SIZE):
        randList[i] = random.uniform(0, 1)
        # print(str(randList[i]) + "\n")
 # writer = writer(res)
    sum_of_rand = sum(randList)
    expectation = sum_of_rand / SIZE
    print("Мат. ожидание: " + str(expectation) + "\n")
    print("Отклонение мат. ожидания: " + str(abs(0.5 - expectation)) + "\n")
    dispersion = 0
    for current in randList:
        dispersion += (current - expectation) ** 2
    dispersion /= SIZE # дисперсия
    print("Дисперсия: " + str(dispersion) + "\n")
    std_deviation = math.sqrt(dispersion) # среднеквад. отклонение
    print("Отклонение дисперсии: " + str(abs(0.08333 - dispersion)) + "\n")
    print("Среднеквад. отклонение: " + str(std_deviation) + "\n")
    autocorrelation = [0] * SIZE # автокорреляция
    denom = 0 # знаменатель автокорелляции
    for i in range(SIZE):
        denom += (randList[i] - expectation) ** 2
    print("Знаменатель Автокорелляции: " + str(denom) + "\n")
    for i in range(SIZE):
        numer = 0
        for j in range(SIZE - i):
            numer += (randList[j] - expectation) * (randList[j + i] -
expectation)
        autocorrelation[i] = numer / denom
        col_correlation[i] = autocorrelation[i]
        row_number[i] = i 
    plt.bar(row_number, col_correlation, 1, 0)
    

    plt.show()
    # for r in autocorrelation:
        # print(str(r) + "\n")
        
 # вторая часть
    col_raspr = [0] * SIZE
    row_raspr = [0] * SIZE
    step = 1.0 / INTERVAL
    density = [0] * INTERVAL
    for i in range(SIZE):
        current = randList[i] / step
        density[int(current)] += 1
    for i in range(INTERVAL):
        density[i] /= SIZE
        col_raspr[i] = density[i]
        row_raspr[i] = i
    plt.bar(row_raspr, col_raspr)
    plt.show()
 # Третья часть
    col_raspr2 = [0] * SIZE
    row_raspr2 = [0] * SIZE
    steps = [0] * (SIZE + 1)
    for i in range(INTERVAL):
        suma = 0
        for j in range(i + 1):
            suma += density[j]
        steps[i+1] = suma
        col_raspr2[i] = steps[i+1]
        row_raspr2[i]= i
    # for i in steps:
    #     print(str(i) + "\n")
    plt.bar(row_raspr2, col_raspr2)
    plt.show()
