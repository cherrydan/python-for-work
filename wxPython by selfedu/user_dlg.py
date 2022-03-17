#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Уроки по GUI wxPython.
Использование пользовательского диалогового окна.
Не модальное диалоговое окно.
(с) selfedu
"""
import wx


class MyDlg(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, e):
        self.Destroy()
        self.parent.dlg = None


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title, size=(600, 200))

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, 'Выход', wx.Bitmap('exit_32.png'))
        toolbar.AddSeparator()
        br_dialog = toolbar.AddTool(wx.ID_ANY, 'Диалог', wx.Bitmap('sound_32.png'))

        self.Bind(wx.EVT_TOOL, self.OnQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.OnDialog, br_dialog)
        self.dlg = None

    def OnQuit(self, event):
        self.Close()

    def OnDialog(self, event):
        if self.dlg is None:
            self.dlg = MyDlg(self, title='Мой диалог...')
            res = self.dlg.Show()

        # mydlg.Destroy()
        # print(res)


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
