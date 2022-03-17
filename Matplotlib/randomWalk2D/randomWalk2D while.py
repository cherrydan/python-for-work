#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python code for 2D random walk.
# added by cherrydan: while loop, input statement for deep random walk
#                     color scheme

import numpy
import matplotlib.pyplot as plt
import random
import sys

# defining the number of steps
while True:
    try:
        n = int(input('How deep do you want random walk (min 1000 steps, max. 1.5 mil. steps)-> '))
        if n < 1000:
            print('Steps must be greather or equal 1000!')
            break
    except ValueError:
        print('You must input only number!')
        continue

    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    y = numpy.zeros(n)

    # filling the coordinates with random variables
    for i in range(1, n):
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1

    # plotting stuff:
    plt.title("Random Walk ($n = " + str(n) + "$ steps)")

    point_numbers = list(range(n))

    plt.scatter(x, y, c=point_numbers, cmap=plt.cm.Reds,
                edgecolors='none', s=15)

    # save random walk to file
    plt.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)

    # removing axes

    plt.axis('off')

    # plot random walk to screen
    plt.show()


