import globals

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

def lu(mat,n=None):
    if n is None:
        n = len(mat)-1
    
 
    res = globals.zeros(n,n)

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
    
    
    return res


# test data
# mat = [
#     [4,-2,0,4],
#     [-2,2,-3,1],
#     [0,-3,13,-7],
#     [4,1,-7,23]
# ]

# globals.indexlize(mat)

# res = lu(mat)


# print(res)
# globals.output(res)