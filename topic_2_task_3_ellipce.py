import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
a = 5
b = 2
x = np.linspace(-a, a, 1000)
y1 = [sqrt((1 - i**2 / a**2) * b**2) for i in x]
y2 = [-sqrt((1 - i**2 / a**2) * b**2) for i in x]
plt.xlim(-a - 1, a + 1)
plt.ylim(-a - 1, a + 1)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

