#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Уроки по GUI wxPython.
Использование пользовательского диалогового окна.
Модальное диалоговое окно. Вызов ShowModal() через менеджер with
(с) selfedu
"""
import wx


class MyDlg(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize(500, 150)

        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(wx.TextCtrl(self, wx.ID_ANY), flag=wx.EXPAND | wx.ALL, border=10)

        vh = wx.BoxSizer(wx.HORIZONTAL)
        btn_Ok = wx.Button(self, wx.ID_OK, label='Да', size=(100, 50))
        btn_Cn = wx.Button(self, wx.ID_CANCEL, label='Отмена', size=(100, 50))
        vh.Add(btn_Ok, flag=wx.LEFT, border=10)
        vh.Add(btn_Cn, flag=wx.LEFT, border=10)

        vb.Add(vh, flag=wx.ALIGN_CENTRE | wx.ALL, border=10)
        self.SetSizer(vb)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title, size=(600, 200))

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, 'Выход', wx.Bitmap('exit_32.png'))
        toolbar.AddSeparator()
        br_dialog = toolbar.AddTool(wx.ID_ANY, 'Диалог', wx.Bitmap('sound_32.png'))

        self.Bind(wx.EVT_TOOL, self.OnQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.OnDialog, br_dialog)

        self.style = wx.CAPTION | wx.CLOSE_BOX | wx.RESIZE_BORDER

    def OnQuit(self, event):
        self.Close()

    def OnDialog(self, event):
        with MyDlg(self, title='My Dialog', style=self.style) as dlg:
            res = dlg.ShowModal()

            if res == wx.ID_OK:
                print('Нажата кнопка Да')
            elif res == wx.ID_CANCEL:
                print('Нажата кнопка Отмена')


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
