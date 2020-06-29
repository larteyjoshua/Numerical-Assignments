## module trapezoid
''' Inew = trapezoid(f,a,b,Iold,k).
Recursive trapezoidal rule:
old = Integral of f(x) from x = a to b computed by
trapezoidal rule with 2ˆ(k-1) panels.
Inew = Same integral computed with 2ˆk panels.
'''
import math
def trapezoid(f,a,b,Iold,k):
    if k == 1:Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k -2 ) # Number of new points
        h = (b - a)/n # Spacing of new points
        x = a + h/2.0
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        Inew = (Iold + h*sum)/2.0
    return Inew
