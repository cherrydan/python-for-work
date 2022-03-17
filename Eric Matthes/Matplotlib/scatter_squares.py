#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Автоматический вычисленный график квадратов чисел до 1000
выведен при помощи отдельных точек
(с) Eric Matiz
"""
import matplotlib.pyplot as plt

x_values = list(range(1, 10001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues,
        edgecolor='none', s=40)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of values', fontsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

