import matrix_norm as matn
import globals as g
import matrix_factorization as matf
import solve_liner_equations as sle
import poly_interp as p


# v = [3,4,9,45]

# mat = [
#     [1,2,5,8],
#     [4,9,3,7],
#     [5,0,4,1],
#     [1,3,4,4]
# ]

# other = [
#     [10,-1,-2],
#     [-1,10,-2],
#     [-1,-1,5]
# ]

# vv = [72,83,42]


# g.indexlize(other)
# g.vectorlize(vv)

# starter = [1,1,1,1]
# g.vectorlize(starter)

# # res = sle.jacobi_recursion(other,vv,3)
# res = sle.gauss_seidel(other,vv,3)


# g.output_vector(res)

# x = [-1,1,2,5]
# y = [-7,7,-4,35]

# f = p.Lagrange(x,y,4)


# print(f(5))

# nums = p.force(x,y,4)

# print(nums)

# f = p.Newton([-1,1,2,5],[-7,7,-4,35])


h = p.Hermite([-1,0],[[0],[-4,0,6]])
print(h(3))
h.add_point(1,[-2,5])

print(h(3))

# n = p.Newton_func()

# n.add_point(1,2)
# n.output()
# n.add_point(1,4)

# n.output()