# -*- coding: utf-8 -*-

# ***************************
# Реализовать функцию car_capacity, принимающую на вход количество человек,
# и возвращающее количество легковых автомобилей, нужных для перевозки заданного количества человек, при условии
# что в одном автомобиле помещается не более 5 человек.
# ***************************
import math


def car_capacity(persons: int) -> int:
    """
    car_capacity(persons)
    returns number of cars, for transfer number of persons needed. One car capacity is 5 pers.

    :param persons: int
    :return: int
    """
    n = persons / 5
    if n % 5 != 0:
        return math.ceil(n)
    else:
        return n

3