#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Поиск кратчайшего пути во взвешенном графе
(c) selfedu
"""

from math import inf as INF
from Floyd.get_path import get_path

# матрица смежности для графа
V = [[0, 2, INF, 3, 1, INF, INF, 10],
     [2, 0, 4, INF, INF, INF, INF, INF],
     [INF, 4, 0, INF, INF, INF, INF, 3],
     [3, INF, INF, 0, INF, INF, INF, 8],
     [1, INF, INF, INF, 0, 2, INF, INF],
     [INF, INF, INF, INF, 2, 0, 3, INF],
     [INF, INF, INF, INF, INF, 3, 0, 1],
     [10, INF, 3, 8, INF, INF, 1, 0]
     ]

# число вершин в графе

N = len(V)
# начальный список вершин, для поиска кратчайшего пути в графе
P = [[v for v in range(N)] for u in range(N)]