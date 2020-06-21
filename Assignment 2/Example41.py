## module rootsearch
'''x1,x2 = rootsearch(f,a,b,dx).
Searches the interval (a,b) in increments dx fo
the bounds (x1,x2) of the smallest root of f(x)
Returns x1 = x2 = None if no roots were detecte
'''

from numpy import sign
def rootsearch(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while sign(f1) == sign(f2):
        if x1 >= b: return None,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2


def f(x): return x**3 - 10.0*x**2 + 5.0
x1 = 0.0; x2 = 1.0
for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = rootsearch(f,x1,x2,dx)
x = (x1 + x2)/2.0
print('x =', '{:6.4f}'.format(x))
input("Press return to exit")