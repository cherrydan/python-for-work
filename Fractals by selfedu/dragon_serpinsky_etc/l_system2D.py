#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle


class LSystem2D:
    # конструктор
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom  # инициатор 'F' в нашем наборе команд черепашки
        self.state = axiom  # строка с набором комманд черепашки (пока это только 'F'
        self.width = width  # толшина линии рисования
        self.length = length  # длина одного сегмента кривой
        self.angle = angle  # угол поворота черепашки
        self.t = t  # сама черепашка для рисования
        self.t.pensize(self.width)  # устанавливаем толщину линии рисования
        self.rules = {}  # словарь для задания правил рисования кривых

    # TODO: write add_rules method (10:16 in video)
    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    # TODO: write generate_path method (11:24 in video)
    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())
            self.state = self.state.upper()

    # черепашка рисует сегмент, распарсивая набор комманд
    def draw_turtle(self, start_pos, start_angle):
        """
        This method
        draws segment from start pos and start angle
        """
        # ***** установка черепашки *****
        turtle.tracer(1, 0)  # врубаем форсажный режим
        self.t.up()  # поднимаем перо, для того чтобы, устанавливаемая на нач. позиции черепашка не рисовала
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()  # опускаем перо
        # ***** рисование *****

        # пробегаемся по строке с коммандами
        # TODO: добавляем команду 'S' - позволяющую черепашке перескакивать в заданную точку
        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()
