"""
Реализация нелинейной комбинации РСЛОС метода генерации псевдослучайных чисел
"""

def excep(R : str):
    for s in R:
        if s != '0':
            if s != '1':
                raise Exception

def nfsr_rand_method(m : int,
                     R1 : str,
                     R2 : str,
                     R3 : str,
                     w : int,
                     x1 : int,
                     x2 : int,
                     x3 : int,
                     size : int = 10000):
    r = [0 for _ in range(size)]
    excep(R1)
    excep(R2)
    excep(R3)
    R1_coeff = [i for i in range(len(R1) - 1, -1, -1) if R1[i] == '1']
    R2_coeff = [i for i in range(len(R2) - 1, -1, -1) if R2[i] == '1']
    R3_coeff = [i for i in range(len(R3) - 1, -1, -1) if R3[i] == '1']
    for i in range(size):
        xor1, xor2, xor3 = 0, 0, 0
        current = 0
        for _ in range(w):
            n = max(len(R1_coeff), len(R2_coeff), len(R3_coeff))
            for j in range(n):
                if j < len(R1_coeff):
                    xor1 ^= x1 >> R1_coeff[j]
                if j < len(R2_coeff):
                    xor2 ^= x2 >> R2_coeff[j]
                if j < len(R3_coeff):
                    xor3 ^= x3 >> R3_coeff[j]
            x1 >>= 1
            x2 >>= 1
            x3 >>= 1
            x1 |= (xor1 & 1) << (R1_coeff[0] - 1)
            x2 |= (xor2 & 1) << (R2_coeff[0] - 1)
            x3 |= (xor3 & 1) << (R3_coeff[0] - 1)
            output_bit = ((x1 & x2) ^ (x2 & x3) ^ x3) & 1
            current <<= 1
            current ^= output_bit
        r[i] = current % m
    return r
