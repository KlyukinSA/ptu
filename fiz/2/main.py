import numpy as np
import sys
import matplotlib.pyplot as plt


def TDMA(a, b, c, f):
    alpha = [-b[0] / c[0]]
    beta = [f[0] / c[0]]
    n = len(f)
    x = np.array([0] * n, dtype='float32')
    for i in range(1, n):
        alpha.append(-b[i]/(a[i]*alpha[i-1] + c[i]))
        beta.append((f[i] - a[i]*beta[i-1])/(a[i]*alpha[i-1] + c[i]))
    x[n-1] = beta[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1]*x[i] + beta[i - 1]
    return x

def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)


test_index = int(sys.argv[1])
method = sys.argv[2]
fmt = "%0.2E"

bl = 0
br = 1
Ns = [pow(2, 3 + i) for i in range(int(sys.argv[3]))]
# Ns = [4,8,16,32]

T = 1
Hs = [pow(10, -1 - i) for i in range(int(sys.argv[3]))]
# Hs = [1e-2, 1e-6]

print(Ns, Hs)
maxmaxes = []
for N in Ns:
    maxmaxes.append([])
    wN = N + 1
    h = (br - bl) / N
    def r_1(i):
        return np.float32(bl + h * i)
    def r_2(i):
        return np.float32(r_1(i) + h / 2)
    def h_1(i):
        return np.float32(h)
    def h_2(i):
        if i % N == 0:
            return np.float32(h / 2)
        return np.float32(h)

    def tones():
        for H in Hs:
            v0 = np.array([np.float32(phi(r_1(i))) for i in range(wN)], dtype='float32')
            v = v0.copy()
            maxes = []
            # T = H * 100
            for t in np.arange(0, T, H):
                if method == 'imp':
                    t = t + H
                
                def k_2(i):
                    return np.float32(k(r_2(i), t))
                def q_1(i):
                    return np.float32(q(r_1(i), t))
                def u_1(i):
                    return np.float32(u(r_1(i), t))
                def f_1(i):
                    return np.float32(f(r_1(i), t))
                def B_1(i):
                    return np.float32(r_2(i) * k_2(i) / h_2(i) / r_1(i) / h_1(i + 1))
                def B_2(i):
                    return np.float32(r_2(i - 1) * k_2(i - 1) / h_2(i) / r_1(i) / h_1(i))
                def C_1(i):
                    return np.float32(2 * k_2(i) / h_2(i) / h_1(i + 1))
                chi_1 = np.float32(chi(t))
                nu_1 = np.float32(nu(t))

                a = np.array([0] * wN, dtype='float32')
                b = np.array([0] * wN, dtype='float32')
                c = np.array([0] * wN, dtype='float32')
                g = np.array([0] * wN, dtype='float32')

                for i in range(1, N):
                    a[i] = B_2(i)
                    c[i] = -(B_1(i) + B_2(i) + q_1(i))
                    b[i] = B_1(i)
                    g[i] = f_1(i)

                i = 0
                a[i] = 0
                c[i] = -(C_1(i) + q_1(i))
                b[i] = C_1(i)
                g[i] = f_1(i)

                i = N
                a[i] = B_2(i)
                c[i] = -(B_2(i) + q_1(i) + chi_1 / h_2(i))
                b[i] = 0
                g[i] = nu_1 / h_2(i) + f_1(i)

                if method == 'exp':
                    A = tridiag(a[1:], c, b[:-1])
                    # norms.append(np.linalg.norm(A))
                    try:
                        integrand = A @ v + g
                    except RuntimeWarning:
                        # print(t, i, A.max(), v.max())
                        pass
                    v = v + H * integrand
                else:
                    a = -H * a
                    b = -H * b
                    c = 1 - H * c
                    g = v + H * g
                    v = TDMA(a, b, c, g)
                d = v.astype('float32') - np.array([u_1(i) for i in range(wN)], dtype='float32')
                val = abs(max(d.min(), d.max(), key=abs))
                maxes.append(val)
            # plt.plot(np.arange(0, T, H), norms)
            # plt.show()
            maxmaxes[-1].append(max(maxes))
  
    def phi(r):
        return u(r, 0)

    if test_index == 4:
        def chi(t):
            return 1
        def k(r, t):
            return 3*r+2
        def q(r, t):
            return 4*r+3
        def u(r, t):
            return 1
        def f(r, t):
            return q(r, t)
        def nu(t):
            return chi(t)
        tones()
    
    def chi(t):
        return 2*t+1
    
    if test_index == 0:
        def k(r, t):
            return 3*r+2
        def q(r, t):
            return 4*r+3
        def u(r, t):
            return 1 + t
        def f(r, t):
            return 1 + q(r, t) * u(r, t)
        def nu(t):
            return chi(t) * u(br, t)
        tones()

    def k(r, t):
        return np.cos(r) / 2 + 3
    def q(r, t):
        return np.sin(r) / 2 + 2
    
    if test_index == 1:
        def u(r, t):
            return r**2
        def f(r, t):
            return r**2*(np.sin(r) + 4)/2 + r*np.sin(r) - 2*np.cos(r) - 12
        def nu(t):
            return br*(2*br*t + br + np.cos(br) + 6)
        tones()

    if test_index == 2:
        def u(r, t):
            return 4 + np.exp(-10*t**2)
        def f(r, t):
            return (-40*t + (4*np.exp(10*t**2) + 1)*(np.sin(r) + 4))*np.exp(-10*t**2)/2
        def nu(t):
            return (2*t + 1)*(4*np.exp(10*t**2) + 1)*np.exp(-10*t**2)
        tones()

    if test_index == 3:
        def u(r, t):
            return r**2 + t**2
        def f(r, t):
            return r*np.sin(r) + 2*t + (r**2 + t**2)*(np.sin(r) + 4)/2 - 2*np.cos(r) - 12
        def nu(t):
            return br*(np.cos(br) + 6) + (br**2 + t**2)*(2*t + 1)
        tones()

    if test_index == 5:
        def k(r, t):
            return r + t + 1
        def q(r, t):
            return r**(0.5) * np.sin(t)
        def u(r, t):
            return r**2*np.exp(-t)
        def f(r, t):
            return (-r**2 - 6*r + r**2.5*np.sin(t) - 4*t - 4)*np.exp(-t)
        def nu(t):
            return br*(2*br*t + 3*br + 2*t + 2)*np.exp(-t)
        tones()

print(maxmaxes)
