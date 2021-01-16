import numpy as np


def display(p):
    print = (p.reshape((3, 3)))


def fitness(p):
    p = p.reshape((3, 3))
    sum_rows = p.sum(axis=0)
    sum_cols = p.sum(axis=1)
