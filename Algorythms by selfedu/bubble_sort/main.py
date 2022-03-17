#!/usr/bin/python3

# -*- coding: utf-8 -*-

from bubble_sort import *


for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
