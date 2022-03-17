#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Уроки по GUI wxPython.
Использование стандартных диалоговых окон
(с) selfedu
"""

import wx

from AppContextMenu import AppContextMenu

APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_sRGB = 4

ID_SOUND = 5
ID_SOUND_ON = 6
ID_SOUND_OFF = 7


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        menubar = wx.MenuBar()
        file_menu = wx.Menu()

        # создаём подменю
        exp_menu = wx.Menu()
        exp_menu.Append(wx.ID_ANY, 'Экспорт &изображения\tCtrl+I')
        exp_menu.Append(wx.ID_ANY, 'Экспорт &видео\tCtrl+V')
        exp_menu.Append(wx.ID_ANY, 'Экспорт &данных\tCtrl+D')

        # добавляем стандартные пункты меню Файл
        file_menu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        file_menu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        file_menu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        file_menu.AppendSubMenu(exp_menu, "&Экспорт\tCtrl+E")
        file_menu.AppendSeparator()

        # создаём меню типа чекбокса
        view_menu = wx.Menu()
        self.v_status = view_menu.Append(VIEW_STATUS, 'Статусная строка', kind=wx.ITEM_CHECK)
        self.v_rgb = view_menu.Append(VIEW_RGB, 'Тип RGB', kind=wx.ITEM_RADIO)
        self.v_srgb = view_menu.Append(VIEW_sRGB, 'Тип sRGB', kind=wx.ITEM_RADIO)

        # создаём контекстное меню
        self.ctx = AppContextMenu(self)

        # назначаем горячую клавишу
        item = wx.MenuItem(file_menu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        # назначаем иконку для меню
        item.SetBitmap(wx.Bitmap('exit.png'))
        file_menu.Append(item)
        menubar.Append(file_menu, '&Файл')
        menubar.Append(view_menu, 'Вид')
        self.SetMenuBar(menubar)
        # вешаем обработчик на меню
        self.Bind(wx.EVT_MENU, self.on_close, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.on_status, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.on_imageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.on_imageType, id=VIEW_sRGB)

        # обрабатываем нажатие правой кнопки мыши в области приложения
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_rightDown)

        # создаём и выводим тулбар
        toolbar = self.CreateToolBar()
        # кнопку
        br_quit = toolbar.AddTool(wx.ID_EXIT, 'Выход', wx.Bitmap('exit_32.png'))
        # и обработчик
        self.Bind(wx.EVT_TOOL, self.on_close, br_quit)
        toolbar.AddSeparator()
        br_redo = toolbar.AddTool(wx.ID_REDO, 'Вернуть', wx.Bitmap('redo_32.png'))
        br_undo = toolbar.AddTool(wx.ID_UNDO, 'Откатить', wx.Bitmap('undo_32.png'))

        toolbar.EnableTool(wx.ID_REDO, False)
        toolbar.AddSeparator()
        br_sound = toolbar.AddTool(ID_SOUND, "", wx.Bitmap('sound_32.png'))

        br_soundOn = toolbar.AddCheckTool(ID_SOUND_ON, "", wx.Bitmap('sound_on32.png'))
        br_soundOff = toolbar.AddCheckTool(ID_SOUND_ON, "", wx.Bitmap('sound_off32.png'))

    # событие на меню Выход
    def on_close(self, event):
        dlg = wx.MessageBox('Вы действительно хотите выйти из программы', 'Вопрос',
                            wx.YES_NO | wx.NO_DEFAULT, self)
        if dlg == wx.YES:
            print('Нажата кнока Yes')
            self.Close()
        elif dlg == wx.NO:
            print('Нажата кнопка No')

    # событие на меню Статусная строка
    def on_status(self, event):
        if self.v_status.IsChecked():
            print('Показывать статусную строку')
        else:
            print('Скрывать статусную строку')

    # событие на радиоменю
    def on_imageType(self, event):
        if self.v_rgb.IsChecked():
            print('Выбран режим RGB')
        elif self.v_srgb.IsChecked():
            print('Выбран режим sRGB')

    def on_rightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())


app = wx.App()

frame = MyFrame(None, 'Hello, world!')
frame.Centre()
frame.Show()

app.MainLoop()
