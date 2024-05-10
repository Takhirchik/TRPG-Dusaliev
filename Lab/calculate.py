from matplotlib.pyplot import plot, title, xlabel, ylabel, show, grid
import numpy as np
from math import sqrt, fabs, floor, comb, factorial
from scipy.stats import chi2

def count(lst : list[float]):
    elems = {}
    for elem in lst:
        if elem in elems:
            elems[elem] += 1
        else: elems[elem] = 1
    return elems

def probs(dct : dict, size : int):
    return {key : value / size for key, value in dct.items()}

def math_expectation(lst : list[float]):
    elem_count = count(lst)
    elem_probs = probs(elem_count, len(lst))
    values = list(elem_probs.keys())
    weights = list(elem_probs.values())
    return sum(map(lambda x : x[0] * x[1], zip(values, weights))) / sum(weights)

def std_deviation(lst : list[float]):
    mean = math_expectation(lst)
    return sqrt(sum([(elem - mean) ** 2 for elem in lst]) / len(lst))

def draw_graph(lst : list[float],
               list_of_messages : list[str],
               func,
               step : int = 1):
    n = len(lst)
    x_lst = []
    y_lst = []
    for i in range(50, 0, -step):
        current_plot = n // i
        x_lst.append(current_plot)
        current_value = func(lst[:current_plot])
        y_lst.append(current_value)
    plot(x_lst, y_lst)
    title(list_of_messages[0])
    ylabel(list_of_messages[1])
    xlabel(list_of_messages[2])
    grid(True)
    show()

def relative(lst):
    expected_mean = 0.5
    expected_std_dev = 0.2877
    current_mean = math_expectation(lst)
    current_std_dev = std_deviation(lst)
    print(f"Относительная погрешность математического ожидания = {fabs(expected_mean - current_mean)}")
    print(f"Относительная погрешность среднеквадратичного отклонения = {fabs(expected_std_dev - current_std_dev)}")

def xi_square(lst : list[float],
              alpha : float = 0.05,
              exp : list[float] = None,
              obs : list[float] = None,
              k : int = None
              ):
    if obs is None:
        obs = list(count(lst).values())
    if k is None:
        k = len(obs)
    if exp is None:
        exp = [len(lst) / k] * k
    xi = sum(map(lambda x: ((x[0] - x[1]) ** 2) / x[1], zip(obs, exp)))
    xi_squared = chi2.ppf(1 - alpha, k - 1)
    return xi <= xi_squared

def series(lst : list[float], alpha : float = 0.05, d : int = 8):
    obs = [0] * (d ** 2)
    for j in range(len(lst) // 2):
        q, r = floor(lst[2 * j] * d), floor(lst[2 * j + 1] * d)
        obs[q * d + r] += 1
    exp = d ** 2 * [len(lst) / (2 * d ** 2)]
    return xi_square(lst=lst, exp=exp, obs=obs, k=d * d, alpha=alpha)

def interval(lst : list[float],
             alpha : float = 0.05,
             t : int = 10,
             a : float = 0.5,
             b : float = 1):
    j, s, c_r, n = -1, 0, t * [0], len(lst)
    intervals_count = n / 10
    while s < intervals_count and j < n:
        r, j = 0, j + 1
        while a <= lst[j] <= b and j < n:
            r, j = r + 1, j + 1
        c_r[min(r, t) - 1] += 1
        s += 1
    sub = b - a
    exp = [intervals_count * sub * (1 - sub) ** z for z in range(t)]
    return xi_square(lst=lst, alpha=alpha, obs=c_r, exp=exp, k=t + 1)

def partition(lst : list[float],
              d : int = 16,
              k : int = 5):
    n = len(lst)
    obs = [0] * k
    for i in range(n // k):
        unique = list(set([floor(u * d) for u in lst[i * k:i * k + k]]))
        obs[len(unique) - 1] += 1

    def stirling(r : int, k : int):
        if r <= 0 or r != 0 and r == k:
            return 1
        elif k <= 0 or r < k:
            return 0
        elif r == 0 and k == 0:
            return - 1
        else:
            return k * (stirling(r - 1, k)) + stirling(r - 1, k - 1)

    exp = [0] * k
    for r in range(1, k + 1):
        p = 1.0
        for i in range(r):
            p *= d - i
        exp[r - 1] = (n / k) * (p / d ** k) * stirling(k, r)
    return xi_square(lst=lst, obs=obs, exp=exp, k=k)

def permutation(lst : list[float],
                alpha : float = 0.05,
                t : int = 10):
    n, k, dct = len(lst), factorial(t), {}

    for i in range(0, n, t):
        group = tuple(sorted(lst[i:i + t]))
        dct[group] = dct.get(group, 0) + 1

    obs = list(dct.values())
    exp = [n / k] * len(obs)

    return xi_square(lst=lst, alpha=alpha, obs=obs, exp=exp, k=k)

def monoton(lst : list[float],
            alpha : float = 0.05):
    mtx_a = [[4529.4, 9044.9, 13568.0, 18091.0, 22615.0, 27892.0],
             [9044.9, 18097.0, 27139.0, 36187.0, 45234.0, 55789.0],
             [13568.0, 27139.0, 40721.0, 54281.0, 67852.0, 83685.0],
             [18091.0, 36187.0, 54281.0, 72414.0, 90470.0, 111580.0],
             [22615.0, 45234.0, 67852.0, 90470.0, 113262.0, 139476.0],
             [27892.0, 55789.0, 83685.0, 111580.0, 139476.0, 172860.0]]
    vec_b = [1.0 / 6.0, 5.0 / 24.0, 11.0 / 120.0, 19.0 / 720.0, 29.0 / 5040.0, 1.0 / 840.0]
    n, tmplst, i  = len(lst), [], 0
    while i < n:
        s = 1
        while i + s < n and lst[i + s - 1] <= lst[i + s]:
            s += 1
        tmplst.append(s)
        i += s
    m, group_counts = 0, {}
    for length in tmplst:
        m = max(m, length)
        group_counts[length] = group_counts.get(length, 0) + 1
    exp, buff, n = [], 0, len(lst)
    for c in tmplst:
        m = 1/6
        min_value = min(c, 6)
        for i in range(min_value):
            for j in range(min_value):
                tmp = 1
                tmp *= (lst[i + buff] - n * vec_b[i])
                tmp *= (lst[j + buff] - n * vec_b[j])
                tmp *= mtx_a[i][j]
                m += tmp
        buff += c
        exp.append(m)
    return xi_square(lst=lst, exp=exp, alpha=alpha)

def conflicts(lst : list[float],
              m : int = 1024):
    n = len(lst) // m
    p0 = 1 - n / m + comb(n, 2) / (m ** 2)
    dev = n / m - 1 + p0
    return dev < n + 10 or dev > n - 10
