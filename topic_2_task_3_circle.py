import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
r = 5
x = np.linspace(-r, r, 1000)
y1 = [sqrt(r**2 - i**2) for i in x]
y2 = [-sqrt(r**2 - i**2) for i in x]
plt.figure(figsize=(6, 6))
plt.xlim(-r - 1, r + 1)
plt.ylim(-r - 1, r + 1)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

