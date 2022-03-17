#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Ищем кратчайший маршрут в грАфе
(с) selfedu
"""

from deap import base, algorithms
from deap import creator
from deap import tools

import random

import matplotlib.pyplot as plt

import numpy as np

import seaborn as sns

from graph_show import show_graph

INF = 100

# матрица смежности с допустимыми маршрутами в графе
D = ((0, 3, 1, 3, INF, INF),
     (3, 0, 4, INF, INF, INF),
     (1, 4, 0, INF, 7, 5),
     (3, INF, INF, 0, INF, 2),
     (INF, INF, 7, INF, 0, 4),
     (INF, INF, 5, 2, 4, 0))

# стартовая вершина 0 (1)
startV = 0

LENGTH_D = len(D)
LENGTH_CHROM = LENGTH_D * len(D[0]) # длина всей хромосомы 36

# константы генетического алгоритма

POPULATION_SIZE = 500 # 500
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS = 30 # 30

HALL_OF_FAME_SIZE = 1

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
