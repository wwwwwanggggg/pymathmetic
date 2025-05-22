import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle
import poly_interp as p
import numerical_integration as ni
from math import *
import numerical_diff as nd
import equation_recursion as er
import ode_solver as ode
import polynomial as poly
import time

# def f(x):
#     return x**3-2*x-5

# def g(x):
#     return (2*x+5)**(1/3)

# # print(nd.extrapolation(f,1,0.8,3))
# # print(nd.two_points(f,[0.2,1.8]))

# print(er.bisection(f,0,5))
# print(er.recursion(g,1))
# print(er.Newton(f,1))
# # print(er.Newton_downhill(f,1))
# print(er.secant(f,0,5))

# 2n(n+3)(n+5)(n+6)



# for i in range(int(1e6)):
#     h = f(i)
#     if h > 0 and sqrt(h) == int(sqrt(h)):
#         print("result:",i)
# def f(x):
#     return (1+x**2)**(1/3)

# print(er.recursion(f,1.5,1e-5))


# def f(x,y):
#     return 1-y

# print(ode.Euler(f,0,0,0.1,10))
h = p.Hermite([-1,0,1],[[2],[5,12,42],[70,164]])
h.output()

x = list(range(6))

f = poly.Polynomial([5,12,21,20,10,2])
for i in x:
    print(h(i),f(i))