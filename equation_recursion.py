from math import *
import globals


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