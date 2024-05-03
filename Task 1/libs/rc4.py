"""
Реализация линейно-конгруэтного метода генерации псевдослучайных чисел
"""

def rc4_rand_method(m : int, K : list[int], size=10000):
    if len(K) != 256:
        raise Exception
    s = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + s[i] + K[i]) % 256
        s[i], s[j] = s[j], s[i]

    i = j = 0
    r = [0 for _ in range(size)]
    for d in range(size):
        k, l = 0, 0
        for _ in range(2):
            k = l
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            t = (s[i] + s[j]) % 256
            l = s[t]
        r[d] = int(str(l) + str(k)) % m
    return r
