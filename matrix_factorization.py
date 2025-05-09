import globals



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
    
    



# test data
# mat = [
#     [4,-2,0,4],
#     [-2,2,-3,1],
#     [0,-3,13,-7],
#     [4,1,-7,23]
# ]

# globals.indexlize(mat)

# l,u = lu(mat)

# globals.output(l)
# print()
# globals.output(u)