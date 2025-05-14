import globals
import solve_liner_equations as sle


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
    

def lagrange(xs,ys,n=None):
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

