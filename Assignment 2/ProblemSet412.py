
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,num=100)
fx=[]
for i in range(len(x)):
    fx.append(x[i]**3 - 3.23*x[i]**2+ 5.54*x[i] + 9.84) #x**3 - 3.23*x**2 - 5.54*x + 9.84


plt.plot(x,fx)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()
## module bisection
''' root = bisection(f,x1,x2,switch=0,tol=1.0e-9).
Finds a root of f(x) = 0 by bisection.
The root must be bracketed in (x1,x2).
Setting switch = 1 returns root = None if
f(x) increases upon bisection.
'''
import math
import error
from numpy import sign

def bisection(f,x1,x2,switch=1,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    if sign(f1) == sign(f2):
        error.err('Root is not bracketed')
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))

    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) \
                         and (abs(f3) > abs(f2)):
            return None
    if f3 == 0.0: return x3
    if sign(f2)!= sign(f3): x1 = x3; f1 = f3
    else: x2 = x3; f2 = f3
    return (x1 + x2)/2.0

def f(x): return x**3 - 3.23*x**2 - 5.54*x + 9.84
x = bisection(f, 1, 2, tol = 1.0e-9)
print('x =', '{:6.4f}'.format(x))
input("Press return to exit")