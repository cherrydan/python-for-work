#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Уроки ООП на Python
Режимы доступа: private, public, protected
Геттеры и сеттеры

(c) selfedu
"""


class Point:
    # атрибут без подчёркивания = public
    # атрибут с одним подчёркиванием = protected
    # атрибут с двумя подчёркиваниями = private
    def __init__(self, x=0, y=0):
        # создадим два приватных атрибута
        self.__x = x
        self.__y = y

    # создаём закрытый метод для проверки
    def __check_value(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    # создаём сеттер для закрытых атрибутов __x и __y
    def set_coords(self, x, y):
        # прежде чем записать значение, проверяем, чтобы оно относилось к числовому типу
        # обращение к закрытому методу происходит через имя основного класса
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Значения координат должны быть цифрами!')

    # и геттер для них же
    def get_coords(self):
        return self.__x, self.__y,


pt = Point(1, 2)
print(pt.get_coords())


