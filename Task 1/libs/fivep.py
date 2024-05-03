"""
Реализация пятипараметрического метода генерации псевдослучайных чисел
"""

def five_P_rand_method(m : int, p : int,  q1 : int, q2 : int, q3 : int, w : int, seed : str, size=10000):
    sr = seed
    r = [0 for _ in range(size)]
    for i in range(size):
        for _ in range(w):
            xor = ((sr >> q1) ^ (sr >> q2) ^ (sr >> q3) ^ (sr & 1)) & 1
            r[i] <<= 1
            r[i] ^= sr & 1
            sr >>= 1
            sr |= xor << (p - 2)
        r[i] %= m
    return r
