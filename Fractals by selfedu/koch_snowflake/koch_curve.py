#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Учебник по фракталам на Питон

Рисование кривой Коха - самого примитивного фрактала
(с) selfedu
"""

import turtle


def draw_koch_segment(t, ln):
    """
    draw_koch_segment(Turtle, int)

    draws segment of koch, using t = Turtle
    ln - length of segment
    """
    if ln > 6:
        ln3 = ln // 3
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
        t.right(120)
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
    else:

        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


t = turtle.Turtle()

t.ht()

t.speed(500)

draw_koch_segment(t, 150)

turtle.done()
