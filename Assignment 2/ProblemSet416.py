
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,num=100)
fx=[]
for i in range(len(x)):
    fx.append((math.sin(x[i])) + (3*math.cos(x[i])) -2) #math.sin(x) + 3*math.cos(x)-2


plt.plot(x,fx)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()
## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol=1.0e-9).
Finds a root of f(x) = 0 by combining the Newton-Raphson
method with bisection. The root must be bracketed in (a,b).
Calls user-supplied functions f(x) and its derivative df(x).
'''

import error
from numpy import sign

def newtonRaphson(f,df,a,b,tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): error.err('Root is not bracketed')
    x = 0.5*(a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
        # Tighten the brackets on the root
        if sign(fa) != sign(fx): b = x
        else: a = x
        # Try a Newton-Raphson step
        dfx = df(x)
        # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
        # If the result is outside the brackets, use bisection
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b - a)
            x = a + dx
        # Check for convergence
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')


def f(x): return math.sin(x) + 3*math.cos(x)-2
def df(x): return math.cos(x) - 3*math.sin(x)
print("Leftmost roots")
print("root =", newtonRaphson(f,df,-1,0,tol=1.0e-9))
print("Rightmost roots")
print("root =", newtonRaphson(f,df,1,2,tol=1.0e-9))
input("Press return to exit")