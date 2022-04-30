import numpy as np
from matplotlib import pyplot as plt
n = 100
r = 0.68
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
a = (sum(x) * sum(y) - n * sum(x * y)) / (sum(x) * sum(x) - n * sum(x * x))
b = (sum(y) - a * sum(x)) / n
x1 = [0, 1]
y1 = [a * i + b for i in x1]
plt.plot(x1, y1)
plt.show()
R = sum((x - (sum(x)/len(x)))*(y - (sum(y)/len(y)))) / (sum((x - (sum(x)/len(x)))**2) * sum((y - (sum(y)/len(y)))**2))**(0.5)
print('коэффициент корреляции R =', round(R, 5))