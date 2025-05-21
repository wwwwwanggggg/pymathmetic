import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle
import poly_interp as p
import numerical_integration as ni
from math import *
import numerical_diff as nd

import time

def f(x):
    return exp(x)

print(nd.extrapolation(f,1,0.8,3))
# print(nd.two_points(f,[0.2,1.8]))

