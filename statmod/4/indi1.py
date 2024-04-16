import random
import math

m = 3
eps = 0.005
P = 0.99
t_a = 2.326
N = int(t_a * t_a * P * (1 - P) / (eps * eps))
print(N)
n = [2, 3, 3]
lambda_ = [40e-6, 10e-6, 80e-6]

def main():
    T = 8760
    # генерация различных комбинаций L
    for i in range(m+1):
        for j in range(m+1):
            for k in range(m+1):
                L = [i, j, k]
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
    return (t[0] > T or t[1] > T) and t[2] > T and t[3] > T and t[4] > T and (t[5] > T or t[6] > T or t[7] > T)

if __name__ == "__main__":
    main()
