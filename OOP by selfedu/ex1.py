#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Уроки ООП на Python

Класс. Экземпляры класса. Атрибуты класса.

(c) selfedu
"""


class Point:
    """Класс для представления точки на плоскости"""
    x = 1
    y = 1


print(Point.__doc__)

pt = Point()
print(pt.__dict__)
Point.x = 100
print(pt.x, pt.y)
print(id(pt), id(Point), sep='\n')
pt.x = 5
pt.y = 10
print(pt.x, pt.y)
print(Point.x, Point.y)
print(pt.__dict__)
