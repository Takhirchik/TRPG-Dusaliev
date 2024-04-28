import math

"""
Реализация линейно-конгруэтного метода генерации псевдослучайных чисел
"""

def linear_rand_method(m : int, modulus : int, a : int, c : int, seed, size=10000):
    sr = seed
    if size == 1:
        return math.ceil(math.fmod(a * math.ceil(sr) + c, modulus))
    r = [0 for _ in range(size + 1)]
    r[0] = math.ceil(sr)
    for i in range(1, size + 1):
        r[i] = math.ceil(math.fmod((a * r[i - 1] + c), modulus))
    return [r[i] % m for i in range(1, size + 1)]
