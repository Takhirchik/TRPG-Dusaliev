"""
Реализация стандартного равномерного распределения c заданным интервалом
"""
__all__ = ['st']

import matplotlib.pyplot as mt
from math import floor, fabs
from .uniform import _gen

def distribution(numbers, a, b):
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    return [b * next(uni) + a for _ in range(len(numbers))]

def st(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    return dist
