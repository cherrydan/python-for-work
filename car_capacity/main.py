#!/usr/bin/python3

# -*- coding: utf-8 -*-

from car_capacity import car_capacity

if __name__ == '__main__':
    persons = int(input('Enter number of persons to transfer needed: '))
    print('Cars needed for transfer {} persons = {}'.format(persons, car_capacity(persons)))
