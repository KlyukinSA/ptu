import random, math, numpy as np
import matplotlib.pyplot as plt 

def uniform(ILOW, IUP):
    u = random.random()
    return int((IUP - ILOW) * u + ILOW)

def normal_miller():
    u1 = random.random()
    u2 = random.random()
    return math.sqrt(-2 * math.log(u2)) * math.cos(2 * math.pi * u1)

def normal_center():
    r = 0
    for i in range(12):
        r += random.random()
    return r - 6

def exponential(b):
    u = random.random()
    return -b * math.log(u)

def hi_disp(N):
    y = 0
    for i in range (N):
        u = random.gauss(0, 1)
        y += u * u
    return y

def student(N):
    z = random.gauss(0, 1)
    y = hi_disp(N)
    return z / math.sqrt(y / N)

def generate_uniform(N, ILOW, IUP):
    array = [] * N
    for i in range(N):
        array.append(uniform(ILOW, IUP))
    return array

def generate_norm1(N):
    return generate_norm(N, normal_miller)

def generate_norm2(N):
    return generate_norm(N, normal_center)

def generate_norm(N, generator):
    array = [] * N
    for i in range (N):
        array.append(generator())
    return array

def generate_exp(N, b):
    array = []
    for i in range (N):
        array.append(exponential(b))
    return array

def generate_hidisp(N, n):
    array = [] * N
    for i in range (N):
        array.append(hi_disp(n))
    return array

def generate_student(N, n):
    array = [] * N
    for i in range (N):
        array.append(student(n))
    return array

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

def integral_disp(u, num):
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
    if (num == 2 or num == 5):
        start = -intervals / 2. * delta
    f_arr = []
    for i in range(intervals):
        x = start + delta * (i + 1)
        xPrev = start + delta * (i)
       # f_arr.append(len([num for num in u if xPrev <= num < x]) / (n * delta))
        f_arr.append(sum(1 for num in u if num < x and num >= xPrev) / (n * delta))
    return f_arr

def p_disp(u, num):
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
    if (num == 2 or num == 5):
        start = -intervals / 2. * delta
    F_arr = []
    for i in range(intervals):
        x = start + delta * (i + 1)
        F_arr.append(sum(num < x for num in u) / n)
    return F_arr

def printinfo(u, num):
    m_ = m(u)
    print('M: ', m_)
    print('D: ', d(u, m_))
    f_ = integral_disp(u, num)
    F_ = p_disp(u, num)
    print(f_)
    print(F_)
    row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.bar(row, f_, 0.8)
    plt.show()
    plt.bar(row, F_, 0.8)
    plt.show()

def main():
    N = 10000
    array = [] * N
    print("Choose:\n1 - Uniform\n2 - Normal\n3 - Exponential\n4 - Hi-dispersion\n5 - Student\n6 - exit")
    type = 0
    while(type!=6):
        type = int(input())
        if type == 1:
            low = 1
            up = 100
            array = generate_uniform(N, low, up)
            printinfo(array, type)
        elif type == 2:
            i = int(input('Choose algorithm: '))
            if i == 1:
                array = generate_norm1(N)
            elif i == 2:
                array = generate_norm2(N)
            else:
                print('algorithm does not exist.')
                break
            printinfo(array, type)
        elif type == 3:
            b = 1
            array = generate_exp(N, b)
            printinfo(array, type)
        elif type == 4:
            n = 10
            array = generate_hidisp(N, n)
            printinfo(array, type)
        elif type == 5:
            n = 10
            array = generate_student(N, n)
            printinfo(array, type)
        elif type == 6:
            print('program finished')
            break
        else:
            print("option doesn't exist. please, choose option from given ones.")

main()


