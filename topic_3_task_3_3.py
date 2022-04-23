import numpy as np
import matplotlib.pyplot as plt


def pol_sys(r, a):
    x = r * np.cos(np.radians(a))
    y = r * np.sin(np.radians(a))
    return x, y


try:
    coord = [float(i) for i in input('введите полярные координаты 1й точки через пробел(угол в градусах): ').split()]
    a = list(pol_sys(*coord))
    coord = [float(i) for i in input('введите полярные координаты 2й точки через пробел(угол в градусах): ').split()]
    b = list(pol_sys(*coord))
    plt.plot([a[0], b[0]], [a[1], b[1]], marker="o")
    plt.show()
except ValueError:
    print('ошибка ввода')