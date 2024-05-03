"""
Реализация RSA метода генерации псевдослучайных чисел
"""

def RSA_rand_method(
        m: int,
        n: int,
        e: int,
        w: int,
        x: int,
        size: int = 10000
):
    r = []
    for _ in range(size):
        current = 0
        for _ in range(w):
            x = pow(x, e, n)
            current <<= 1
            current ^= x & 1
        r.append(current % m)
    return r
