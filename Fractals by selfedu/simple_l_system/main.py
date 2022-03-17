#!/usr/bin/python3
# -*- coding: utf-8 -*-
import turtle
from simple_l_system.l_system2D import LSystem2D

# ********** создаём окно 1200*600 строго в левом верхнем углу **********
WIDTH = 1200
HEIGHT = 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
# **********

t = turtle.Turtle()
t.ht()

pen_width = 2  # толщина линии рисования
f_len = 5  # длина одного сегмента прямой
f_angle = 90  # фиксированный угол поворота
axiom = "F+F+F+F"

l_sys = LSystem2D(t, axiom, pen_width, f_len, f_angle)
l_sys.add_rules(("F", "F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF"), ("S", "SSSSSS"))
l_sys.generate_path(2)
l_sys.draw_turtle((0, 0), 0)
