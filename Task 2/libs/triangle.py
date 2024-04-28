"""
Реализация треугольного распределения
"""
__all__ = ['tr']

from .uniform import _gen

def distribution(numbers, a, b):
    res = []
    m = max(numbers) + 1
    uni = _gen(numbers=numbers, m=m)
    i = 0
    while i <= len(numbers) - 2:
        u1, u2 = next(uni), next(uni)
        res.append(a + b * (u1 + u2 - 1))
        i += 2
    return res

def tr(numbers : list,
       p1,
       p2):
    dist = distribution(numbers=numbers, a=p1, b=p2)
    return dist
