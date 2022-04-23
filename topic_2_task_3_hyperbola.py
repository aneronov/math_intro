import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
a = 5
b = 2
x1 = np.linspace(a, 2 * a, 1000)
x2 = np.linspace(-a, 2 * (-a), 1000)
y1 = [sqrt((i**2 / a**2 - 1) * b**2) for i in x1]
y2 = [-sqrt((i**2 / a**2 - 1) * b**2) for i in x1]
y3 = [sqrt((i**2 / a**2 - 1) * b**2) for i in x2]
y4 = [-sqrt((i**2 / a**2 - 1) * b**2) for i in x2]
plt.plot(x1, y1, x1, y2, x2, y1, x2, y2)
plt.show()

