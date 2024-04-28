"""
Реализация биномиального распределения c заданным интеравалом
"""

__all__ = ['bi']

from math import comb
from .uniform import _gen

def distribution(numbers, p, n):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    res = []
    for _ in range(len(numbers)):
        k, accum = 0, 0
        u = next(uni)
        while accum < u:
            accum += comb(n, k) * pow(p, k) * pow(1 - p, n - k)
            k += 1
        res.append(k)
    return res

def bi(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, p=p1, n=p2)
    return dist
