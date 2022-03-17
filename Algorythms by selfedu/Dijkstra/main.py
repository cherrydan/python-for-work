#!/usr/bin/python3

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    from Dijkstra import *

    while v != -1:  # пока не просмотрим все вершины
        for j in get_link_v(v, D):  # перебираем вершины
            if j not in S:  # если вершина еще не просмотрена, то формируем её вес по формуле
                w = T[v] + D[v][j]
                if w < T[j]:
                    T[j] = w

        v = arg_min(T, S)
        if v > 0:
            S.add(v)

    print(T)
