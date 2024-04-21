import math


"""
Реализация аддитивного метода генерации псевдослучайных чисел
"""

def add_rand_method(m : int, modulus: int, k : int, l : int, x0 : list, size = 10000):
    n = len(x0) - 1
    if size == 1:
        return math.ceil(math.fmod((x0[n - k] + x0[n - l]), modulus))
    r = x0.copy()
    r.extend([0 for _ in range(0, size)])
    for _ in range(0, size):
        r[n + 1] = math.ceil(math.fmod((r[n - k] + r[n - l]), modulus))
        n += 1
    return [r[i] % m for i in range(l, len(r))]
