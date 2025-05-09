import globals
import matrix_factorization as matf

def get_equations():
    print("Ax=b\n请输入A")
    A = globals.get_matrix()
    print("请输入b")
    b = list(map(int,input().split(" ")))

    return A,b

# 传参请保证是三角矩阵，否则计算出错此函数概不负责
def angle_mat_solve():
    pass


def lu_solve(A,b):
    l,u = matf.lu(A)

