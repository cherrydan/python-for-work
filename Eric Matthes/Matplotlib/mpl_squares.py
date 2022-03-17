#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Пример простейшей диаграммы в Matplotlib
(c) Eric Matiz
"""
import matplotlib.pyplot as plt

input_values = [1.0, 2.0, 3.0, 4.0, 5.0]
squares = [1.0 ** 2, 2.0 ** 2, 3.0 **2, 4.0 ** 2, 5.0 **2]
plt.plot(input_values, squares, linewidth=5)

# задаём заголовок окна и диаграммы
plt.title('Square numbers', fontsize=25)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Square of values', fontsize=14)

# назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)
# выводим график
plt.show()

