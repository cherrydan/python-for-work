#!/usr/bin/python3

# -*- coding: utf-8 -*-
import time

import numpy as np

from gym_balance import *
from gym_balance.get_score import get_score

creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register('randomWeight', random.uniform, LOW, UP)
toolbox.register('individualCreator', tools.initRepeat, creator.Individual, toolbox.randomWeight, LENGTH_CHROM)
toolbox.register('populationCreator', tools.initRepeat, list, toolbox.individualCreator)

population = toolbox.populationCreator(n=POPULATION_SIZE)

toolbox.register('evaluate', get_score)
toolbox.register('select', tools.selTournament, tournsize=2)
toolbox.register('mate', tools.cxSimulatedBinaryBounded, low=LOW, up=UP, eta=ETA)
toolbox.register('mutate', tools.mutPolynomialBounded, low=LOW, up=UP, eta=ETA, indpb=1.0/LENGTH_CHROM)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register('max', np.max)
stats.register('avg', np.mean)

population, logbook = algelitism.eaSimpleElitism(population, toolbox,
                                                 cxpb=P_CROSSOVER,
                                                 mutpb=P_MUTATION,
                                                 ngen=MAX_GENERATIONS,
                                                 halloffame=hof,
                                                 stats=stats,
                                                 verbose=True)


best = hof.items[0]
print(best)

observation = env.reset()
action = int(nnetwork.predict(observation.reshape(-1, 1)))

while True:
    env.render()
    observation,reward, done, info = env.step(action)

    if done:
        break
    time.sleep(0.03)
    action = int(nnetwork.predict(observation.reshape(-1, 1)))

env.close()