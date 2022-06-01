import numpy as np
A = [[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]]
B = [1, 7, 12, 7, 15]
X = np.linalg.lstsq(A, B, rcond=None)
print('псевдорешение для:')
print('x + 2y – z = 1',
      '3x – 4y = 7',
      '8x – 5y + 2z = 12',
      '2x – 5z = 7',
      '11x +4y – 7z = 15', sep='\n')
print(f'является: x={X[0][0]}; y={X[0][1]}; z={X[0][2]}')
