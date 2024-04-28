"""
Реализация экспоненциального распределения
"""
__all__ = ['ex']

import matplotlib.pyplot as m
from math import floor, ceil, log
from .uniform import _gen

def distribution(numbers, a, b):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    res = []
    for _ in range(len(numbers)):
        x = next(uni)
        if x == 0:
            res.append(0)
        else:
            res.append(a - b * log(x))
    return res

def ex(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    return dist
