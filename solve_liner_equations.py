import globals
import matrix_factorization as matf

def get_equations():
    print("Ax=b\n请输入A")
    A = globals.get_matrix()
    print("请输入b")
    b = list(map(int,input().split(" ")))

    return A,b

# 传参请保证是三角矩阵，否则计算出错此函数概不负责
def down_angle_mat_solve(A,b,n=None):
    if n is None:
        n = len(b)-1
    
    res = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        origin = b[i]
        for j in range(1,i):
            origin -= A[i][j]*res[j]
        res[i] = origin / A[i][i]
    
    return res

def up_angle_mat_solve(A,b,n=None):
    if n is None:
        n = len(b)-1
    
    res = [0 for _ in range(n+1)]
    for i in range(n,0,-1):
        origin = b[i]
        for j in range(n,i,-1):
            origin -= A[i][j] * res[j]
        res[i] = origin / A[i][i]

    return res

def lu_solve(A,b,n=None):
    if n is None:
        n = len(b)-1
    l,u = matf.lu(A,n)

    y = down_angle_mat_solve(l,b,n)
    globals.output_vector(y)
    x = up_angle_mat_solve(u,y,n)
    return x

def cholesky_solve(A,b,n=None):
    if n is None:
        n = len(b)-1

    g = matf.cholesky(A,n)
    y = down_angle_mat_solve(g,b,n)
    globals.T(g,n)
    x = up_angle_mat_solve(g,y,n)

    return x


# A  = [
#     [3,0,0,0],
#     [6,3,0,0],
#     [3,-6,9,0],
#     [-9,3,6,3]
# ]

# b = [1,2,16,8]
# globals.vectorlize(b)
# globals.indexlize(A)
# globals.output_vector(up_angle_mat_solve(A,b))

# B = [
#     [1,2,1],
#     [0,3,-2],
#     [0,0,2]
# ]
# globals.indexlize(B)

# b = [3,-9,6]
# globals.vectorlize(b)

# globals.output_vector(up_angle_mat_solve(B,b))


A = [
    [1,2,3],
    [2,5,8],
    [3,8,14]
]

b = [6,18,32]

globals.indexlize(A)
globals.vectorlize(b)

globals.output_vector(lu_solve(A,b))
print()
globals.output_vector(cholesky_solve(A,b))