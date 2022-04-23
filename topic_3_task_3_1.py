import numpy as np


def pol_sys(r, a):
    x = r * np.cos(np.radians(a))
    y = r * np.sin(np.radians(a))
    return x, y


try:
    coord = [float(i) for i in input('введите полярные координаты через пробел(угол в градусах): ').split()]
    m = pol_sys(*coord)
    print(f'в декартовой системе координат ({round(m[0], 2)}, {round(m[1], 2)})')
except ValueError:
    print('ошибка ввода')