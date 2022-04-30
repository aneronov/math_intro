import numpy as np
a = [0 for i in range(37)]
for i in range(1000):
    b = np.random.randint(0, 37)
    a[b] += 1
p1 = sum(a) / 1000
p2 = 0
for i in range(len(a)):
    p2 += a[i] / 1000
print(f'вероятность суммы выпадания полей рулетки {p1:.1f} равна сумме вероятностей выпадания каждого поля рулетки {p2:.1f}')