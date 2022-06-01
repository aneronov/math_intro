import numpy as np
A = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
B = [12, 2, 1]
X = np.linalg.solve(A, B)
print('Решением линейной системы типа А*Х=В, где:')
print('A=')
for i in range(len(A)):
    print(*A[i])
print()
print('B=')
print(*B, sep='\n')
print()
print('является Х=')
print(*X, sep='\n')
