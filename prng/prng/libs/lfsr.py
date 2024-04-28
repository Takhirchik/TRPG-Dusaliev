"""
Реализация РСЛОС метода генерации псевдослучайных чисел
"""

def excep(R : str):
    for s in R:
        if s != '0':
            if s != '1':
                raise Exception

def lfsr_rand_method(m : int, c_vec : str, seed : str, size=10000):
    excep(c_vec)
    excep(seed)
    sr = int(seed, 2)
    xor = 0
    r = [0 for _ in range(size)]
    c = [i for i in range(len(c_vec) - 1, -1, -1) if c_vec[i] != '0']
    for i in range(size):
        current = 0
        for _ in range(2 ** (c[0] - 1)):
            for ch in c:
                xor ^= (sr >> ch)
            current <<= 1
            current ^= (sr & 1)
            sr >>= 1
            sr |= (xor & 1) << (c[0] - 1)
            xor = 0
        r[i] = current % m
    return r
