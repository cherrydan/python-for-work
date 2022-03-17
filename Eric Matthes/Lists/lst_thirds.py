#!/usr/bin/python3
#-*- coding: utf-8 -*-
# создать список чисел кратных 3, в диапазоне от 3 до 30
# вывести его на экран
lst = []
for x in range(3, 31, 3):
    lst.append(x)

for x in lst:
    print(x)

