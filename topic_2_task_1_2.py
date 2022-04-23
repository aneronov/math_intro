from math import sqrt
try:
    vctr = [float(i) for i in input('введите координаты вектора через пробел: ').split()]
    sum_ = 0
    for i in vctr:
        sum_ += i ** 2
    print('длина указанного вектора =', round(sqrt(sum_), 2))
except (TypeError, ValueError):
    print('неправильный ввод данных')

