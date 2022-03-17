#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Автоматический вычисленный график кубов чисел до 5000
выведен при помощи отдельных точек
(с) Eric Matiz
ДЗ выполнил: danny
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values,c=y_values,
        edgecolor='none', s=40)

plt.title('Cube Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of values', fontsize=14)
plt.axis([0, 5000, 0, 125000000000])

#plt.show()
# сохраняем диаграмму в png
plt.savefig('cubes.png',  bbox_inches='tight')
