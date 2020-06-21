## module neville
'''p = neville(xData,yData,x).
Evaluates the polynomial interpolant p(x) that passe
through the specified data points by Neville’s methoD'''
import numpy as np
def neville(xData,yData,x):
    m = len(xData) # number of data points
    y = yData.copy()
    for k in range(1,m):
        y[0:m-k] = ((x - xData[k:m])*y[0:m-k] + \
        (xData[0:m-k] - x)*y[1:m-k+1])/ \
        (xData[0:m-k] - xData[k:m])
    return y[0]


xData = np.array([-2.0,-0.1,-1.5,0.5, \
-0.6,2.2,1.0,1.8])
yData = np.array([2.2796,1.0025,1.6467,1.0635, \
1.0920,2.6291,1.2661,1.9896])

while True:
    try:
        x = eval(input("\nx ==> "))
    except SyntaxError: break
    print("y =",neville(xData,yData,x))
input("Finished. Press return to exit")