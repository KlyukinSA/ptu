import random, math, numpy as np
import matplotlib.pyplot as plt 

def uniform(ILOW, IUP):
    u = random.uniform(0, 1)
    return int((IUP - ILOW) * u + ILOW)

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

def geo_1(p):
    M = random.random()
    P = p
    r = 0
    while M >= 0:
        M -= P
        P *= (1 - p)
        r += 1
    return r

def geo_2(p):
    k = 1
    M = random.random()
    while M > p:
        M = random.random()
        k += 1
    return k

def geo_3(p):
    u = random.random()
    q = 1 - p
    return math.floor(math.log(u) / math.log(q)) + 1

def poisson_1(mu):
    if mu >= 88:
        return int(round(normal_poisson(mu, mu) + 0.5))
    P = np.exp(-mu)
    M = np.random.random()
    r = 0
    M -= P
    while M >= 0:
        r += 1
        P *= mu / r
        M -= P
    return r

def poisson_2(mu):
    if mu >= 88:
        return int(round(normal_poisson(mu, mu) + 0.5))
    e = np.exp(-mu)
    M = np.random.random()
    k = 0
    while M >= e:
        k += 1
        M *= np.random.random()
    return k

def generate_uniform(N, ILOW, IUP):
    array = []
    for i in range(N):
        array.append(uniform(ILOW, IUP))
    return array

def generate_bin(N, n, p):
    array = [binomial(n, p) for i in range(N)]
    return array

def generate_geo1(N, p):
    return generate_geo(N, p, geo_1)

def generate_geo2(N, p):
    return generate_geo(N, p, geo_2)

def generate_geo3(N, p):
    return generate_geo(N, p, geo_3)

def generate_geo(N, p, generator):
    array = [generator(p) for i in range(N)]
    return array

def generate_p1(N, mu):
    return generate_p(N, mu, poisson_1)

def generate_p2(N, mu):
    return generate_p(N, mu, poisson_2)

def generate_p(N, mu, generator):
    array = []
    for i in range(N):
        array.append(generator(mu))
    return array

def normal_binomial(N, p):
    m = N * p # матожидание
    s = N * p * (1 - p) ** 0.5 # ско
    x = random.gauss(0, 1) # стандартное нормальное распределение
    return m + x * s

def normal_poisson(m, d):
    s = np.sqrt(d) # ско
    x = np.random.normal() # стандартное нормальное распределение
    return m + x * s

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
    d /= len(u)
    return d

def integral_disp(u):
    n = len(u)
    intervals = 9
    min_val = min(u)
    max_val = max(u)
    delta = float(max_val - min_val) / intervals
    if (delta < 1):
        delta = 1
    elif (delta > 1):
        delta = round(delta, 1)
    start = (max_val - min_val) / 2. - intervals/2. * delta
    f_arr = [0.0] * intervals
    for i in range(1, intervals+1):
        x = start + delta * i
        xPrev = start + delta * (i - 1)
        f_arr[i - 1] = sum(1 for num in u if num < x and num >= xPrev) / (n * delta)
    return f_arr

def p_disp(u):
    n = len(u)
    intervals = 9
    min_val = min(u)
    max_val = max(u)
    delta = float(max_val - min_val) / intervals
    if (delta < 1):
        delta = 1.
    elif (delta > 1):
        delta = round(delta, 1)
    start = (max_val - min_val) / 2. - intervals/2. * delta
    F_arr = [0.0] * intervals
    for i in range(1, intervals+1):
        x = start + delta * i
        F_arr[i - 1] = sum(1 for num in u if num < x) / float(n)
    return F_arr

def printinfo(u):
    m_ = m(u)
    print('M: ', m_)
    print('D: ', d(u, m_))
    f_ = integral_disp(u)
    F_ = p_disp(u)
    print(integral_disp(u))
    print(p_disp(u))
    row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.bar(row, f_, 0.8, 0)
    plt.show()
    plt.bar(row, F_, 0.8, 0)
    plt.show()

def main():
    N = 10000
    array = [] * N
    print("Choose:\n1 - Uniform\n2 - Binomial\n3 - Geometric\n4 - Poisson\n5 - exit")
    type = 0
    while(type!=5):
        type = int(input())
        if type == 1:
            low = 1
            up = 100
            array = generate_uniform(N, low, up)
            printinfo(array)
        elif type == 2:
            n = 10
            p = 0.5
            array = generate_bin(N, n, p)
            printinfo(array)
        elif type == 3:
            p = 0.5
            i = int(input('Choose algorithm: '))
            if i == 1:
                array = generate_geo1(N, p)
            elif i == 2:
                array = generate_geo2(N, p)
            elif i == 3:
                array = generate_geo3(N, p)
            else:
                print('algorithm does not exist.')
                break
            printinfo(array)
        elif type == 4:
            mu = 10
            i = int(input('Choose algorithm: '))
            if i == 1:
                array = generate_p1(N, mu)
            elif i == 2:
                array = generate_p2(N, mu)
            else:
                print('algorithm does not exist.')
                break
            printinfo(array)
        elif type == 5:
            print('program finished')
            break
        else:
            print("option doesn't exist. please, choose option from given ones.")


main()


