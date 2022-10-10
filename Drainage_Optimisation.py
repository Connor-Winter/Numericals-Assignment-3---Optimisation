import matplotlib.pyplot as plt
import numpy as np

#define function
def elavation_func(x):
    return x**2*(3*np.cos(3*x)+np.sin(x**2))

#plot points
x = np.arange(0,4,0.01)
elavs = elavation_func(x)

#plot
plt.plot(x, elavs)
plt.grid(True)
plt.show()
