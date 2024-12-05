from sympy import Symbol, simplify, latex
from sympy import cos, sin, exp


def pp(v):
    print(latex(v))


one = Symbol('1')
r = Symbol('r')
t = Symbol('t')
# k = cos(r) / 2 + 3
# q = sin(r) / 2 + 2
k = r + t + 1
q = r**(0.5) * sin(t)
chi = 2 * t + 1

# for u in one, t + 1, r**2, 4 + exp(-1 * t**2), r**2 + t**2:
for u in [r**2 * exp(-t)]:
    pp(u)
    f = u.diff(t) - (1 / r) * (r * k * u.diff(r)).diff(r) + q * u
    pp(simplify(f))
    nu = chi * u + k * u.diff(r)
    pp(simplify(nu).subs(r, 'br'))
    print()

