import numpy as np
from scipy.optimize import fsolve


def sys_eq(p):
    x, y = p
    return (np.exp(x) + x * (1 - y) - 1, x**2 - y - 1)


x1, y1 = fsolve(sys_eq, (-2, 3))
x2, y2 = fsolve(sys_eq, (2, 5))
x3, y3 = fsolve(sys_eq, (4, 15))

print(f'корни системы неравенства и уравнения: exp(x)+x*(1-y)-1>0 и y=x^2-1:')
print('x1 =',x1)
print('y1 =',y1)
x = x1 - 0.1
y = y1 - 0.1
if np.exp(x) + x * (1 - y) - 1 > 0:
    print('x1, y1 являются корнями системы.')
else:
    print('x1, y1 не являются корнями системы, так как не удовлетворяют условию неравенства exp(x)+x*(1-y)-1>0')
print('x2 =',x2)
print('y2 =',y2)
x = (x1 + x2) / 2
y = (y1 + y2) / 2
if np.exp(x) + x * (1 - y) - 1 > 0:
    print('x2, y2 являются корнями системы.')
else:
    print('x2, y2 не являются корнями системы, так как не удовлетворяют условию неравенства exp(x)+x*(1-y)-1>0')
print('x3 =',x3)
print('y3 =',y3)
x = x3 + 0.1
y = y3 + 0.1
if np.exp(x) + x * (1 - y) - 1 > 0:
    print('x3, y3 являются корнями системы.')
else:
    print('x3, y3 не являются корнями системы, так как не удовлетворяют условию неравенства exp(x)+x*(1-y)-1>0')
