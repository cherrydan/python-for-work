#!/usr/bin/python3

def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i
