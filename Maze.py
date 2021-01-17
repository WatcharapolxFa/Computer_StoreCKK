import numpy as np
from matplotlib import pyplot as plt


def display(maze, i, j):
    img = np.zeros(*maze.shape, 3, dtype=np.uint8)
    img[maze == '0'] = 255
    img[i, j] = [255, 0, 0]
    img[maze == 'E'] = [0, 255, 0]
    plt.imshow(img)
    plt.axis('off')
    plt.pause(0.5)
    plt.cla()


maze = np.array([list('1E11111111111'),
                 list('1011111111111'),
                 list('10000000000S1'),
                 list('1111111111111')])

display(maze, 2, 11)
plt.show()
