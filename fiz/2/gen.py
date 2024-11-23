from sympy import Symbol, simplify, latex
from sympy import cos, sin, exp

one = Symbol('1')
r = Symbol('r')
t = Symbol('t')
k = cos(r) / 2 + 3
q = sin(r) / 2 + 2
chi = 2 * t + 1

def pp(v):
    print(latex(v))

for u in one, r**2, 4 + exp(-1 * t**2), r**2 + t**2:
    pp(u)
    f = u.diff(t) - (1 / r) * (r * k * u.diff(r)).diff(r) + q * u
    pp(simplify(f))
    nu = chi * u + k * u.diff(r)
    pp(simplify(nu).subs(r, 'R'))
    print()

