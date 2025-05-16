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

    def output(self):
        for i in range(len(self.xs)):
            print(f"x:{self.xs[i]:<10},y:{self.table[i]}")
    
    def __call__(self,x):
        temp = 0
        for i in range(len(self.xs)):
            tt = self.table[i][i]
            for j in range(i):
                tt *= x-self.xs[j]
            temp += tt
        
        return temp

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


def Hermite(xs,ys,n=None,h=None):
    if n is None:
        n = len(xs)

    if not isinstance(h,Hermite_func):
        h = Hermite_func()
    
    for i in range(n):
        h.add_point(xs[i],ys[i])
    
    return h
    
