#!/usr/bin/python3

# -*- coding: utf-8 -*-

def get_max_vertex(k, V, S):
    m = 0  # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue
        if w[2] == 1:  # движение по стрелке
            if m < w[0]:
                m = w[0]
                v = i
        else:
            if m < w[1]:
                m = w[1]
                v = i
    return v
