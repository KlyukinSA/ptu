from sympy import Symbol, simplify, latex, diff, N, Float
from sympy import log, sin
from sys import argv
import numpy as np


def lmatrix(a):
    if len(a.shape) > 2:
        raise ValueError('matrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{pmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{pmatrix}']
    return '\n'.join(rv).replace('0', ' ')
def TDMA(a, b,  c, f):
    alpha = [-b[0] / c[0]]
    beta = [f[0] / c[0]]
    n = len(f)
    x = np.array([0] * n, dtype='float64')
    for i in range(1, n):
        alpha.append(-b[i]/(a[i]*alpha[i-1] + c[i]))
        beta.append((f[i] - a[i]*beta[i-1])/(a[i]*alpha[i-1] + c[i]))
    x[n-1] = beta[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1]*x[i] + beta[i - 1]
    return x
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
def epsilon(v1, v2):
    # return np.max(v1 - v2)
    d = v1 - v2
    return abs(max(d.min(), d.max(), key=abs))
def delta(v, tilde_v, order):
    return np.linalg.norm(v - tilde_v, order) / np.linalg.norm(v, order)

# solve linear system by odd-even elimination (complete reduction)
# C - array of diagonals (b_m, c_m, d_m) for 1 block `C`
def odd_even_elimination(C, F, n, V):
    def main_diag(l, k):
        # print(np.cos((2 * l - 1) * np.pi / 2**(k+1)))
        return C[1] - 2 * np.cos((2 * l - 1) * np.pi / 2**(k+1))
    def alpha(l, k):
        return (-1)**(l + 1) * np.sin((2 * l - 1) * np.pi / 2**(k+1)) / 2**((k+1) - 1)
    def accumulate(k, phi, psi, target):
        for l in range(1, 2**(k-1) + 1):
            C_m = tridiag(C[0][1:], main_diag(l, k-1), C[2][:-1])
            # print(k, l, np.linalg.det(C_m), target)
            if abs(np.linalg.det(C_m)) < 1e-2:
                print('det=0', k, l, np.linalg.det(C_m), target)
            target += TDMA(C[0], C[2], main_diag(l, k-1), psi + alpha(l, k-1) * phi)

    N = F.shape[0] - 1
    # print(N)
    p = V
    for j in range(1, N):
        p[j] = F[j]
    # print(p)
    for k in range(1, n):
        for j in range(2**k, N, 2**k):
            phi = p[j - 2**(k - 1)] + p[j + 2**(k - 1)]
            psi = np.zeros(phi.shape)
            accumulate(k, phi, psi, p[j])
            p[j] *= 0.5
            # print(k, j, phi, psi, p[j])
    V[0] = F[0]
    V[N] = F[N]
    # print(V)
    # print([i for i in range(n, 0, -1)])
    for k in range(n, 0, -1):
        # print([i for i in range(2**(k-1), N - 2**(k-1) + 1, 2 * 2**(k-1))])
        for j in range(2**(k-1), N, 2**k):
            phi = V[j - 2**(k - 1)] + V[j + 2**(k - 1)]
            psi = p[j].copy()
            V[j] = 0
            accumulate(k, phi, psi, V[j])
            # print(k, j, phi, psi, V[j])

def calculate_Nz(n):
    return 2**n
def calculate_h_r(R_0, R_1, Nr):
    return (R_1 - R_0) / Nr
def calculate_h_z(L, Nz):
    return L / Nz
def make_r_1(R_0, h_r):
    def r_1(i):
        return (R_0 + h_r * i)
    return r_1
def make_r_2(r_1, h_r):
    def r_2(i):
        return (r_1(i) + h_r / 2)
    return r_2
def make_z_1(h_z):
    def z_1(i):
        return (h_z * i)
    return z_1

def calculate_solution_grid(funcs, Nr, n, R_0, R_1, L):
    n_k, n_f, chi, n_phi_1, phi_2, phi_3, phi_4 = funcs

    Nz = calculate_Nz(n)
    h_r = calculate_h_r(R_0, R_1, Nr)
    h_z = calculate_h_z(L, Nz)

    r_1 = make_r_1(R_0, h_r)
    r_2 = make_r_2(r_1, h_r)
    z_1 = make_z_1(h_z)

    C_diags = np.zeros((3, Nr+1))
    for i in range(3):
        for j in range(Nr+1):
            if i == 0:
                if j == 0:
                    v = 0
                elif j == Nr:
                    v = 0
                else:
                    v = -((h_z**2)/(h_r**2)) * (r_2(j-1)/r_1(j)) * n_k(r_2(j-1))
            elif i == 1:
                if j == 0:
                    v = 2 + 2 * ((h_z**2)/h_r) * (chi + (r_2(j)/(r_1(j)*h_r)) * n_k(r_2(j)))
                elif j == Nr:
                    v = 1
                else:
                    v = 2 + ((h_z**2)/(h_r**2)) * (r_2(j-1) * n_k(r_2(j-1)) + r_2(j) * n_k(r_2(j))) / r_1(j)
            else:
                if j == 0:
                    v = -2 * ((h_z**2)/(h_r**2)) * (r_2(j)/r_1(j)) * n_k(r_2(j))
                elif j == Nr:
                    v = 0
                else:
                    v = -((h_z**2)/(h_r**2)) * (r_2(j)/r_1(j)) * n_k(r_2(j))
            # print(i, j, v)
            C_diags[i, j] = v
    # C = tridiag(C_diags[0][1:], C_diags[1], C_diags[2][:-1])
    # print('C=',C_diags)

    F = np.zeros((Nz+1, Nr+1))
    for i in range(Nz+1):
        for j in range(Nr+1):
            if i == 0:
                F[i, j] = phi_3(r_1(j))
            elif i == Nz:
                F[i, j] = phi_4(r_1(j))
            elif j == Nr:
                F[i, j] = phi_2(z_1(i))
            elif j == 0:
                F[i, j] = h_z**2 * (n_f(r_1(j), z_1(i)) + 2 * (n_phi_1(z_1(i))/h_r))
            else:
                F[i, j] = h_z**2 * n_f(r_1(j), z_1(i))
    j = Nr
    odd_even_elimination_F_modification = np.zeros((Nz+1, ))
    for i in range(1, Nz):
        odd_even_elimination_F_modification[i] = F[i - 1, j] + F[i + 1, j]
    for i in range(1, Nz):
        F[i, j] -= odd_even_elimination_F_modification[i]
    # print('F=',F)

    V = np.zeros(F.shape)
    odd_even_elimination(C_diags, F, n, V)
    return V

def calculate_solution_at(point, V, R_0, h_r, h_z):
    return V[round((point[1]-0)/h_z), round((point[0]-R_0)/h_r)]


np.set_printoptions(linewidth=np.inf)
fmt = "%0.2e"
latex_flag = len(argv) > 2 and argv[2] == 'latex'
point_flag = len(argv) > 4 and argv[4] == 'point'
custom = [1.3, 1.3] # specified coordinates
if point_flag:
    print('custom =',custom)
if argv[1] == 'w':
    r = Symbol('r')
    z = Symbol('z')

    chi = 2
    R_0 = 1
    R_1 = 3
    L = 2
    test_cases = [
        ( Float(1), r + z**3 ),
        ( r + 1, r + z**3 ),
        ( (r + 1)**2, r + z**3 ),
    ]
    for test_num, test_case in enumerate(test_cases):
        print('test', test_num+1, test_case)
        k, u = test_case
        f = -( (1 / r) * diff(r * k * u.diff(r), r) + u.diff(z).diff(z))
        phi = chi * u - k * u.diff(r)
        if latex_flag:
            print(str(test_num+1)+'&$'+latex(k)+'$&$'+latex(u)+'$&$'+latex(simplify(f))+'$&$'+latex(simplify(phi).subs(r, 'R0'))+'$\\\\')
        def n_k(param_r):
            return N(k.subs({r: param_r}))
        def n_u(param_r, param_z):
            return N(u.subs({r: param_r, z: param_z}))
        def n_f(param_r, param_z):
            return N(f.subs({r: param_r, z: param_z}))
        def n_phi_1(param_z):
            return N(phi.subs({r: R_0, z: param_z}))

        def phi_2(z):
            return n_u(R_1, z)
        def phi_3(r):
            return n_u(r, 0)
        def phi_4(r):
            return n_u(r, L)
        funcs = (n_k, n_f, chi, n_phi_1, phi_2, phi_3, phi_4)

        prev_delta_1 = np.inf
        for Nr, n in [(2**i, i) for i in range(1, int(argv[3]))]:            
            V = calculate_solution_grid(funcs, Nr, n, R_0, R_1, L)
            
            Nz = calculate_Nz(n)
            h_r = calculate_h_r(R_0, R_1, Nr)
            h_z = calculate_h_z(L, Nz)

            r_1 = make_r_1(R_0, h_r)
            z_1 = make_z_1(h_z)
            x = np.zeros((Nz+1, Nr+1))
            for i in range(Nz+1):
                for j in range(Nr+1):
                    x[i, j] = n_u(r_1(j), z_1(i))
            # print('x=',x)
            
            ds = np.average(np.array([delta(x, V, 1), delta(x, V, 2), delta(x, V, np.inf)]))
            if point_flag:
                v = calculate_solution_at(custom, V, R_0, h_r, h_z) 
                print(v, fmt % abs(v - n_u(custom[0], custom[1])))
            else:
                print(Nr,Nz,fmt%delta(x, V, 1),fmt%delta(x, V, 2),fmt%delta(x, V, np.inf),'%0.2f'%(prev_delta_1/ds),sep='&',end='\\\\\n')
            prev_delta_1 = ds
elif argv[1] == 'eq':
    Nr = 3
    n = 2
    Nz = 2**n
    C_diags = np.zeros((3, Nr+1))
    for i in range(3):
        for j in range(Nr+1):
            if i == 0:
                if j == 0 or j == Nr:
                    v = 0
                else:
                    v = 2
            elif i == 1:
                if j == Nr:
                    v = 1
                else:
                    v = 5
            else:
                if j > Nr - 2:
                    v = 0
                else:
                    v = 2
            C_diags[i, j] = v
    # print(C_diags)
    C = tridiag(C_diags[0][1:], C_diags[1], C_diags[2][:-1])
    # print(C)
    # print((np.linalg.eig(C).eigenvalues))

    A = np.identity((Nr+1)*(Nz+1))
    E = np.identity(Nr+1)
    for i in range(1, Nz):
        A[i * (Nr+1):(i + 1) * (Nr+1), i * (Nr+1):(i + 1) * (Nr+1)] = C
        A[i * (Nr+1):(i + 1) * (Nr+1), (i - 1) * (Nr+1):i * (Nr+1)] = -E
        A[i * (Nr+1):(i + 1) * (Nr+1), (i + 1) * (Nr+1):(i + 2) * (Nr+1)] = -E
    # print(A)
    # print((np.linalg.eig(A).eigenvalues))

    np.random.seed(0)
    x = np.random.rand(A.shape[0])
    x = np.round(x, 2)
    # print(x)
    b = A @ x
    # print(b)
    # print(epsilon(x, np.linalg.solve(A, b)))

    F = b.reshape((Nz+1, Nr+1))
    # print(F)
    V = np.zeros(F.shape)
    odd_even_elimination(C_diags, F, n, V)
    print(epsilon(x, V.flatten()))
    print(Nr,Nz,fmt%delta(x, V.flatten(), 1),fmt%delta(x, V.flatten(), 2),fmt%delta(x, V.flatten(), np.inf),sep='&',end='\\\\\n')
    # print(F.flatten())
    # print(V.flatten())
    # print(x)
    if latex_flag:
        print(lmatrix(A.astype(np.int64)))
        print(lmatrix(b))
        print(lmatrix(x))
else:
    print('no', argv[1])
