from numpy import cos, arccos, linspace

def f(x): return cos( 2 * arccos(x) )

a = -1.
b = +1.

nPanels = [2,4,6]

Is = [] 
for np in nPanels:
    assert np % 2 == 0, 'number of panels must be even'
    xs = linspace( a, b, np+1 )
    I = 0.

    # for each group of two panels accumulate the contribution to the integral I using Simpson's 1/3 rule
    h = (b-a)/np
    for cpi in range(int(np/2)): # cpi = center panel index
        ci = 2*cpi+1 # ci = center index so that (ci-1, ci, ci+1) specify the left end point, center point, and right end point 
        I += (h/3.) * ( f(xs[ci-1]) + 4*f(xs[ci]) + f(xs[ci+1]) )
    Is.append(I)

print ("nPanels= ", nPanels)
print ("Integrals= ", Is)