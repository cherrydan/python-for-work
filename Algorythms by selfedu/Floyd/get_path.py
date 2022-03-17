#!/usr/bin/python3

# -*- coding: utf-8 -*-

def get_path(P, u, v):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)

    return path


