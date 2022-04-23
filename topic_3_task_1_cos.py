import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 300)
k = [1, 4, 7]
a = [2, 5, 3]
b = [-5, 3, 20]
y1 = k[0] * np.cos(x - a[0]) + b[0]
y2 = k[1] * np.cos(x - a[1]) + b[1]
y3 = k[2] * np.cos(x - a[2]) + b[2]
plt.plot(x, y1, x, y2, x, y3)
plt.grid()
plt.show()