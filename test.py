import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle

v = [3,4,9,45]

mat = [
    [1,2,5,8],
    [4,9,3,7],
    [5,0,4,1],
    [1,3,4,4]
]

other = [
    [10,-1,-2],
    [-1,10,-2],
    [-1,-1,5]
]

vv = [72,83,42]


g.indexlize(other)
g.vectorlize(vv)

starter = [1,1,1,1]
g.vectorlize(starter)

# res = sle.jacobi_recursion(other,vv,3)
res = sle.gauss_seidel(other,vv,3)


g.output_vector(res)