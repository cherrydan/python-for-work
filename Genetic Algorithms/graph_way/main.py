#!/usr/bin/python3

# -*- coding: utf8 -*-
import random

import matplotlib.pyplot as plt
import numpy as np

from graph_way import *

# создаём ф-кцию вычисляющую приспособленность каждой особи
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# и сам класс особи, зарегаем в нём фун-цию FitnessMin
creator.create("Individual", list, fitness=creator.FitnessMin)

# создаём популяцию
toolbox = base.Toolbox()
# будет создаваться список неповторяющихся значений от 0 до 5
toolbox.register("RandomOrder", random.sample, range(LENGTH_D), LENGTH_D)
# создание индивида: у каждого будет 6 списков, созданных при помощи RandomOrder
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.RandomOrder, LENGTH_D)
# создание популяции из индивида
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

# создаём популяцию
population = toolbox.populationCreator(n=POPULATION_SIZE)


# вычисление суммарных маршрутов до всех вершин графа
def dijkstra_fitness(individual):
    s = 0
    for n, path in enumerate(individual):
        path = path[:path.index(n) + 1]
        si = startV
        for j in path:
            s += D[si][j]
            si = j
    return s,


# функция упорядочного скрещивания
def cx_ordered(ind1, ind2):
    for p1, p2 in zip(ind1, ind2):
        tools.cxOrdered(p1, p2)
    return ind1, ind2


# перемешиваем индексы в случае мутации
def mut_shuffle_indexes(individual, indpb):
    for ind in individual:
        tools.mutShuffleIndexes(ind, indpb)
    return individual,


# регистрируем рабочие функции ген. алгоритма
toolbox.register("evaluate", dijkstra_fitness)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", cx_ordered)
toolbox.register("mutate", mut_shuffle_indexes, indpb=1.0 / LENGTH_CHROM / 10)


# сбор статистики
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)

# запускаем генетический алгоритм средствами DEAP

population, logbook = algorithms.eaSimple(population, toolbox,
                                        cxpb=P_CROSSOVER/LENGTH_D,
                                        mutpb=P_MUTATION/LENGTH_D,
                                        ngen=MAX_GENERATIONS,
                                        stats=stats,
                                        halloffame=hof,
                                        verbose=True)
max_fitness_values, mean_fitness_values = logbook.select("min", "avg")
sns.set_style("whitegrid")
plt.plot(max_fitness_values, color="red")
plt.plot(mean_fitness_values, color="green")
plt.xlabel('Поколение')
plt.ylabel('Макс./сред. приспособляемость')
plt.title('Зависимость макс./средней приспособляемости от поколения')

plt.show()

best = hof[0]
print('\nЛучший индивид:\n', best)

fig, ax = plt.subplots()

show_graph(ax, best, startV)

plt.show()