import matplotlib.pyplot as plt
import numpy as np

def sigmoid(t):
    return 1/(1+np.exp(-t))

t2 = np.arange(-6.0, 6.0, 0.01)

plt.plot(t2, sigmoid(t2))
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.show()
