import matrix_norm as matn
import globals as g

v = [3,4,9,45,12,789,3]

mat = [
    [1,2,5,8],
    [4,9,3,7],
    [5,0,4,1],
    [1,3,4,4]
]

g.indexlize(mat)
g.vectorlize(v)

print(matn.v_p_norm(v,5))

print(matn.mat_1norm(mat))