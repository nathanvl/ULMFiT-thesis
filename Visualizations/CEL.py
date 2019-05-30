import matplotlib.pyplot as plt
import numpy as np

def cel(t):
    return(-1*np.log(t))

t2 = np.arange(0, 1.0, 0.01)

plt.plot(t2, cel(t2))
plt.xlabel(r'$y_{pred}$')
plt.ylabel(r'Cross-Entropy Loss($y_{actual}$=1,$y_{pred}$ )')
plt.show()
