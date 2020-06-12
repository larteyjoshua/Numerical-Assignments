import error
    
## module swap
'''swapRows(v,i,j).
Swaps rows i and j of a vector or matrix [v].
swapCols(v,i,j).
Swaps columns of matrix [v].
'''
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]
    
## module gaussPivot
'''x = gaussPivot(a,b,tol=1.0e-12).
Solves [a]{x} = {b} by Gauss elimination with
scaled row pivoting'''
import numpy as np

def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)
    # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
    for k in range(0,n-1):
        # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: error.err('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
        # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1,n-1]) < tol: error.err('Matrix is singular')
    # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

## module polyFit
'''c = polyFit(xData,yData,m).
Returns coefficients of the polynomial
p(x) = c[0] + c[1]x + c[2]xˆ2 +...+ c[m]xˆm
that fits the specified data in the least
squares sense.
sigma = stdDev(c,xData,yData).
Computes the std. deviation between p(x)
and the data.'''
import numpy as np
import math

def polyFit(xData,yData,m):
    a = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]
    return gaussPivot(a,b)
def stdDev(c,xData,yData):
    def evalPoly(c,x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p
    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c,xData[i])
        sigma = sigma + (yData[i] - p)**2
    sigma = math.sqrt(sigma/(n - m))
    return sigma


xData = np.array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
yData = np.array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])
while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        coeff = polyFit(xData,yData,m)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
        print(coeff[0])
        print(coeff[1])
        x=2000
        y= coeff[0]+(coeff[1]*x)
        print("The Thermal Efficiency at x=2000 is:\n",y)
    except SyntaxError: break
input("Finished. Press return to exit")