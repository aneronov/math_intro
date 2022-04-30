import numpy as np
from math import factorial
k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(n):
    if x[i] == 2:
        k += 1
print('значение по методу Монте-Карло:', k/n)
print('значение через биномиальное распределение', (factorial(4))/(factorial(2) * factorial(4 - 2)) * (1/2)**2 * (1/2)**(4 - 2))