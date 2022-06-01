import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = np.linalg.qr(A)
print('матрица A:', A, sep='\n')
print('матрица Q:', Q, sep='\n')
print('матрица R:', R, sep='\n')
R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]
X1 = np.linalg.solve(R1, B1)
X=np.append(X1, 0)
print('одно из псевдорешений: ', X)
print('норма: ', np.linalg.norm(X))
X = np.linalg.lstsq(A,B, rcond=None)[0]
print(f'нормальное псевдорешение: {X}')
print('норма: ', np.linalg.norm(X))

