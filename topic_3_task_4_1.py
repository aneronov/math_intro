import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def sys_eq(p):
    x, y = p
    return (np.exp(x) + x * (1 - y) - 1, x**2 - y - 1)

xx = np.arange(-5, 5, 0.01)
yy1 = (np.exp(xx) + xx - 1) / xx
yy2 = xx**2 - 1
plt.plot(xx, yy1)
plt.plot(xx, yy2)
plt.show()
x1, y1 = fsolve(sys_eq, (-2, 3))
x2, y2 = fsolve(sys_eq, (2, 5))
x3, y3 = fsolve(sys_eq, (4, 15))
print(f'корни системы уравнений: exp(x)+x*(1-y)=1 и y=x^2-1:')
print('x1 =',x1)
print('y1 =',y1)
print('x2 =',x2)
print('y2 =',y2)
print('x3 =',x3)
print('y3 =',y3)