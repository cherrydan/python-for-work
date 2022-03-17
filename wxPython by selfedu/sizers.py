#!/usr/bin/python3

# -*- coding: utf-8 -*-

# *********************************************************************
# импровизированный калькулятор (болванка интерфейса) с использованием
# BoxSizer и GridSizer
# (c) selfedu
# ********************************************************************

import wx
from const import *


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        # grid-sizer с кнопками для калькулятора
        gbox = wx.GridSizer(5, 4, 5, 5)
        gbox.AddMany([(wx.Button(panel, label='Cls'), CLS, wx.EXPAND),
                      (wx.Button(panel, label='Bck'), BCK, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='Close'), CLOSE, wx.EXPAND),
                      (wx.Button(panel, label='7'), SEVEN, wx.EXPAND),
                      (wx.Button(panel, label='8'), EIGHT, wx.EXPAND),
                      (wx.Button(panel, label='9'), NINE, wx.EXPAND),
                      (wx.Button(panel, label='/'), DIV, wx.EXPAND),
                      (wx.Button(panel, label='4'), FOUR, wx.EXPAND),
                      (wx.Button(panel, label='5'), FIVE, wx.EXPAND),
                      (wx.Button(panel, label='6'), SIX, wx.EXPAND),
                      (wx.Button(panel, label='*'), MUL, wx.EXPAND),
                      (wx.Button(panel, label='1'), ONE, wx.EXPAND),
                      (wx.Button(panel, label='2'), TWO, wx.EXPAND),
                      (wx.Button(panel, label='3'), THREE, wx.EXPAND),
                      (wx.Button(panel, label='-'), MINUS, wx.EXPAND),
                      (wx.Button(panel, label='0'), ZERO, wx.EXPAND),
                      (wx.Button(panel, label='.'), POINT, wx.EXPAND),
                      (wx.Button(panel, label='='), EQ, wx.EXPAND),
                      (wx.Button(panel, label='+'), PLUS, wx.EXPAND)

                      ])
        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
