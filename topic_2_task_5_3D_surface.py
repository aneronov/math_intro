import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 1)
Y = np.arange(-10, 10.5, 1)
X, Y = np.meshgrid(X, Y)
Z1 = - X**2 - Y**2 / 5 - 125
Z2 = X**2 / 5 + Y**2 + 125
ax.plot_wireframe(X, Y, Z1)
ax.plot_wireframe(X, Y, Z2)
plt.show()

