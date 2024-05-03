"""
Реализация Блюма-Блюма-Шуба метода генерации псевдослучайных чисел
"""
import math

p, q, n = 127, 131, 16637

def bbs_rand_method(m: int, x: int, size: int = 10000):
    if math.gcd(x, n) != 1 or x < 1 or x >= n:
        raise Exception
    r = []
    for _ in range(size):
        current = 0
        for _ in range(n.bit_length()):
            x = pow(x, 2, n)
            current <<= 1
            current ^= (x & 1)
        r.append(current % m)
    return r
