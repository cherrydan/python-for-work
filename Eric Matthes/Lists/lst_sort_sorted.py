#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Демонстрация разницы между sort() и sorted()

countries = ['Japan', 'Ireland', 'Australia', 'New Zeland', 'Canada']
print(countries)
# сортируем
print('Сортируем...')
print(sorted(countries))
print('Исходный...')
print(countries)
print('Сортируем с реверсом')
print(sorted(countries, reverse=True))
print('Исходный...')
print(countries)
print('Изменяем список при помощи reverse()')
countries.reverse()
print('Изменённый...')
print(countries)
print('Восстановленный...')
countries.reverse()
print(countries)
print('Сортируем с изменением')
countries.sort()
print(countries)
print('Сортировка в обратном алфавитном порядке')
countries.sort(reverse=True)
print(countries)
