import numpy as np


def display(p):
    print = (p.reshape((3, 3)))


def fitness(p):
    p = p.reshape((3, 3))
    sum_rows = p.sum(axis=0)
    sum_cols = p.sum(axis=1)
    sum_diag = [np.sum(np.diag(p)), np.sum(np.diag(np.fliplr(p)))]
    sum_all = np.concatenate((sum_rows, sum_cols, sum_diag))
    return len(np.unique(sum_all))


p = np.arange(1, 10)
display(p)
print(fitness(p))
