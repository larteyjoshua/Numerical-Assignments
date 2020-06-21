import math
def f(x): return x**2 -2 
def df(x): return 2*x
def newtonRaphson(x,tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i
print ('Too many iterations\n')
root,numIter = newtonRaphson(math.sqrt(2))
print ('Root =',root)
print ("Number of iterations =",numIter)
input("Press return to exit")