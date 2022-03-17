#!/usr/bin/python3

# -*- coding: utf-8 -*-


from selection_sort import *


for i in range(N-1):
    m = arr[i]  # предполагаем что это минимальное значение
    p = i  # запоминаем индекс минимального значения

    # поиск минимального среди оставшихся элементов
    for j in range(i + 1, N):
        if m > arr[j]:
            m = arr[j]
            p = j

    if p != i:  # обмен значениями, если был найден минимальный не в i-той позиции
        t = arr[i]
        arr[i] = arr[p]
        arr[p] = t


print(arr)
