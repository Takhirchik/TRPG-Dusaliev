"""
Реализация логнормального распределения c заданным интеравалом
"""
__all__ = ['ln']

from math import floor, ceil, e
from .normal import distribution as d

def distribution(numbers, a, b):
    dist = d(numbers=numbers, mu=0, si=1)
    return [a + e ** (b - dist[i]) for i in range(len(dist))]

def ln(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    l = [floor(x * 100000) % 100000 if x > 0 else ceil(x * 100000) % 100000 for x in dist]
    return dist
