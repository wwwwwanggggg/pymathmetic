def two_points(f,x):
    h = x[1]-x[0]
    return (f(x[1])-f(x[0]))/h


def extrapolation(f, x, h=1, k=5):  
    table = []
    for i in range(k):
        temp = []
        for j in range(i+1):
            if j == 0:
                temp.append(two_points(f, [x-h, x+h]))
            else:
                res = temp[j-1] + (temp[j-1] - table[i-1][j-1]) / (4**j - 1)
                temp.append(res)
        table.append(temp)
        h /= 2

        
    return table[-1][-1]