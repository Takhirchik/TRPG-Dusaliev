from libs import LC, add, lfsr, fivep, nfsr, mt, rc4, rsaSH, bbs
import argparse as ag
import sys
import os.path

class NotEnoughParameters(Exception):
    pass

class NoneMethod(Exception):
    pass

def formatter_par(args : list):
    l = []
    k = 1
    for arg in args:
        if len(l) < k:
            l.append(arg)
        else:
            if arg == ',':
                k += 1
                continue
            else:
                l[k - 1] += arg
    return l

def call(args):
    if args.i == []:
        help_g = "Code of method"
        help_g += "\n   lc - parameters mod - integer, a - integer, c - integer, seed - integer"
        help_g += "\n   add - parameters mod - integer, k - integer, l - integer, x0 - list of integers with size == l"
        help_g += "\n   5p - parameters p - integer, q1 - integer, q2 - integer, q3 - integer, w - integer, seed - integer"
        help_g += "\n   lfsr - parameters c_vec - binary, seed - binary"
        help_g += "\n   nfsr - parameters R1 - binary, R2 - binary, R3 - binary, w - integer, x1 - integer, x2 - integer, x3 - integer"
        help_g += "\n   mt - parameters mod - integer, seed - integer"
        help_g += "\n   rc4 - parameters K - list of 256 integers"
        help_g += "\n   rsa - parameters n - integer, e - integer, w - integer, x - integer"
        help_g += "\n   bbs - parameters x - integer"
        print(help_g)
        sys.exit()
    if args.g == 'lc':
        if len(args.i) > 4 or len(args.i) < 4:
            raise NotEnoughParameters("Not enough parameters need 4")
        try:
            result = LC.linear_rand_method(m=args.m,
                                           modulus=int(args.i[0]),
                                           a=int(args.i[1]),
                                           c=int(args.i[2]),
                                           seed=int(args.i[3]),
                                           size=args.n)
        except:
            print("Error: LC parameters  error")
            sys.exit()
        return result
    elif args.g == 'add':
        if len(args.i) <= 3 or len(args.i[3:]) < int(args.i[2]):
            raise NotEnoughParameters(f"Not enough parameters need {3 + args.i[2]}")
        try:
            result = add.add_rand_method(m=args.m,
                                         modulus=int(args.i[0]),
                                         k=int(args.i[1]),
                                         l=int(args.i[2]),
                                         x0=list(map(int, args.i[3:])),
                                         size=args.n)
        except:
            print("Error: add parameters error")
            sys.exit()
        return result
    elif args.g == '5p':
        if len(args.i) < 6 or len(args.i) > 6:
            raise NotEnoughParameters("Not enough parameters need 6")
        try:
            result = fivep.five_P_rand_method(m=args.m,
                                              p=int(args.i[0]),
                                              q1=int(args.i[1]),
                                              q2=int(args.i[2]),
                                              q3=int(args.i[3]),
                                              w=int(args.i[4]),
                                              seed=int(args.i[5]),
                                              size=args.n)
        except:
            print("Error: 5p parameters error")
            sys.exit()
        return result
    elif args.g == 'lfsr':
        if len(args.i) > 2 or len(args.i) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = lfsr.lfsr_rand_method(m=args.m,
                                           c_vec=args.i[0],
                                           seed=args.i[1],
                                           size=args.n)
        except:
            print("Error: lfsr parameters error")
            sys.exit()
        return result
    elif args.g == 'nfsr':
        if len(args.i) > 7 or len(args.i) < 7:
            raise NotEnoughParameters("Not enough parameters need 7")
        try:
            result = nfsr.nfsr_rand_method(m=args.m,
                                           R1=args.i[0],
                                           R2=args.i[1],
                                           R3=args.i[2],
                                           w=int(args.i[3]),
                                           x1=int(args.i[4]),
                                           x2=int(args.i[5]),
                                           x3=int(args.i[6]),
                                           size=args.n)
        except:
            print("Error: nfsr parameters error")
            sys.exit()
        return result
    elif args.g == 'mt':
        if len(args.i) > 2 or len(args.i) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = mt.mt_rand_method(m=args.m,
                                       modulus=int(args.i[0]),
                                       seed=int(args.i[1]),
                                       size=args.n)
        except:
            print("Error: mt parameters error")
            sys.exit()
        return result
    elif args.g == "rc4":
        if len(args.i) < 256 or len(args.i) > 256:
            raise NotEnoughParameters("Not enough parameters need 256")
        try:
            result = rc4.rc4_rand_method(m=args.m,
                                         K=list(map(int, args.i)),
                                         size=args.n)
        except:
            print("Error: rc4 parameters error")
            sys.exit()
        return result
    elif args.g == "rsa":
        if len(args.i) < 4 or len(args.i) > 4:
            raise NotEnoughParameters("Not enough parameters need 4")
        try:
            result = rsaSH.RSA_rand_method(m=args.m,
                                           n=int(args.i[0]),
                                           e=int(args.i[1]),
                                           w=int(args.i[2]),
                                           x=int(args.i[3]),
                                           size=args.n)
        except:
            print("Error: rsa parameters error")
            sys.exit()
        return result
    elif args.g == "bbs":
        if len(args.i) > 2 or len(args.i) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = bbs.bbs_rand_method(m=args.m,
                                         x=int(args.i[0]),
                                         size=args.n)
        except:
            print("Error: bbs parameters error")
            sys.exit()
        return result
    else:
        raise NoneMethod(f"Error: have no {args.g} method")

def main():
    parser = ag.ArgumentParser(prog="prng.exe")
    parser.add_argument('-g', type=str, required=True, help="Code of method, lc, add, 5p, lfsr, nfsr, mt, rc4, rsa, bbs")
    parser.add_argument('-i', type=list, default=[], help="Parameters")
    parser.add_argument('-n', type=int, default=10000, help="Size")
    parser.add_argument('-f', type=str, default='rnd.dat', help="Path to save")
    parser.add_argument('-m', type=int, default=1024, help="Modulus")
    args = parser.parse_args()
    args.i = formatter_par(args.i)
    try:
        result = call(args)
    except NotEnoughParameters:
        print("Error: Not enough parameters")
        sys.exit()
    except NoneMethod:
        print(f"Error: {parser.prog} has no {args.g} method")
        help_g = "Code of method"
        help_g += "\n   lc - parameters mod - integer, a - integer, c - integer, seed - integer"
        help_g += "\n   add - parameters mod - integer, k - integer, l - integer, x0 - list of integers with size == l"
        help_g += "\n   5p - parameters p - integer, q1 - integer, q2 - integer, q3 - integer, w - integer, seed - integer"
        help_g += "\n   lfsr - parameters c_vec - binary, seed - binary"
        help_g += "\n   nfsr - parameters R1 - binary, R2 - binary, R3 - binary, w - integer, x1 - integer, x2 - integer, x3 - integer"
        help_g += "\n   mt - parameters mod - integer, seed - integer"
        help_g += "\n   rc4 - parameters K - list of 256 integers"
        help_g += "\n   rsa - parameters n - integer, e - integer, w - integer, x - integer"
        help_g += "\n   bbs - parameters x - integer"
        print(help_g)
        sys.exit()
    head, tail = os.path.split(args.f)
    name, ex = os.path.splitext(tail)
    filename = name + ex
    i = 1
    while os.path.exists(filename):
        filename = name + f" ({i})" + ex
        i += 1
    with open(os.path.join(head, filename), "w") as f:
        f.write(str(result)[1:-1])

if __name__ == "__main__":
    main()
