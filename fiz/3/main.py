from sympy import Symbol, simplify, latex, diff
from sympy import log, sin
from sys import argv
import numpy as np


def pp(v):
    print(latex(v))
def lmatrix(a):
    if len(a.shape) > 2:
        raise ValueError('matrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{pmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{pmatrix}']
    return '\n'.join(rv).replace('0', ' ')


test_name = argv[-1]
if test_name == 'w':
    one = Symbol('1')
    r = Symbol('r')
    z = Symbol('z')

    chi = 2
    test_cases = [
        ( one, r + z**3 ),
        ( r + 2 * z + 1, r + z**3 ),
        ( (r + 2 * z + 1)**2, r + z**3 ),
        ( sin(r * z) + 2, log(r) + z**(0.5) ),
    ]
    for test_num, test_case in enumerate(test_cases):
        k, u = test_case
        f = -( (1 / r) * diff(r * k * u.diff(r), r) + u.diff(z).diff(z))
        # pp(simplify(f))
        phi = chi * u - k * u.diff(r)
        pp(simplify(phi).subs(r, 'R0'))
        print()
elif test_name == 'eq':
    n = 4
    side = n**2
    A = np.identity(side)
    for k in range(1, n-1):
        left=k * n
        right=(k+1)*n-1
        for i in range(left, right):
            A[i, i] = 5
            if i - 1 >= left:
                A[i, i-1] = 2
            if i + 1 < right:
                A[i, i+1] = 2
            if k > 0:
                A[i, i-n] = -1
            if k < n-1:
                A[i, i+n] = -1
    # print((A))
    print(np.linalg.eig(A).eigenvalues)
    np.random.seed(0)
    x = np.random.rand(side)
    x = np.round(x, 2)
    b = A @ x
    print(np.max(x - np.linalg.solve(A, b)))
    print(lmatrix(A.astype(np.int64)))
    print(lmatrix(b))
    print(lmatrix(x))
else:
    print('no', test_name)
