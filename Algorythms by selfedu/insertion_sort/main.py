#!/usr/bin/python3

# -*- coding: utf-8 -*-


from insertion_sort import *

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(a)
