#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Рисование дракона Хартера-Хайтвея средствами
l-системы

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
f_len = 5  # длина одного сегмента прямой
f_angle = 90  # фиксированный угол поворота

axiom = "FX"

l_sys = LSystem2D(t, axiom, pen_width, f_len, f_angle)
l_sys.add_rules(("FX", "FX+FY+"), ("FY", "-FX-FY"))
l_sys.generate_path(12)
print(l_sys.state)
l_sys.draw_turtle((0, 0), 0)