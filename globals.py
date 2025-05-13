from functools import *
from typing import List

def get_matrix()->list[list]:
    print("输入矩阵的行数和列数，用空格分开")
    # n,m row,column
    n,m = map(int,input().split(" "))

    print("输入矩阵的每行元素，用回车分开行")

    matrix = [[0 for _ in range(m)]]

    for i in range(1,n+1):
        t = list(map(int,input().split(" ")))
        t.insert(0,0)
        matrix.append(t)
    
    return matrix

def zeros(n,m): 
    return [[0 for _ in range(m+1)] for _ in range(n+1)]


def multi_row(mat,row,num,m=None,n=None):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1

    for i in range(1,n+1):
        mat[row][i] *= num


def multi_column(mat,column,num,m=None,n=None):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1

    for i in range(1,n+1):
        mat[i][column] *= num

def add_row_to_other(mat,row,added_row,num,m=None,n=None):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1

    for i in range(1,n+1):
        mat[added_row][i] += num * mat[row][i]

    
def add_column_to_other(mat,column,added_column,num,m=None,n=None):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1

    for i in range(1,n+1):
        mat[i][added_column] += num * mat[i][column]


def indexlize(mat:list):
    column = len(mat[0])
    row = len(mat)

    mat.insert(0,[0 for _ in range(column+1)])
    for i in range(1,row+1):
        mat[i].insert(0,0)


def output(mat,n=None,m=None,width=10,*,prefix="",end="\n"):
    print(prefix,end="")

    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(f"{mat[i][j]:<{width}}", end="")
        print("")
    
    print(end,end="")

def output_vector(v,*,prefix="",end="\n"):
    print(prefix,end="")
    for i in range(1,len(v)):
        print(v[i])
    print(end,end="")


# n*1 或者 1*m 的矩阵转化成额行向量或者列向量,以列表类型返回
# 用户自己要清楚是行向量还是列向量
def vectorlize(mat):
    mat.insert(0,0)


def T(A,n=None):
    if n is None:
        n = len(A)-1
    
    for i in range(1,n+1):
        for j in range(1,i):
            A[i][j],A[j][i] = A[j][i],A[i][j]

def add(a,b,m=None,n=None):
    if m is None or n is None:
        m = len(a)-1
        n = len(a[1])-1

    res = zeros(m,n)

    for i in range(1,m+1):
        for j in range(1,n+1):
            res[i][j] = a[i][j] + b[i][j]

    return res

def multiple(a,b,*,ar=None,ac=None,br=None,bc=None):
    if ar is None or ac is None:
        ar = len(a)-1
        ac = len(a[1])-1
    if not isinstance(b,list):
        res = zeros(ar,ac)
        for i in range(1,ar+1):
            for j in range(1,ac+1):
                res[i][j] = a[i][j]*b
            
        return res
    
    if br is None or bc is None:
        br = len(b)-1
        bc = len(b[1])-1
    
    res = zeros(ar,bc)


    def compute(i,j):
        res = 0
        if ac != br:
            raise TypeError("The matrixs can not be multiped")
        for k in range(1,ac+1):
            res += a[i][k]*b[k][j]

        return res

    for i in range(1,ar+1):
        for j in range(1,bc+1):
            res[i][j] = compute(i,j)
        
    return res

        
def minus(a,b,m=None,n=None):
    if m is None or n is None:
        m = len(a)-1
        n = len(a[1])-1
    
    tempb = multiple(b,-1)
    return add(a,tempb)
    


def eigvals(mat,n=None):
    if n is None:
        n = len(n)-1
    
    
    
    


# A = [
#     [1,2,4],
#     [3,4,8],
#     [5,12,30]
# ]

# indexlize(A)
# T(A)
# output(A)

# A = [[1,2,3,4]]
# indexlize(A)
# print(A)

# print(vectorlize(A))