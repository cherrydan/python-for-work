#!/usr/bin/python3

# -*- coding: utf-8 -*-

import numpy as np

from matplotlib.patches import Rectangle

v_ship = np.array([0, 1, 2, 3])
h_ship = np.array([0, 0, 0, 0])

type_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
colors = ['g', 'b', 'm', 'y']


def show_ships(ax, best, pole_size):
    rect = Rectangle((0, 0), pole_size + 1, pole_size + 1, fill=None, edgecolor='r')
    t_n = 0
    for i in range(0, len(best), 3):
        x = best[i]
        y = best[i + 1]
        r = best[i + 2]
        t = type_ship[t_n]
        t_n += 1
        if r == 1:
            ax.plot(v_ship[:t] + x, h_ship[:t] + y, 'sb', markersize=18, alpha=0.8,
                    markerfacecolor=colors[t - 1])
        else:
            ax.plot(h_ship[:t] + x, v_ship[:t] + y, 'sb', markersize=18, alpha=0.8,
                    markerfacecolor=colors[t - 1])

    ax.add_patch(rect)
