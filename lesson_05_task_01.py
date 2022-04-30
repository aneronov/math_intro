import numpy as np
try:
    print('игра в рулетку')
    n = int(input('введите кол-во попыток: '))
    for i in range(n):
        a = input('для продолжения нажмите "Enter".')
        print('выпало поле', np.random.randint(0, 37))
except (TypeError, ValueError):
    print('ошибка ввода')