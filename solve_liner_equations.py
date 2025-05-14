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

def jacobi_recursion(mat,b,n=None,*,use_logger=True,start=None,times=20):
    if n is None:
        n = len(mat)-1

    if start is None:
        start = [0 for _ in range(n+1)]
    
    def recursion(xk):
        res = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            res[i] = b[i]
            for j in range(1,n+1):
                if i != j:
                    res[i] -= mat[i][j] * xk[j]
            
            res[i] /= mat[i][i]
        
        return res

    temp = start
    if use_logger:
        globals.output_vector(temp,prefix="第0次迭代:\n",end="\n")

    for i in range(1,times+1):
        temp = recursion(temp)
        if use_logger:
            globals.output_vector(temp,prefix=f"第{i}次迭代:\n",end="\n")

    return temp


def gauss_seidel(mat,b,n=None,*,use_logger=True,start=None,times=20):
    if n is None:
        n = len(mat)-1

    if start is None:
        start = [0 for _ in range(n+1)]
    
    def recursion(xk):
        res = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            res[i] = b[i]
            for j in range(1,n+1):
                if i < j:
                    res[i] -= mat[i][j] * xk[j]
                elif i > j:
                    res[i] -= mat[i][j] * res[j]
            
            res[i] /= mat[i][i]
        
        return res

    temp = start
    if use_logger:
        globals.output_vector(temp,prefix="第0次迭代:\n",end="\n")

    for i in range(1,times+1):
        temp = recursion(temp)
        if use_logger:
            globals.output_vector(temp,prefix=f"第{i}次迭代:\n",end="\n")

    return temp

def SOR(mat,b,w,n=None,*,use_logger=True,start=None,times=20):
    if n is None:
        n = len(mat)-1

    if start is None:
        start = [0 for _ in range(n+1)]
    
    def recursion(xk):
        res = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            res[i] = b[i]
            for j in range(1,n+1):
                if i < j:
                    res[i] -= mat[i][j] * xk[j] * w
                elif i > j:
                    res[i] -= mat[i][j] * res[j] * w
            
            res[i] /= mat[i][i]
            res[i] += (1-w)*xk[i]
        
        return res

    temp = start
    if use_logger:
        globals.output_vector(temp,prefix="第0次迭代:\n",end="\n")

    for i in range(1,times+1):
        temp = recursion(temp)
        if use_logger:
            globals.output_vector(temp,prefix=f"第{i}次迭代:\n",end="\n")

    return temp