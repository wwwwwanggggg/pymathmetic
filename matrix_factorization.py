import globals
import math


def lu(mat,n=None):
    if n is None:
        n = len(mat)-1
    
 
    res = globals.zeros(n,n)
    l,u = globals.zeros(n,n),globals.zeros(n,n)

    def compute(r,c):
        origin = mat[r][c]
        for i in range(min(r,c)):
            origin -= res[r][i]*res[i][c]
        
        return origin


    for i in range(1,n+1):
        for j in range(1,n+1):
            temp = compute(i,j)
            if i <= j:
                res[i][j] = temp
            else:
                res[i][j] = temp / res[j][j]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < j:
                u[i][j] = res[i][j]
            elif i == j:
                u[i][j] = res[i][j]
                l[i][j] = 1
            else:
                l[i][j] = res[i][j]
    
    return l,u
    
    
def Cholesky(mat,n=None):
    if n is None:
        n = len(mat)-1
    
    res = globals.zeros(n,n)

    def compute_drag(r):
        origin = mat[r][r]
        for i in range(1,r):
            origin -= res[r][i]**2
        
        return math.sqrt(origin)
    
    def compute(r,c):
        origin = mat[r][c]
        for i in range(1,c):
            origin -= res[r][i]*res[c][i]
        
        return origin / res[j][j]

    for i in range(1,n+1):
        for j in range(1,i+1):
            if i != j:
                res[i][j] = compute(i,j)
            else:
                res[i][j] = compute_drag(i)

    return res


def Gauss(mat,m=None,n=None):
    print(mat)
    if m is None or n is None:
        m = len(mat)-1
        n = len(mat[1])-1
    
    res = mat.copy()

    for i in range(1,m+1):
        for j in range(i+1,m+1):
            num = -res[j][i]/res[i][i]
            globals.add_row_to_other(mat,i,j,num,m,n)

def Givens():
    pass



    


def QR(mat,m=None,n=None):
    """m for row and n for column"""
    if m is None or n is None:
        m = len(mat)-1
        n = len(mat[0])-1

    