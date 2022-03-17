#!/usr/bin/python3

# -*- coding: utf-8 -*-

import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
        self.counter = 0

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.counter += 1
        print('Событие EVT_PAINT сработало ' + str(self.counter) + ' раз(а)')
        dc = wx.PaintDC(self)
        dc.DrawLine(0, 0, 100, 100)


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
