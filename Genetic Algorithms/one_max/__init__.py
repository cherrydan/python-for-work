#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""

Задача OneMax состоит в том, чтобы найти двоичную строку заданной дли-
ны, для которой сумма составляющих ее цифр максимальна. Например, при
решении задачи OneMax длины 5 будут рассматриваться такие кандидаты

(Генетические алгоритмы на Питон. Вирсански. Стр. 68)

"""
from deap import base
from deap import creator
from deap import tools

import random

import matplotlib.pyplot as plt

# константы задачи

ONE_MAX_LENGTH = 100  # длина подлежащей оптимизации строки

# константы генетического алгоритма

POPULATION_SIZE = 200  # размер популяции
P_CROSSOVER = 0.9  # вероятность скрещивания
P_MUTATION = 0.1  # вероятность мутации
MAX_GENERATIONS = 50  # максимальное количество поколений

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
