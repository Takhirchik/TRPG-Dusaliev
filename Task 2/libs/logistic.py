"""
Реализация логистического распределения c заданным интеравалом
"""
__all__ = ['ls']

import matplotlib.pyplot as m
from math import floor, ceil, log
from .uniform import _gen

def distribution(numbers, a, b):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    res = []
    for _ in range(len(numbers)):
        u = next(uni)
        if u == 0:
            res.append(0)
        else:
            res.append(a + b * log(u / (1 - u)))
    return res

def ls(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    return dist
