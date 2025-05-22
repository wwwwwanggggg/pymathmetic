import globals
import solve_liner_equations as sle
from math import *

class Newton_func:
    def __init__(self):
        self.xs = []
        self.table = []

    def add_point(self,x,y):
        self.xs.append(x)
        l = len(self.table)
        ys = [y]
        for i in range(l):
            # print(self.table,l)
            temp = (ys[i] - self.table[l-1][i]) / (self.xs[l]-self.xs[l-1-i])
            ys.append(temp)
        self.table.append(ys)

    def output(self,prefix="",end=""):
        print(prefix,end="")
        for i in range(len(self.xs)):
            print(f"x:{self.xs[i]:<10}y:",end=" ")
            for j in self.table[i]:
                print(f"{str(j):^{4}}", end=" ")
            print()
        print(end,end="")
    
    def __call__(self,x):
        temp = 0
        for i in range(len(self.xs)):
            tt = self.table[i][i]
            for j in range(i):
                tt *= x-self.xs[j]
            temp += tt
        
        return temp

# 返回值是从0次开始到高次
def force(xs,ys,n=None):
    if  n is None:
        n = len(xs)

    A = globals.zeros(n,n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i][j] = xs[i-1]**(j-1)

    cpys = ys.copy()
    globals.vectorlize(cpys)
    res = sle.lu_solve(A,cpys)
    return res[1:]
    

def Lagrange(xs,ys,n=None):
    if n is None:
        n = len(xs)
    
    def f(x):
        temp = 0
        for i in range(n):
            up,down=1,1
            for j in range(n):
                if j != i:
                    up *= x-xs[j]
                    down *= xs[i]-xs[j]
            
            temp += up/down*ys[i]

        return temp

    return f


def Newton(xs,ys,n=None,f=None):
    if n is None:
        n = len(xs)

    if not isinstance(f,Newton_func):
        f = Newton_func()
        
    for i in range(n):
        f.add_point(xs[i],ys[i])
    
    return f


    

# 看起来Hermite 插值不能绕过某一阶导数
# Hermite 完全可以完成Newton插值的功能
class Hermite_func(Newton_func):   
    def __init__(self):
        super().__init__()
    
    # 认为values是一个列表，记录着各阶导数
    def add_point(self, x, values,n=None):
        if n is None:
            n = len(values)
        
        len_xs = len(self.xs)
        for i in range(n):
            self.xs.append(x)
            len_xs += 1
            temp = [values[0]]
            for j in range(1,len_xs):
                # 计算temp表
                down = self.xs[len_xs-1] - self.xs[len_xs-1-j]
                if down == 0:
                    # 说明要取导数
                    temp.append(values[j]/factorial(j))
                else:
                    tt = (temp[j-1] - self.table[len_xs-2][j-1]) / down
                    temp.append(tt)
            
            self.table.append(temp)

    def output(self,prefix="",end=""):
        print(prefix,end="")
        for i in range(len(self.xs)):
            print(f"x:{self.xs[i]:<10}y:",end=" ")
            for j in self.table[i]:
                print(f"{str(j):^{4}}", end=" ")
            print()
        print(end,end="")


def Hermite(xs,ys,n=None,h=None):
    if n is None:
        n = len(xs)

    if not isinstance(h,Hermite_func):
        h = Hermite_func()
    
    for i in range(n):
        h.add_point(xs[i],ys[i])
    
    return h
    

def compute_lists(x:list,y:list,n=None):
    if n is None:
        n = len(x)

    # 足标都从1开始
    x.insert(0,0)
    y.insert(0,0)
    h = [x[i]-x[i-1] for i in range(1,n+1)]
    h.insert(0,0)

    mu = [h[i]/(h[i]+h[i+1]) for i in range(1,n)]
    lam = [1-i for i in mu]
    mu.insert(0,0)
    lam.insert(0,0)

    d = [6/(h[i]+h[i+1])*((y[i+1]-y[i])/h[i+1]-(y[i]-y[i-1])/h[i]) for i in range(1,n)]
    d.insert(0,0)
    return mu,lam,d,h


# 默认认为x 是按照大小顺序传入
def cubic_spline_with_2(x,y,l=0,r=0,n=None,solve=sle.lu_solve):
    if n is None:
        n = len(x)

    mu,lam,d,h = compute_lists(x,y,n)
    
    mat = globals.zeros(n-1,n-1)
    for i in range(1,n):
        for j in range(1,n):
            if i == j:
                mat[i][j] = 2
            elif i == j+1:
                mat[i][j] = mu[i]
            elif i == j-1:
                mat[i][j] = lam[j]
    
    # M_0=l   M_n=r
    b = [0,d[1]-mu[1]*l]
    for i in range(2,n-1):
        b.append(d[i])
    b.append(d[n-1]-lam[n-1]*r)

    m = solve(mat,b,n-1)
    m[0] = l
    m.append(r)
    def compute(k):
        for i in range(2,n+1):
            if k >= x[i-1] and k <= x[i]:
                res = (x[i]-k)**3/6/h[i]*m[i-1]
                res += (k-x[i-1])**3/6/h[i]*m[i]
                res += (y[i-1]-h[i]**2/6*m[i-1])*(x[i]-k)/h[i]
                res += (y[i]-h[i]**2/6*m[i])*(k-x[i-1])/h[i]
                return res
        
        return None
    
    return compute

def cubic_spline_with_1(x,y,l=0,r=0,n=None,solve=sle.lu_solve):
    if n is None:
        n = len(x)

    mu,lam,d,h = compute_lists(x,y,n)
    lam[0] = 1
    d[0] = 6/h[1]*((y[1]-y[0])/h[1]-l)
    d.insert(0,0)
    d.append(6/h[n]*(r-(y[n]-y[n-1])/h[n]))

    mat = globals.zeros(n+1,n+1)
    for i in range(1,n+2):
        for j in range(1,n+2):
            if i==j:
                mat[i][j] = 2
            elif i == j+1:
                if i == n+1:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mu[i-1]
            elif i == j-1:
                mat[i][j] = lam[j-2]
    

    m = solve(mat,d)
    

    def compute(k):
        for i in range(2,n+1):
            if k >= x[i-1] and k <= x[i]:
                res = (x[i]-k)**3/6/h[i]*m[i-1]
                res += (k-x[i-1])**3/6/h[i]*m[i]
                res += (y[i-1]-h[i]**2/6*m[i-1])*(x[i]-k)/h[i]
                res += (y[i]-h[i]**2/6*m[i])*(k-x[i-1])/h[i]
                return res
        
        return None

    return compute


    