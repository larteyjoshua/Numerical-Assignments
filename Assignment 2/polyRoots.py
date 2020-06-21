## module evalPoly
''' p,dp,ddp = evalPoly(a,x).
Evaluates the polynomial
p = a[0] + a[1]*x + a[2]*xˆ2 +...+ a[n]*xˆn
with its derivatives dp = p’ and ddp = p’’
at x.
'''
def evalPoly(a,x):
    n = len(a) - 1
    p = a[n]
    dp = 0.0 + 0.0j
    ddp = 0.0 + 0.0j
    for i in range(1,n+1):
        ddp = ddp*x + 2.0*dp
        dp = dp*x + p
        p = p*x + a[n-i]
    return p,dp,ddp

    ## module polyRoots
''' roots = polyRoots(a).
Uses Laguerre’s method to compute all the roots of
a[0] + a[1]*x + a[2]*xˆ2 +...+ a[n]*xˆn = 0.
The roots are returned in the array ’roots’,
'''
import numpy as np
import cmath
from random import random

def polyRoots(a,tol=1.0e-12):

    def laguerre(a,tol):
        x = random()   # Starting value (random number)
        n = len(a) - 1
        for i in range(30):
            p,dp,ddp = evalPoly(a,x)
            if abs(p) < tol: return x
            g = dp/p
            h = g*g - ddp/p
            f = cmath.sqrt((n - 1)*(n*h - g*g))
            if abs(g + f) > abs(g - f): dx = n/(g + f)
            else: dx = n/(g - f)
            x = x - dx
            if abs(dx) < tol: return x
        print ('Too many iterations')

    def deflPoly(a,root):  # Deflates a polynomial
        n = len(a)-1
        b = [(0.0 + 0.0j)]*n
        b[n-1] = a[n]
        for i in range(n-2,-1,-1):
            b[i] = a[i+1] + root*b[i+1]
        return b

    n = len(a) - 1
    roots = zeros((n),dtype=Complex)
    for i in range(n):
        x = laguerre(a,tol)
        if abs(x.imag) < tol: x = x.real
        roots[i] = x
        a = deflPoly(a,x)
    return roots
