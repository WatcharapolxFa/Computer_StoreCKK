import numpy as np
from matplotlib import pyplot as plt
n = 100
x = np.random.rand(n)
y = 5*x**2 - 2*x+10 + 0.4*np.random.rand(n)
plt.plot(x, y, '.')

X = np.vstack((x**2, x, np.ones(n))).T
W = np.linalg.inv(X.T @ X) @ X.T @ y
print(W)
z = X @ W
plt.plot(X, z, '.r')

plt.show()
