#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Прогоню свою функцию kmp, alg_speed_info

(c) danny
"""
from kmp import kmp, alg_speed_info

if __name__ == '__main__':
    t = 'данные'
    a = 'большие метеоданные'

    if kmp(t, a):
        print('Образец найден!')
    else:
        print('Образец не найден.')

    print('\nСтатистика работы алгоритма:')
    print('-----------------------------')
    alg_speed_info(t, a)