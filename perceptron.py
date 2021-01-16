import numpy as np
X = np.array({[1, 2], [2.5, 3], [3, 1], [-3, -1.7], [-1.6, -3], [1.5, -3]})
T = [1, 1, 1, -1, -1, -1]
W = X[1].copy()
done = False
while not done:
    done = True
    for i, x in enumerate(X):
        if T[i]*np.dot(x, W) < 0:
            W += x
            done = False
for x in X:
    print(np.dot(W, x))
