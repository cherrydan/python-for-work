#!/usr/bin/python3

# -*- coding: utf-8 -*-

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
        self.x = wx.StaticText(self, label='x:', pos=(10, 10))
        self.y = wx.StaticText(self, label='y:', pos=(10, 30))

        self.Bind(wx.EVT_MOTION, self.OnMove)

    def OnMove(self, event):
        x, y = event.GetPosition()
        self.x.SetLabel('x: ' + str(x))
        self.y.SetLabel('y: ' + str(y))


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
