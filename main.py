from sympy import *

x = Symbol('x')
y = x**2
yp = y.diff(x)

print(type(yp))