from numpy import asarray

vs = [ 0, 1.0, 1.8, 2.4, 3.5, 4.4, 5.1, 6.0 ]
Ps = [ 1.e-6, 4.7, 12.2, 19.0, 31.8, 40.1, 43.8, 43.2 ] # note Ps[0] is very small to make vs[0]/Ps[0] defined 

nPanels = len(vs)-1

I = 0.
for ii in range(1,nPanels+1):
    I += 0.5 * ( vs[ii] - vs[ii-1] ) * ( vs[ii-1] / Ps[ii-1] + vs[ii] / Ps[ii] )
print( "I= ", I )
# m=2000kg
m=2000
t= m*I
print("t= ", t)