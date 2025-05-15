import globals
import solve_liner_equations as sle

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
            print(f"x:{self.xs[i]:<10},y:{" ".join([str(j) for j in self.table[i]])}")
    
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

    f = Newton_func()


    

