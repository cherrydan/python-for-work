# -*- coding: utf-8 -*-

"""

сделаю на основе урока selfedu kmp-алгоритм в виде функции

Алгоритм kmp:
Время работы алгоритма линейно зависит от объёма входных данных, то есть разработать асимптотически
более эффективный алгоритм невозможно.
(c) Wikipedia

"""


def kmp(t, a) -> bool:
    """
    kmp(t,a)
    :param t: substring
    :param a: string
    :return: true if substring is found
    """
    p = [0] * len(t)
    j = 0
    i = 1

    while i < len(t):
        if t[j] == t[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]

    m = len(t)
    n = len(a)

    i = 0
    j = 0

    while i < n:
        if a[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                return True
                break

        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == n:
        return False


def alg_speed_info(t, a):
    print('Количество проходов при прямом поиске: (len строка * len образец)', len(t) * len(a))
    print('Количество проходов при использовании алгоритма kmp (len строка + len образец)', len(t) + len(a))
