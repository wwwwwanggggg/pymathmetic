from math import *
import globals
import numerical_diff as nd


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
    while True:
        x = x - f(x)/nd.extrapolation(f,x,h=0.5)
        if abs(x-last) < eps:
            return x
        
        last = x


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