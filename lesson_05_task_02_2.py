import numpy as np
import matplotlib.pyplot as plt
a = np.random.randint(0, 100, 10)
sum_ = [0 for i in range(10)]
for i in range(10):
    for j in range(10):
        sum_[i] += np.random.choice(a)
plt.hist(sum_, bins=5)
plt.show()