import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,num=15)
fx=[]
for i in range(len(x)):
    fx.append(x[i]**3 - 3.23*x[i]**2+ 5.54*x[i] + 9.84) #x**3 - 3.23*x**2 - 5.54*x + 9.84


plt.plot(x,fx)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()