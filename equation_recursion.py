from math import *
import globals
import numerical_diff as nd
import matrix_norm as matn

def bisection(f,a,b,eps=1e-5):
    last = None
    l = a
    r = b
    while True:
        fl = f(l)
        fr = f(r)
        fm = f((l+r)/2)
        if last is not None and abs(last-fm)<eps:
            return (l+r)/2
        last = fm

        if globals.sgn(fl) == globals.sgn(fm):
            l = (l+r)/2
        else:
            r = (l+r)/2


def recursion(g:callable,x,eps=1e-5):
    last = x
    while True:
        x = g(x)
        if abs(x-last) < eps:
            return x
        last = x


def Newton(f:callable,x,eps=1e-5):
    last = x

    def g(x):
        return x-f(x)/nd.extrapolation(f,x,h=0.5)
    return recursion(g,x,eps)


# 不可用
def Newton_downhill(f:callable,x,lam=None,eps=1e-5):
    if lam is None:
        lam = 1
        last = x
        x = x- lam*f(x)/nd.extrapolation(f,x,h=0.5)
        while x >= last:
            lam /= 2
            x = x- lam*f(x)/nd.extrapolation(f,x,h=0.5)
    
    last = x
    while True:
        x = x - lam*f(x)/nd.extrapolation(f,x,h=0.5)
        if abs(x-last) < eps:
            return x
        
        last = x


def secant(f:callable,x0,x1,eps=1e-5):
    last = x1
    while True:
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        if abs(x-last) < eps:
            return x
        last = x
        x0 = x1
        x1 = x


def non_linear_equation_recursion(f,x,n=None,norm=matn.v_p_norm,eps=1e-5):
    if n is None:
        n = len(f)-1

    last = x
    while True:
        for i in range(1,n+1):
            x[i]= f[i](x)

        if abs(norm(x)-norm(last)) < eps:
            return x
    
        last = x





