def zeros(n,m): 
    return [[0 for _ in range(m+1)] for _ in range(n+1)]

def indexlize(mat:list):
    column = len(mat[0])
    row = len(mat)

    mat.insert(0,[0 for _ in range(column+1)])
    for i in range(1,row+1):
        mat[i].insert(0,0)

def output(mat,n=None,m=None):
    if n is None or m is None:
        n = len(mat)-1
        m = len(mat[0])-1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(mat[i][j],end=" ")
        print("")