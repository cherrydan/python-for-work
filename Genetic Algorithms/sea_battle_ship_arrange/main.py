#!/usr/bin/python3
# -*- coding: utf-8 -*-

from deap import base, algorithms
from deap import creator
from deap import tools

from time import sleep

import algelitism
from graph_show import show_ships

import random
import matplotlib.pyplot as plt
import numpy as np

POLE_SIZE = 7
SHIPS = 10
LENGTH_CHROM = 3*SHIPS    # длина хромосомы, подлежащей оптимизации

# константы генетического алгоритма
POPULATION_SIZE = 200   # количество индивидуумов в популяции
P_CROSSOVER = 0.9       # вероятность скрещивания
P_MUTATION = 0.2        # вероятность мутации индивидуума
MAX_GENERATIONS = 50    # максимальное количество поколений
HALL_OF_FAME_SIZE = 1

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def randomShip(total):
    ships = []
    for n in range(total):
        ships.extend([random.randint(1, POLE_SIZE), random.randint(1, POLE_SIZE), random.randint(0, 1)])

    return creator.Individual(ships)


toolbox = base.Toolbox()
toolbox.register("randomShip", randomShip, SHIPS)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.randomShip)

population = toolbox.populationCreator(n=POPULATION_SIZE)

def shipsFitness(individual):
    type_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    inf = 1000
    P0 = np.zeros((POLE_SIZE, POLE_SIZE))
    P = np.ones((POLE_SIZE+6, POLE_SIZE+6))*inf
    P[1:POLE_SIZE+1, 1:POLE_SIZE+1] = P0

    th = 0.2
    h = np.ones((3, 6)) * th
    ship_one = np.ones((1, 4))
    v = np.ones((6, 3)) * th

    for *ship, t in zip(*[iter(individual)] * 3, type_ship):
        if ship[-1] == 0:
            sh = np.copy(h[:, :t+2])
            sh[1, 1:t+1] = ship_one[0, :t]
            P[ship[0] - 1:ship[0] + 2, ship[1]-1:ship[1] + t+1] += sh
        else:
            sh = np.copy(v[:t+2, :])
            sh[1:t+1, 1] = ship_one[0, :t]
            P[ship[0]-1:ship[0] + t+1, ship[1] - 1:ship[1] + 2] += sh


    s = np.sum(P[np.bitwise_and(P > 1, P < inf)])
    s += np.sum(P[P > inf+th*4])

    return s,         # кортеж

def mutShips(individual, indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] = random.randint(0, 1) if (i+1) % 3 == 0 else random.randint(1, POLE_SIZE)

    return individual,


toolbox.register("evaluate", shipsFitness)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutShips, indpb=1.0/LENGTH_CHROM)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)


def show(ax):
   # sleep(0.5)
    ax.clear()
    show_ships(ax, hof.items[0], POLE_SIZE)

    plt.draw()
    plt.gcf().canvas.flush_events()


plt.ion()
fig, ax = plt.subplots()
fig.set_size_inches(6, 6)

ax.set_xlim(-2, POLE_SIZE+3)
ax.set_ylim(-2, POLE_SIZE+3)

population, logbook = algelitism.eaSimpleElitism(population, toolbox,
                                        cxpb=P_CROSSOVER,
                                        mutpb=P_MUTATION,
                                        ngen=MAX_GENERATIONS,
                                        halloffame=hof,
                                        stats=stats,
                                        callback=(show, (ax, )),
                                        verbose=True)

maxFitnessValues, meanFitnessValues = logbook.select("min", "avg")

best = hof.items[0]
print(best)

plt.ioff()
plt.show()

# plt.plot(maxFitnessValues, color='red')
# plt.plot(meanFitnessValues, color='green')
# plt.xlabel('Поколение')
# plt.ylabel('Макс/средняя приспособленность')
# plt.title('Зависимость максимальной и средней приспособленности от поколения')
# plt.show()
#
