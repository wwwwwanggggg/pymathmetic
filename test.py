import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle
import poly_interp as p
import numerical_integration as ni
from math import *


# f = p.cubic_spline_with_1([-3,-1,0,3,4],[7,11,26,56,29])

# print(f(3))


def f(x):
    if x == 0:
        return 1
    return sin(x)/x


x = [0.125*i for i in range(9)]


print(ni.composite_trapezoid(f,x))
print(ni.composite_Simpson(f,x))
