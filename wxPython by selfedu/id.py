# -*- coding: utf-8 -*-

import wx
"""
Простое назначение id
BUTTON1 = 1
BUTTON2 = 2
"""

# назначение id при помощи генератора id
BUTTON1 = wx.NewIdRef()
BUTTON2 = wx.NewIdRef() # вернёт объект WindowIdRef у которого надо будет взять GetId

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 300))
        # № id кнопкам будет выделять библиотека
        b1 = wx.Button(self, wx.ID_SAVE, label='Кнопка1')
        b2 = wx.Button(self, BUTTON2.GetId(), label='Кнопка2')  # wx.ID_ANY это тоже, что и -1, и автоматом задаются
        # только отрицательные id

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(b2, flag=wx.EXPAND | wx.ALL, border=10)

        self.SetSizer(vbox)

        # получаем id виджетов и выводим их
        print(b1.GetId(), b2.GetId(), sep='\n')


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
