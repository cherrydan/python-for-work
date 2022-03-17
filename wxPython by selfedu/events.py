#!/usr/bin/python3

# -*- coding: utf-8 -*-

import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
        panel = wx.Panel(self)
        btn = wx.Button(panel, wx.ID_ANY, 'Нажать')
        btn.Bind(wx.EVT_BUTTON, self.OnButton)
        panel.Bind(wx.EVT_BUTTON, self.OnButtonPanel)
        panel.Unbind(wx.EVT_BUTTON)
        self.Bind(wx.EVT_BUTTON, self.OnButtonFrame)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnButton(self, event):
        print('Уровень кнопки')
        event.Skip()

    def OnButtonPanel(self, event):
        print('Уровень панели')
        event.Skip()

    def OnButtonFrame(self, event):
        print('Уровень фрейма')
        event.Skip()


    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?',
                                'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

app = wx.App()

frame = MyFrame(None, 'wxPython')
frame.Centre()
frame.Show()

app.MainLoop()
