import numpy as np
from matplotlib import pyplot as plt


def display(maze, i, j):
    img = np.zeros((*maze.shape, 3), dtype=np.uint8)
    img[maze == '0'] = 255
    img[maze == '.'] = [255, 200, 200]
    img[maze == 'E'] = [0, 255, 0]
    img[i, j] = [255, 0, 0]
    plt.imshow(img)
    plt.axis('off')
    plt.pause(0.5)
    plt.cla()


maze = np.array([list('1E111111111'),
                 list('10110010001'),
                 list('10100100101'),
                 list('10110010101'),
                 list('10100010101'),
                 list('100010001S1'),
                 list('11111111111')])

stack = []
start = np.where(maze == 'S')
i, j = start[0][0], start[1][0]
display(maze, i, j)
path = []
while maze[i, j] != 'E':
    maze[i, j] = '.'
    path.append([i, j])
    for m, n in zip([i-1, i, i+1, i], [j, j-1, j, j+1]):
        if maze[m, n] == '0' or maze[m, n] == 'E':
            stack.append([m, n])
    if len(stack) > 0:
        i, j = stack.pop()
    else:
        print('Cannot exit! ')
        break
    display(maze, i, j)
plt.show()
