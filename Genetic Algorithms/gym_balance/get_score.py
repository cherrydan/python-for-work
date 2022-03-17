#!/usr/bin/python3

from gym_balance import *


def get_score(individual):
    nnetwork.set_weights(individual)

    observation = env.reset()

    actionCounter = 0
    totalReward = 0

    done = False

    while not done and actionCounter < 500:
        actionCounter += 1
        action = int(nnetwork.predict(observation.reshape(-1, 1)))
        observation, reward, done, info = env.step(action)
        totalReward += reward

    return totalReward,
