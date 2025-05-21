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

def f(x,y):
    return -0.9*y/(1+2*x)

print(ode.Euler(f,0,1,0.02,5))
print()
print(ode.Runge_Kutta(f,0,1,0.02,5))