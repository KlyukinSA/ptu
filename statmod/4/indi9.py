import random
import math

m = 4
eps = 0.005
P = 0.995
t_a = 2.576
N = int(t_a * t_a * P * (1 - P) / (eps * eps))
n = [4, 2, 3, 4]
lambda_ = [40e-6, 10e-6, 80e-6, 30e-6]

def main():
    T = 8760
    print(lambda_)
    # генерация различных комбинаций L
    for i in range(m+1):
        for j in range(m+1):
            for k in range(m+1):
                for l in range(5):
                    L = [i, j, k, l]
                    # вычисление ВБР
                    p_ = p(T, L)
                    if p_ > P:
                        print(L, "\tP =", p_, "\tN = ", sum(L))

def p(T, L):
    d = 0
    for nn in range(N):
        x = []
        for i in range(m): # классы
            t = []
            for j in range(n[i]): # элементы
                t.append(-math.log(random.random()) / lambda_[i])
            for j in range(L[i]): # запасные элементы
                l = t.index(min(t))
                t[l] -= math.log(random.random()) / lambda_[i]
            for j in range(n[i]):
                x.append(t[j])
        arr = [a for a in x]
        if not F(arr, T):
            d += 1
    return 1 - d / N

def F(t, T):
    return ((t[0] > T and t[1] > T or t[2] > T and t[3] > T) and t[4] > T and t[5] > T
            and (t[6] > T or t[7] > T or t[8] > T)
            and (t[9] > T or t[10] > T) and (t[11] > T or t[12] > T))

if __name__ == "__main__":
    main()
