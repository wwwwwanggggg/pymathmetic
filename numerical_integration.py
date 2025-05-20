import poly_interp as ploy

# 求解已经分解好的多项式在某个区域上的积分
def root_poly_nomial_integration(roots,a,b):
    n = len(roots)
    res = 1
    for i in roots:
        res *= -i
    roots.append(0)
    ys = [0 for _ in range(n)]
    ys.append(res)
    cods = ploy.force(roots,ys,n+1) # 这一步很慢啊

    res = 0
    for i in range(n+1):
        res += cods[i]/(i+1)*(b**(i+1)-a**(i+1))
    
    return res



# 问题在于怎么求多项式的积分
def Newton_Cotes(x,f:callable,a,b,n=None):
    if n is None:
        n = len(x)
    def Ai(i):
        roots = x.copy()
        roots.pop(i)

        up = root_poly_nomial_integration(roots,a,b)
        down = 1
        for j in range(n):
            if j != i:
                down *= (x[i]-x[j])
        return up / down

    qf = 0
    for i in range(n):
        qf += Ai(i)*f(x[i])
    
    return qf

def trapezoid(f:callable,a,b):
    return (b-a)/2*(f(b)+f(a))

def Simpson(f:callable,a,b):    
    return (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))

def Cotes(f:callable,a,b):
    h = (b-a)/4
    x = [0,a+h,a+2*h+a+3*h]

    return (b-a)/90*(7*f(a)+32*f(x[1])+12*f(x[2])+32*f(x[3])+7*f(b))



def composite_trapezoid(f:callable,x,n=None):
    if n is None:
        n = len(x)
    
    res = 0
    for i in range(n-1):
        res += trapezoid(f,x[i],x[i+1])
    
    return res


def composite_Simpson(f:callable,x,n=None): 
    if n is None:
        n = len(x)
    
    res = 0
    for i in range(n-1):
        res += Simpson(f,x[i],x[i+1])

    
    return res

def composite_Cotes(f:callable,x,n=None):
    if n is None:
        n = len(x)
    
    res = 0
    for i in range(n-1):
        res += Cotes(f,x[i],x[i+1])

    return res

def Romberg(f:callable,a,b,epslion=1e-6):
    table = []
    i=0
    j = 0
    temp = []
    while True:
        # 计算t
        if j % 4 == 0:
            temp = []
            h = (b-a)/2**(i)
            x = [a + p*h for p in range(2**i+1)]
            res = composite_trapezoid(f,x,2**i)
            temp.append(res)

        # 计算s
        if i > 0 and j % 4 == 1:
            s = temp[0] + 1/3*(temp[0]-table[i-1][0])
            temp.append(s)
        # 计算 c
        if i > 1 and j % 4 == 2:
            c = temp[1]+1/15*(temp[1]-table[i-1][1])
            temp.append(c)

        # 计算 r
        if i > 2 and j % 4 == 3:
            r = temp[2] + 1/63*(temp[2]-table[i-1][2])
            temp.append(r)
            
        
        if j % 4 == 3:
            table.append(temp)
            if i > 3 and abs(table[i][3]-table[i-1][3]) < epslion:
                return table[i][3]

            i += 1

        j += 1
        
