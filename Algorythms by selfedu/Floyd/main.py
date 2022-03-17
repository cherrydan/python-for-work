#!/usr/bin/python3

# -*- coding: utf-8 -*-

from Floyd import *

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

# нумерация вершин начинается с 0
start = 1
end = 4

print(get_path(P, end, start))
