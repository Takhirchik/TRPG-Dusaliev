"""
Реализация гамма-распределения, где c = k
"""
__all__ = ['gm']

from math import log
from .uniform import _gen

def distribution(numbers, a, b, c):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    res = []
    i = 0
    while i < len(numbers) - c + 1:
        j = 1
        for k in range(c):
            j *= (1 - next(uni))
        x = a - b * log(j)
        res.append(x)
        i += c
    return res

def gm(numbers : list,
       p1,
       p2,
       p3):
    dist = distribution(numbers=numbers, a=p1, b=p2, c=p3)
    return dist
