#!/usr/bin/python3

def arg_min(T, S):
    amin = -1
    m = max(T)

    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin


