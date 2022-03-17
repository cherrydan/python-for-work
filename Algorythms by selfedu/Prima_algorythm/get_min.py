#!/usr/bin/python3

# -*- coding: utf-8 -*-

from Prima_algorythm import *


def get_min(R, U):
    rm = (INF, -1, -1)
    for v in U:
        rr = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else INF)
        if rm[0] > rr[0]:
            rm = rr

    return rm

