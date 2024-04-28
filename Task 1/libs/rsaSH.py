"""
Реализация RSA метода генерации псевдослучайных чисел
"""
import math

def ferma_factorization(n):
    if n & 1 == 0:
        return
    x = int(n ** 0.5) + 1
    y = 1
    result = x * x - y * y - n
    while result != 0:
        if result > 0:
            y += 1
        else:
            x += 1
        result = x * x - y * y - n
    return x + y, x - y

def RSA_rand_method(
        m: int,
        n: int,
        e: int,
        w: int,
        x: int,
        size: int = 10000
):
    if n < 100000000:
        p, q = ferma_factorization(n)
        f = (p - 1) * (q - 1)
        if e <= 1 or e >= f or math.gcd(e, f) != 1:
            raise Exception
    if x < 1 or x >= n:
        raise Exception
    r = []
    for _ in range(size):
        current = 0
        for l in range(w):
            x = (x ** e) % n
            current ^= (x & 1) << l
            print(bin(current))
        r.append(current % m)

    return r

