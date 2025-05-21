import numerical_diff as nd

def Euler(f:callable,x0,y0,h,n):    
    result = [(x0,y0)]

    x = x0
    y = y0
    for i in range(n):
        y = y+h*f(x,y)
        x += h
        result.append((x,y))

    return result   

# 标准4级4阶R-K法
def Runge_Kutta(f:callable,x0,y0,h,n):
    result = [(x0,y0)]

    x = x0
    y = y0

    for i in range(n):
        k1 = h*f(x,y)
        k2 = h*f(x+h/2,y+k1/2)
        k3 = h*f(x+h/2,y+k2/2)
        k4 = h*f(x+h,y+k3)

        y = y+(k1+k2+k3+k4)/6
        x += h
        result.append((x,y))

    
    return result