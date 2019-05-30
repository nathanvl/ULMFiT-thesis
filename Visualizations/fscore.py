import matplotlib.pyplot as plt
import numpy as np

# generate 2 2d grids for the x & y bounds
amount = 200
y, x = np.meshgrid(np.linspace(0, 1, amount), np.linspace(0, 1, amount))

z = 2*(y*x)/(y+x)
# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = 0,1

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('F-score')
plt.xlabel('Precision')
plt.ylabel('Recall')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
plt.savefig('images/fscore.pdf')
plt.show()
