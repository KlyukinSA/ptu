import numpy as np

# Метод прогонки https://ru.wikibooks.org/wiki/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BF%D1%80%D0%BE%D0%B3%D0%BE%D0%BD%D0%BA%D0%B8
#  * b - диагональ, лежащая над главной          (нумеруется: [0;n-1], b[n-1]=0)
#  * c - главная диагональ матрицы A             (нумеруется: [0;n-1])
#  * a - диагональ, лежащая под главной          (нумеруется: [0;n-1], a[0]=0)
#  * f - правая часть (столбец)                  (нумеруется: [0;n-1])
#  * x - решение, массив x будет содержать ответ (нумеруется: [0;n-1])
def TDMA(a, b, c, f):
    a, b, c, f = tuple(map(lambda k_list: list(map(float, k_list)), (a, b, c, f)))

    alpha = [-b[0] / c[0]]
    beta = [f[0] / c[0]]
    n = len(f)
    x = [0]*n

    for i in range(1, n):
        alpha.append(-b[i]/(a[i]*alpha[i-1] + c[i]))
        beta.append((f[i] - a[i]*beta[i-1])/(a[i]*alpha[i-1] + c[i]))

    x[n-1] = beta[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1]*x[i] + beta[i - 1]

    return x

if False:
    a = np.array([0, 0, 0])
    b = np.array([0, 0, 0])
    c = np.array([1, 1, 1])
    f = np.array([1, 1, 1])
    x = TDMA(a, b, c, f)
    print(x - np.array([1.0, 1.0, 1.0]))

    # Пример вычисления https://scask.ru/i_book_clm.php?id=47
    # но лучше взять со всеми целыми числами
    a = np.array([0, 2, 2, 3])
    b = np.array([-1, -1, -0.8, 0])
    c = np.array([5, 4.6, 3.6, 4.4])
    f = np.array([2, 3.3, 2.6, 7.2])
    x = TDMA(a, b, c, f)
    print(x - np.array([0.5256, 0.628, 0.64, 1.2]))

bl = 0
br = 1
N = 10
wN = N + 1
h = (br - bl) / N
def r_1(i):
    return bl + h * i
def r_2(i):
    return r_1(i) + h / 2
def h_1(i):
    return h
def h_2(i):
    if i % N == 0:
        return h / 2
    return h

# def k(r):
#     return 1
# def q(r):
#     return 1
# def f(r):
#     return 1
# u = [1] * wN
# v2 = u[-1]
# Xi2 = v2

def k(r):
    return 3*r
def q(r):
    return 4*r+3
def f(r):
    return 8*r*r+12*r-9
u = [2*r_1(i)+1 for i in range(wN)]
v2 = u[-1]
Xi2 = 1 - 2 * k(r_1(N)) / v2

def k_2(i):
    return k(r_2(i))
def q_1(i):
    return q(r_1(i))
def f_1(i):
    return f(r_1(i))
a = [0] * wN
b = [0] * wN
c = [0] * wN
g = [0] * wN

# середина
for i in range(1, N):
    a[i] = r_2(i - 1) * k_2(i - 1) / h_1(i)
    c[i] = -(r_2(i - 1) * k_2(i - 1) / h_1(i)
        + r_2(i) * k_2(i) / h_1(i + 1)
        + h_2(i) * r_1(i) * q_1(i))
    b[i] = r_2(i) * k_2(i) / h_1(i + 1)
    g[i] = -h_2(i) * r_1(i) * f_1(i)

i = 0
a[i] = 0
c[i] = h_1(i) * r_2(i) * q_1(i) / 2 \
    + r_2(i) * k_2(i) / h_1(i + 1)
b[i] = -r_2(i) * k_2(i) / h_1(i + 1)
g[i] = h_1(i) * r_2(i) * f_1(i) / 2

i = N
a[i] = -r_2(i - 1) * k_2(i - 1) / h_1(i)
c[i] = r_1(i) * Xi2 \
    + r_2(i - 1) * k_2(i - 1) / h_1(i) \
    + h_2(i) * r_1(i) * q_1(i)
b[i] = 0
g[i] = h_2(i) * r_1(i) * f_1(i) + r_1(i) * v2

x = TDMA(a, b, c, g)
print(u)
print(x - np.array(u))
