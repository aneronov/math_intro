import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10.5, 1)
Y = np.arange(-10, 10.5, 1)
X, Y = np.meshgrid(X, Y)
Z1 = X - Y + 15
Z2 = X - Y - 15
ax.plot_wireframe(X, Y, Z1)
ax.plot_wireframe(X, Y, Z2)
plt.show()

