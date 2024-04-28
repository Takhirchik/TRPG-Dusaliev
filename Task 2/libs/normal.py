"""
Реализация нормального распределения
"""
__all__ = ['nr', 'distribution']

import matplotlib.pyplot as m
from math import floor, ceil, sqrt, cos, sin, log, pi
from .uniform import _gen

def distribution(numbers, mu, si):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    res = []
    i = 0
    while i <= len(numbers) - 2:
        u1, u2 = next(uni), next(uni)
        res.append((mu + si * sqrt(-2 * log(1 - u1)) * cos(2 * pi * u2)))
        res.append((mu + si * sqrt(-2 * log(1 - u1)) * sin(2 * pi * u2)))
        i += 2
    return res

def nr(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, mu=p1, si=p2)
    return dist
