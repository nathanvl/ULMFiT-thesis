import matplotlib.pyplot as plt
import numpy as np

def tanh(t):
    return((1-np.exp(-2*t)) / (1 + np.exp(-2*t)))

t2 = np.arange(-6.0, 6.0, 0.01)

plt.plot(t2, tanh(t2))
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.show()
