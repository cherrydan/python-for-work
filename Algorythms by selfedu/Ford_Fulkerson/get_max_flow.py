#!/usr/bin/python3

def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)
