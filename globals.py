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

def indexlize(mat:list):
    column = len(mat[0])
    row = len(mat)

    mat.insert(0,[0 for _ in range(column+1)])
    for i in range(1,row+1):
        mat[i].insert(0,0)

def output(mat,n=None,m=None,width=10):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(f"{mat[i][j]:<{width}}", end="")
        print("")