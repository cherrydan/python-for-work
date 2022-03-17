#!/usr/bin/python3
# -*- coding: utf-8 -*-

# функция, распаковывающая кортеж или список агрументов
def my_func(*args):
    for a in args:
        print(a, end=' ')
    if args:  # если аргументов нет
        print()


# функция, распаковывающая словарь аргументов
def my_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep=' -> ', end=' ')
    if kwargs:  # если словарь пуст
        print()


# делает и распаковку кортежа-списка, и словаря аргументов
def my_func3(*args, **kwargs):
    for a in args:
        print(a, end=' ')
    if args:  # если аргументов нет
        print()
    for k, v in kwargs.items():
        print(k, v, sep=' -> ', end=' ')
    if kwargs:  # если словарь пуст
        print()


if __name__ == '__main__':
    values = [1, 'py', 2, 'thon', '-', 3, ' the ', 4, ' best']
    dicts = {'Keiko': 'female 3', 'Hosico': 'male 7'}
    my_func3(*values, **dicts)

