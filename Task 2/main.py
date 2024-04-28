from libs import st, tr, ex, gm, nr, ln, ls, bi
import sys
import os.path
from matplotlib.pyplot import hist, xlabel, ylabel, title, show
from numpy import array

class NotEnoughParameters(Exception):
    pass

class NoneMethod(Exception):
    pass

def visual(distribution:list, name_of_dist:str):
    dists = {
        "st":"Стандартное равномерное распределение",
        "tr":"Треугольное распределение",
        "ex":"Общее экспоненциальное распределение",
        "nr":"Нормальное распределение",
        "gm":"Гамма распределение",
        "ln":"Логнормальное распределение",
        "ls":"Логистическое распределение",
        "bi":"Биномиальное распределение"
    }
    sequence = array(distribution)
    hist(x=sequence, bins=100)
    xlabel("Значение")
    ylabel("Частота")
    title(dists[name_of_dist])
    show()

def readfile(path:str):
    with open(path, "r") as f:
        l = []
        numbers = f.read()
        k = 1
        j = 0
        for s in numbers:
            if s.isdigit():
                if len(l) < k:
                    l.append(s)
                else:
                    l[k - 1] += s
                j = 0
            else:
                if j == 0:
                    k += 1
                j += 1
                continue
        numbers = l.copy()
        del(l)
        return list(map(int, numbers))

def print_usage(prog):
    usage_g = "Использование: "
    usage_g += f"{prog} [/h] /f:<Путь> /d:<Распределение> [/p1:<Параметр>] [/p2:<Параметр>] [/p3:<Параметр>] [/s:<Путь>] [/v]"
    print(usage_g)

def print_help():
    help_g = "Описание аргументов"
    help_g += "\n   /f:<Путь>            Путь до файла с входной последовательностью"
    help_g += "\n   /d:<Распределение>   st - Стандартное равномерное"
    help_g += "\n                        tr - Треугольное"
    help_g += "\n                        ex - Общее экспоненциальное"
    help_g += "\n                        nr - Нормальное"
    help_g += "\n                        gm - Гамма"
    help_g += "\n                        ln - Логнормальное"
    help_g += "\n                        ls - Логистическое"
    help_g += "\n                        bi - Биномиальное"
    help_g += "\n   [/p1:<Параметр>]     Параметр 1"
    help_g += "\n   [/p2:<Параметр>]     Параметр 2"
    help_g += "\n   [/p3:<Параметр>]     Параметр 3"
    help_g += "\n   [/s:<Путь>]          Путь для записи (default:distr-<Распределение>.dat)"
    help_g += "\n   [/v]                 Визулизировать (default:False)"
    help_g += "\n   [/h]                 Справка"
    print(help_g)

def call(d:str,
         numbers:list[int],
         p1,
         p2,
         p3
):
    if d == 'st':
        try:
            if p1 == None or p2 == None:
                raise NotEnoughParameters
            result = st(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры ST")
            sys.exit()
        return result
    elif d == 'tr':
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = tr(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры TR")
            sys.exit()
        return result
    elif d == 'ex':
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = ex(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры EX")
            sys.exit()
        return result
    elif d == 'nr':
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = nr(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры NR")
            sys.exit()
        return result
    elif d == 'gm':
        if p1 is None or p2 is None or p3 is None:
            raise NotEnoughParameters()
        try:
            if p1 is None or p2 is None or p3 is None:
                raise NotEnoughParameters()
            result = gm(numbers=numbers, p1=p1, p2=p2, p3=p3)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2 и/или P3")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры GM")
            sys.exit()
        return result
    elif d == 'ln':
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = ln(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры LN")
            sys.exit()
        return result
    elif d == "ls":
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = ls(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры LS")
            sys.exit()
        return result
    elif d == "bi":
        try:
            if p1 is None or p2 is None:
                raise NotEnoughParameters()
            result = bi(numbers=numbers, p1=p1, p2=p2)
        except NotEnoughParameters:
            print("Ошибка: Неправильно указаны параметры P1 и/или P2")
            sys.exit()
        except:
            print("Ошибка: Неправильно указаны параметры BI")
            sys.exit()
        return result
    else:
        raise NoneMethod()

def main(prog:str, args:list[str]):
    failed_args = []
    flag_viz = False
    p1, p2, p3 = None, None, None
    for argument in args:
        if argument.startswith("/f:"):
            if os.path.exists(argument[3:]):
                path = argument[3:]
            else:
                print(f"Ошибка: файла по пути {argument[3:]} не существует")
        elif argument.startswith("/d:"):
            d = argument[3:]
            name, ex = f"distr-{d}", ".dat"
            savepath = name + ex
            i = 1
            while os.path.exists(savepath):
                savepath = name + f" ({i})" + ex
                i += 1
        elif argument.startswith("/s:"):
            head, tail = os.path.split(argument[3:])
            name, ex = os.path.splitext(tail)
            filename = name + ex
            savepath = os.path.join(head, filename)
            i = 1
            while os.path.exists(savepath):
                filename = name + f" ({i})" + ex
                savepath = os.path.join(head, filename)
                i += 1
        elif argument.startswith("/p1:"):
            if '.' in argument[4:]:
                p1 = float(argument[4:])
            else:
                p1 = int(argument[4:])
        elif argument.startswith("/p2:"):
            if '.' in argument[4:]:
                p2 = float(argument[4:])
            else:
                p2 = int(argument[4:])
        elif argument.startswith("/p3:"):
            if '.' in argument[4:]:
                p3 = float(argument[4:])
            else:
                p3 = int(argument[4:])
        elif argument.startswith("/v"):
            flag_viz = True
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

    numbers = readfile(path)
    try:
        result = call(d=d, numbers=numbers, p1=p1, p2=p2, p3=p3)
    except NoneMethod:
        print(f"Ошибка: В {prog} нет распределения {d}")
        print_usage(prog)
        print_help()
        sys.exit()

    with open(savepath, "w") as f:
        f.write(d + '\n')
        f.write(str(result)[1:-1])

    if flag_viz:
        visual(result, d)

    sys.exit()

if __name__ == "__main__":
    args = sys.argv[1:]
    main(sys.argv[0], args)
