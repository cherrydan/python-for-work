'''
Программа спрашивает у пользователя, сколько знаков вывести после точки в числе
Пи и выводит его
'''

import math

Pi = math.pi

sPi = str(Pi)

print('Число Pi = ' + sPi)
print('Макс длина числа Pi после точки = ' + str(len(sPi) - 2) + ' знаков')

pos = int(input('''Введите количество знаков после точки, которое
следует вывести: '''))

resStr = sPi[:pos + 2]

print('Результат = ' + resStr)
