import matrix_norm as matn
import globals as g

v = [3,4,9,45,12,789,3]

mat = [
    [1,2,5,8],
    [4,9,3,7],
    [5,0,4,1],
    [1,3,4,4]
]

hhh = [
    [4],
    [74],
    [7],
    [4]
]

g.indexlize(mat)
g.vectorlize(v)
g.indexlize(hhh)


g.output(g.multiple(mat,2))