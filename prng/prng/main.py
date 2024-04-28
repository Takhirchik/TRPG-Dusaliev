from libs import LC, add, lfsr, fivep, nfsr, mt, rc4, rsaSH, bbs
import sys
import os.path

class NotEnoughParameters(Exception):
    pass

class NoneMethod(Exception):
    pass

def print_usage(prog):
    usage_g = "Использование: "
    usage_g += f"{prog} [/h] /g:<Метод> [/i:<Параметры>] [/n:<Кол-во>] [/f:<Путь>] [/m:<Модуль>]"
    print(usage_g)

def print_help():
    help_g = "Описание аргументов"
    help_g += "\n   /g:<Метод>       lc - Линейный Конгруэнтный метод"
    help_g += "\n                    add - Аддитивный метод"
    help_g += "\n                    5p - Пятипараметрический метод"
    help_g += "\n                    lfsr - РСЛОС"
    help_g += "\n                    nfsr - НРСЛОС"
    help_g += "\n                    mt - Вихрь Мерсенна"
    help_g += "\n                    rc4 - Алгоритм RC4"
    help_g += "\n                    rsa - Метод на основе RSA"
    help_g += "\n                    bbs - Метод Блюма-Блюма-Шуба"
    help_g += "\n   [/n:<Кол-во>]    Количество выходных генерируемых чисел (default:10000)"
    help_g += "\n   [/f:<Путь>]      Путь для выходного файла (default:rnd.dat)"
    help_g += "\n   [/m:<Модуль>]    Максимально возможное генерируемое число (default:1024)"
    help_g += "\n   [/i:<Параметры>] Необходимые параметры для методов"
    help_g += "\n   [/h]             Справка"
    print(help_g)

def formatter_par(args : list):
    l = []
    k = 1
    for arg in args:
        if len(l) < k:
            l.append(arg)
        else:
            if arg.isdigit():
                l[k - 1] += arg
            else:
                k += 1
                continue
    return l

def call(method:str,
         pars:list,
         n:int,
         m:int):
    if pars == []:
        print(pars)
        print_help()
        sys.exit()
    if method == 'lc':
        if len(pars) > 4 or len(pars) < 4:
            raise NotEnoughParameters("Not enough parameters need 4")
        try:
            result = LC.linear_rand_method(m=m,
                                           modulus=int(pars[0]),
                                           a=int(pars[1]),
                                           c=int(pars[2]),
                                           seed=int(pars[3]),
                                           size=n)
        except:
            print("Ошибка: Неправильно указаны параметры LC")
            sys.exit()
        return result
    elif method == 'add':
        if len(pars) <= 3 or len(pars[3:]) < int(pars[2]):
            raise NotEnoughParameters(f"Not enough parameters need {3 + pars[2]}")
        try:
            result = add.add_rand_method(m=m,
                                         modulus=int(pars[0]),
                                         k=int(pars[1]),
                                         l=int(pars[2]),
                                         x0=list(map(int, pars[3:])),
                                         size=n)
        except:
            print("Ошибка: Неправильно указаны параметры ADD")
            sys.exit()
        return result
    elif method == '5p':
        if len(pars) < 6 or len(pars) > 6:
            raise NotEnoughParameters("Not enough parameters need 6")
        try:
            result = fivep.five_P_rand_method(m=m,
                                              p=int(pars[0]),
                                              q1=int(pars[1]),
                                              q2=int(pars[2]),
                                              q3=int(pars[3]),
                                              w=int(pars[4]),
                                              seed=int(pars[5]),
                                              size=n)
        except:
            print("Ошибка: Неправильно указаны параметры 5P")
            sys.exit()
        return result
    elif method == 'lfsr':
        if len(pars) > 2 or len(pars) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = lfsr.lfsr_rand_method(m=m,
                                           c_vec=pars[0],
                                           seed=pars[1],
                                           size=n)
        except:
            print("Ошибка: Неправильно указаны параметры LFSR")
            sys.exit()
        return result
    elif method == 'nfsr':
        if len(pars) > 7 or len(pars) < 7:
            raise NotEnoughParameters("Not enough parameters need 7")
        try:
            result = nfsr.nfsr_rand_method(m=m,
                                           R1=pars[0],
                                           R2=pars[1],
                                           R3=pars[2],
                                           w=int(pars[3]),
                                           x1=int(pars[4]),
                                           x2=int(pars[5]),
                                           x3=int(pars[6]),
                                           size=n)
        except:
            print("Ошибка: Неправильно указаны параметры NFSR")
            sys.exit()
        return result
    elif method == 'mt':
        if len(pars) > 2 or len(pars) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = mt.mt_rand_method(m=m,
                                       modulus=int(pars[0]),
                                       seed=int(pars[1]),
                                       size=n)
        except:
            print("Ошибка: Неправильно указаны параметры MT")
            sys.exit()
        return result
    elif method == "rc4":
        if len(pars) < 256 or len(pars) > 256:
            raise NotEnoughParameters("Not enough parameters need 256")
        try:
            result = rc4.rc4_rand_method(m=m,
                                         K=list(map(int, pars)),
                                         size=n)
        except:
            print("Ошибка: Неправильно указаны параметры RC4")
            sys.exit()
        return result
    elif method == "rsa":
        if len(pars) < 4 or len(pars) > 4:
            raise NotEnoughParameters("Not enough parameters need 4")
        try:
            result = rsaSH.RSA_rand_method(m=m,
                                           n=int(pars[0]),
                                           e=int(pars[1]),
                                           w=int(pars[2]),
                                           x=int(pars[3]),
                                           size=n)
        except:
            print("Ошибка: Неправильно указаны параметры RSA")
            sys.exit()
        return result
    elif method == "bbs":
        if len(pars) > 2 or len(pars) < 2:
            raise NotEnoughParameters("Not enough parameters need 2")
        try:
            result = bbs.bbs_rand_method(m=m,
                                         x=int(pars[0]),
                                         size=n)
        except:
            print("Ошибка: Неправильно указаны параметры BBS")
            sys.exit()
        return result
    else:
        raise NoneMethod(f"Error: have no {method} method")

def main(prog:str, args:list[str]):
    path = "rnd.dat"
    n = 10000
    m = 1024
    failed_args = []
    for argument in args:
        if argument.startswith("/g:"):
            method = argument[3:]
        elif argument.startswith("/i:"):
            pars = formatter_par(argument[3:])
        elif argument.startswith("/f:"):
            head, tail = os.path.split(argument[3:])
            name, ex = os.path.splitext(tail)
            filename = name + ex
            path = os.path.join(head, filename)
            i = 1
            while os.path.exists(path):
                filename = name + f" ({i})" + ex
                path = os.path.join(head, filename)
                i += 1
        elif argument.startswith("/n:"):
            n = int(argument[3:])
        elif argument.startswith("/m:"):
            m = int(argument[3:])
        elif argument.startswith("/h"):
            if argument != args[0]:
                print("Ошибка: параметр /h нельзя использовать вместе с другими параметрами")
            print_usage(prog)
            print_help()
            sys.exit()
        else:
            failed_args.append(argument)
            if argument != args[-1]:
                continue
            else:
                print(f"Неправильно указаны параметры {failed_args}")
                print_usage(prog)
                print_help()
                sys.exit()
    try:
        result = call(method=method, pars=pars, n=n, m=m)
    except NotEnoughParameters:
        print("Ошибка: Недостаточно параметров")
        print_help()
        sys.exit()
    except NoneMethod:
        print(f"Ошибка: В {prog} нет метода {method}")
        print_usage(prog)
        print_help()
        sys.exit()

    with open(path, "w") as f:
        f.write(str(result)[1:-1])

if __name__ == "__main__":
    args = sys.argv[1:]
    main(sys.argv[0], args)
