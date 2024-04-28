"""
Реализация вихря Мерсена метода генерации псевдослучайных чисел
"""

p, w, r, q = 624, 32, 31, 397
u = 1 << (w - r)
h = (1 << (r + 1)) - 1
a, b, c = 0x9908B0DF, 0x9D2C5680, 0xEFC60000
s = 7
t = 15
l = 18

def mt_rand_method(m : int, modulus : int, seed : int, size = 10000):
    x = [0] * p
    x[0] = seed
    for i in range(1, p):
        x[i] = (69069 * x[i - 1]) & ((1 << w + 1) - 1)

    mta = [0, a]
    i = 0
    r = [0 for _ in range(size)]
    for j in range(size):
        y = (x[i] & u) | (x[(i + 1) % p] & h)

        x[i] = x[(i + q) % p] ^ (y >> 1) ^ mta[y & 1]

        y = x[i]
        y ^= y >> u
        y ^= (y << s) & b
        y ^= (y << t) & c

        i = (i + 1) % p

        r[j] = (y ^ (y >> l)) % m
    return r
