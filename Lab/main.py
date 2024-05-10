import tabulate
import os.path, os
import subprocess
import calculate as c
import sys
from time import sleep

def readfile(path, message):
    with open(path, 'r') as f:
        lst = f.read().split(', ')
    lst = list(map(lambda x: float(x) if '.' in x else int(x), lst))
    # m = max(lst)
    lst = list(map(lambda x: x / 1024, lst))
    return lst, message

def main(args : list[tuple[list, str]]):
    tabs = []
    for lst, message in args:
        print(message)
        print(f"Мат. ожидание {c.math_expectation(lst)}")
        print(f"Среднекв. отклонение {c.std_deviation(lst)}")
        c.relative(lst)
        c.draw_graph(lst, ["Зависимость математического ожидания от объёма выборки", "Мат. ожидание", "Объём выборки"], c.math_expectation)
        c.draw_graph(lst, ["Зависимость среднеквадратичного отклонения от объёма выборки", "Среднекв. отклонение", "Объём выборки"], c.std_deviation)
        tabs.append([c.xi_square(lst), c.series(lst), c.interval(lst), c.partition(lst), c.permutation(lst), c.monoton(lst), c.conflicts(lst)])
        tabs[-1] = list(map(lambda x: '+' if x else '-', tabs[-1]))
        tabs[-1].insert(0, message)
        # print(f"Хи-квадрат {c.xi_square(lst)}")
        # print(f"Серий {c.series(lst)}")
        # print(f"Интервалов {c.interval(lst)}")
        # print(f"Разбиений {c.partition(lst)}")
        # print(f"Перестановок {c.permutation(lst)}")
        # print(f"Монотонности {c.monoton(lst)}")
        # print(f"Конфликтов {c.conflicts(lst)}")
    print(tabulate.tabulate(tabs, headers=["", "Хи-квадрат", "Серий", "Интервалов", "Разбиений", "Перестановок", "Монотонности", "Конфликтов"], tablefmt="grid-circled"))

if __name__ == "__main__":
    rnd_files = {}
    if not os.path.exists('prng.sh'):
        print("Ключевой файл генерации ПСЧ отсутствует")
        with open('prng.sh', 'w') as f:
            print("Создаём файл по умолчанию.", end='')
            f.write('prng.exe /g:lc /i:2147483647,48271,0,350 /n:10000 /m:1024 /f:rnd_lc.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:add /i:100,24,55,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55 /n:10000 /m:1024 /f:rnd_add.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:5p /i:89,20,40,69,1024,615930009644690137449363111 /n:10000 /m:1024 /f:rnd_5p.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:lfsr /i:1000001010011,1110101001001 /n:10000 /m:1024 /f:rnd_lfsr.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:nfsr /i:1000001010011,1000000000000011,100011101,1024,7497,49311,345 /n:10000 /m:1024 /f:rnd_nfsr.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:mt /i:4096,25 /n:10000 /m:1024 /f:rnd_mt.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:rc4 /i:3179,3298,3097,2987,2258,2437,195,583,1623,2324,1886,3533,1935,254,1697,2568,2181,2266,3523,3830,535,3541,1025,2103,290,3932,3481,909,4047,2991,2586,129,2338,1775,706,1232,2149,3662,2979,175,3241,2746,431,1137,2249,806,3589,22,2536,3305,3375,844,4047,3642,3293,3153,2464,437,488,3122,2235,771,828,3208,2879,3482,2070,1233,11,1985,2594,1762,3934,642,2227,3319,1403,2038,4071,3533,1740,3480,2488,2788,2784,890,264,163,4012,662,762,1410,2948,1937,2593,369,2871,1094,1347,4041,1516,3187,2897,3381,342,1125,1350,512,3698,1854,692,2027,1682,3734,4003,753,1349,20,2203,3273,3287,3889,458,691,2666,2126,617,2832,142,2853,3938,843,2352,2377,435,1051,1383,4070,3333,1726,1382,3098,2874,2303,2592,2034,874,3591,2833,1628,3144,3702,2086,3820,783,966,4039,1654,3876,3345,3243,3645,49,1549,22,1945,3010,2182,3350,3038,3687,1545,3194,1693,3793,3947,3254,3438,1337,2986,1500,1970,1130,2007,2477,3272,2090,746,2576,78,1204,3821,2162,1001,3963,2814,273,2751,419,735,175,1385,1844,63,264,1379,2546,3196,863,1185,3727,3353,662,1172,2545,2122,1470,2940,1036,3108,3717,1266,2252,2540,2065,993,2492,1469,187,2773,4091,2432,2003,509,1930,2326,2440,2882,2673,562,1563,2950,367,2366,2763,3293,2654,2122,1836,4089,1000,3463,3052,9,1078,2453 /n:10000 /m:1024 /f:rnd_rc4.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:rsa /i:12709189,53,300,25 /n:10000 /m:1024 /f:rnd_rsa.dat\n')
            print('.', end='')
            sleep(1)
            f.write('prng.exe /g:bbs /i:25 /n:10000 /m:1024 /f:rnd_bbs.dat')
            print('*')
        print("Файл по умолчанию создан. Продолжаем")
    with open('prng.sh', 'r') as f:
        commands = list(map(lambda x: x.strip('\n').split(' '), f.readlines()))

    directory_path = os.path.abspath(__file__)
    head1, _ = os.path.split(directory_path)
    head2, _ = os.path.split(head1)
    prng_path = None
    for root, dirs, files in os.walk(head2):
        for name in files:
            if name == commands[0][0]:
                prng_path = os.path.join(root, name)
    if prng_path == None:
        print("Не найден файл программы prng.exe")
        sys.exit()
    for i in range(len(commands)):
        for arg in commands[i]:
            if arg.startswith('/g:'):
                method = arg[3:]
            if arg.startswith('/f:'):
                file_path = arg[3:]
        rnd_files[method] = (file_path, commands[i])
    args = []
    print("Loading", end='')
    print(".", end='')
    if not os.path.exists(rnd_files['lc'][0]):
        subprocess.run([prng_path].extend(rnd_files['lc'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['lc'][0], 'Линейно-конгруэнтный метод'))
    print(".", end='')
    if not os.path.exists(rnd_files['add'][0]):
        subprocess.run([prng_path].extend(rnd_files['add'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['add'][0], 'Аддитивный метод'))
    print(".", end='')
    if not os.path.exists(rnd_files['5p'][0]):
        subprocess.run([prng_path].extend(rnd_files['5p'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['5p'][0], 'Пятипараметрический метод'))
    print(".", end='')
    if not os.path.exists(rnd_files['lfsr'][0]):
        subprocess.run([prng_path].extend(rnd_files['lfsr'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['lfsr'][0], 'РСЛОС'))
    print(".", end='')
    if not os.path.exists(rnd_files['nfsr'][0]):
        subprocess.run([prng_path].extend(rnd_files['nfsr'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['nfsr'][0], 'Нелинейная комбинация РСЛОС'))
    print(".", end='')
    if not os.path.exists(rnd_files['mt'][0]):
        subprocess.run([prng_path].extend(rnd_files['mt'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['mt'][0], 'Вихрь Мерсенна'))
    print(".", end='')
    if not os.path.exists(rnd_files['rc4'][0]):
        subprocess.run([prng_path].extend(rnd_files['rc4'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['rc4'][0], 'RC4'))
    print(".", end='')
    if not os.path.exists(rnd_files['rsa'][0]):
        subprocess.run([prng_path].extend(rnd_files['rsa'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['rsa'][0], 'ГПСЧ на основе RSA'))
    print(".", end='')
    if not os.path.exists(rnd_files['bbs'][0]):
        subprocess.run([prng_path].extend(rnd_files['bbs'][1][1:]))
    print(".", end='')
    args.append(readfile(rnd_files['bbs'][0], 'Блюма-Блюма-Шуба'))
    print("*")
    main(args)
