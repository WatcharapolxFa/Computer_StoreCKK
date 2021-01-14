import numpy as np
from numpy.core.fromnumeric import argmin
X = np.array([[40, 150],
              [50, 130],
              [50, 170],
              [60, 160],
              [70, 140],
              [70, 180]])

Y = np.array(['N', 'Y', 'N', 'Y', 'Y', 'N'])
p = np.array([30, 145])
D = np.zeros(len(X))
for i, x in enumerate(X):
    D[i] = np.sqrt(np.sum((x-p)**2))
print(Y[D.argmin()])
