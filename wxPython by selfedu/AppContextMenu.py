# -*- coding: utf-8 -*-

"""

Помещаем контекстное меню в отдельный класс

"""
import wx


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        # создаём пункты меню
        it_min = self.Append(wx.ID_ANY, 'Минимизировать')
        it_max = self.Append(wx.ID_ANY, 'Распахнуть')

        # и привязываем обработчики
        self.Bind(wx.EVT_MENU, self.on_minimize, it_min)
        self.Bind(wx.EVT_MENU, self.on_maximize, it_max)

    def on_minimize(self, event):
        self.parent.Iconize()

    def on_maximize(self, event):
        self.parent.Maximize()
