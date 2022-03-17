#!/usr/bin/python3
# coding: utf-8 -*-

"""

Домашнее задание по курсу ООП

(с) selfedu

"""


class Point3D:
    """Класс для представления точки на трехмерной плоскости """
    x = 10
    y = 1
    z = 1


pt1 = pt2 = pt3 = Point3D()

print(Point3D.__name__)
print(pt1.__doc__)

print('Точки x, y, z из разных экземпляров класса')
print(pt1.x, pt2.y, pt3.z)

print('Удаляем атрибут z')
delattr(Point3D, "z")

try:
    print(pt1.z, pt2.z, pt3.z)
except AttributeError:
    print('В классе Point3D отсутствует такой атрибут')

print('Добавляем атрибут q к экземпляру класса pt1')
pt1.q = 10
print('И выводим его через экземпляр класса pt2')
print(pt2.q)
print('Выводим список локальных переменных класса и экземпляров класса')
print('Point3D.__dict__ ', Point3D.__dict__)
print('pt1.__dict__ ', pt1.__dict__)
print('pt2.__dict__ ', pt2.__dict__)
print('pt3.__dict__ ', pt3.__dict__)
