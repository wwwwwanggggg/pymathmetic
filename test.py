import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle
import poly_interp as p


f = p.cubic_spline_with_1([-3,-1,0,3,4],[7,11,26,56,29])

print(f(3))
