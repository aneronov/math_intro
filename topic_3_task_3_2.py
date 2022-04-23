import numpy as np
import matplotlib.pyplot as plt
try:
    r = float(input('введите радиус круга: '))
    a = np.linspace(0, 2 * np.pi, 3600)
    for i in a:
        plt.polar(i, r, 'b.')
    # 2й вариант
    r_ = [2 * r] * 3600
    plt.polar(a, r_, 'r.')
    plt.show()
except ValueError:
    print('ошибка ввода')

