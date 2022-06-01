import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def Q(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)


fig = figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-50, 50, 0.5)
Y = np.arange(-50, 50, 0.5)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Q(X, Y, X + 2*Y - 1))
ax.plot_surface(X, Y, Q(X, Y, 6 - 4*X + 2.5*Y))
A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
print(f'Ответ: {np.linalg.lstsq(A,B, rcond=None)[0]}')
show()