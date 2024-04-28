"""
Реализация логнормального распределения c заданным интеравалом
"""
__all__ = ['ln']

from math import e
from .normal import distribution as d

def distribution(numbers, a, b):
    dist = d(numbers=numbers, mu=0, si=1)
    return [a + e ** (b - dist[i]) for i in range(len(dist))]

def ln(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    return dist
