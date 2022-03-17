#!/usr/bin/python3

# -*- coding: utf-8 -*-

import time

from deap import base, algorithms
from deap import creator
from deap import tools

import algelitism

import random

import matplotlib.pyplot as plt

import gym

from neuralnetwork import NNetwork

# создаём виртуальную тележку с шестом
env = gym.make('CartPole-v1')

# параметры нейросети
NEURONS_IN_LAYERS = [4, 1]  # распределение нейронов по слоям
nnetwork = NNetwork(*NEURONS_IN_LAYERS)


LENGTH_CHROM = nnetwork.getTotalWeights(*NEURONS_IN_LAYERS)
LOW = -1.0
UP = 1.0
ETA = 20


# параметры ген. алгоритма
POPULATION_SIZE = 20
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS  = 50
HALL_OF_FAME_SIZE = 2

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

RANDOM_SEED = 42
random.seed(RANDOM_SEED)