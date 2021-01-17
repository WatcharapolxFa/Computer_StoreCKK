import numpy as np
from matplotlib import pyplot as plt
n = 100000
rocks = np.random.rand(n, 2)
plt.plot(rocks[:, 0], rocks[:, 1], '.')
j = []
for i, rock in enumerate(rocks):
    if rock[0]**2+rock[1]**2 <= 1:
        j.append(i)
j = np.array(j)
pi = 4 * len(j)/n
print(pi)
plt.plot(rocks[j, 0], rocks[j, 1], '.r')
plt.axis('equal')
plt.axis('off')
plt.show()
