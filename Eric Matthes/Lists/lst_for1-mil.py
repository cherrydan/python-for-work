#!/usr/bin/python3
# -*- coding: utf-8 -*-
# список из миллиона чисел
# от 1 до 1000000
CAPACITY = 1000000
lst = []
for x in range(1, CAPACITY + 1):
    lst.append(x)
print(min(lst)) # пусть Питон нам покажет самое минимальное значение 
print(max(lst)) # самое максимальное
print(sum(lst)) # и сумму всего от 1 до миллиона

