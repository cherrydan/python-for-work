#!/usr/bin/python3

# -*- coding: utf-8 -*-

from Prima_algorythm import *

from Prima_algorythm.get_min import get_min

while len(U) < N:
    r = get_min(R, U)  # ребро с нимимальным весом
    if r[0] == INF:  # если ребёр нет, то остов построен
        break

    T.append(r)  # добавляем ребро в остов

    U.add(r[1])  # добавляем вершины в множество U
    U.add(r[2])

print(T)