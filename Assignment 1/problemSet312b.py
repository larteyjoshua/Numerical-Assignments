import numpy as np
import math
## module newtonPoly
'''p = evalPoly(a,xData,x).
Evaluates Newton’s polynomial p at x. The coefficient
vector {a} can be computed by the function ’coeffts’.
a = coeffts(xData,yData).
Computes the coefficients of Newton’s polynomial.'''
def evalPoly(a,xData,x):
    n = len(xData) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

def coeffts(xData,yData):
    m= 4 # Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a
xData = np.array([0,0.5,1,1.5,2,2.5,3])
yData = np.array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727])
a = coeffts(xData,yData)
print(" x yInterp")
print("-----------------------")
for x in [0]:
    y = evalPoly(a,xData,x)
    print('{:3.1f} {:9.5f}'.format(x,y))
input("\nPress return to exit")