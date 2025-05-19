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
def Newton_Cotes(x,y,a,b,n=None):
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
        qf += Ai(i)*y[i]
    
    return qf