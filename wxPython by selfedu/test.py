#!/usr/bin/python3

# -*- coding: utf-8 -*-

import wx

app = wx.App()

frame = wx.Frame(None, title='Hello, world!', style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
frame.Centre()
frame.Show()

app.MainLoop()
