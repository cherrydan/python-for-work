#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Подобрал свои константы генетического алгоритма, для поиска за меньшее поличество поколений

(c) danny
"""

from deap import base, algorithms
from deap import creator
from deap import tools

import algelitism

import random

import matplotlib.pyplot as plt

import numpy as np

import gym

env = gym.make('MountainCar-v0')

LENGTH_CHROM = 200

# константы генетического алгоритма
# подобрал их таким образом, чтобы алгоритм искал решение за меньшее кол-во поколений

POPULATION_SIZE = 100 # 100 находит на 58-м поколении
P_CROSSOVER = 0.9
P_MUTATION = 0.2
MAX_GENERATIONS = 80 # находит на 58-поколении

HALL_OF_FAME_SIZE = 3

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

RANDOM_SEED = 42
random.seed(RANDOM_SEED)



