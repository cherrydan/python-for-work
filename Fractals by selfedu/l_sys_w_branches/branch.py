#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Рисование ветки средствами
l-системы со стеком

(с) selfedu
"""
import turtle

from l_system2D import LSystem2D

# ********** создаём окно 1200*600 строго в левом верхнем углу **********
WIDTH = 1200
HEIGHT = 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
# **********

t = turtle.Turtle()
t.ht()
t.speed(1000)

pen_width = 2  # толщина линии рисования
f_len = 8  # длина одного сегмента прямой
f_angle = 33  # фиксированный угол поворота

axiom = "A"

l_sys = LSystem2D(t, axiom, pen_width, f_len, f_angle)
l_sys.add_rules(("F", "FF"), ("A", "F[+A][-A]"))
l_sys.generate_path(5)
print(l_sys.state)
l_sys.draw_turtle((0, -200), 90)
