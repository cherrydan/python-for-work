#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Уроки по GUI wxPython.
Работа со стандартными виджетами
"""

import wx

TB_RED = 1
TB_GREEN = 2
TB_BLUE = 3


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title, size=(700, 550))
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText('Текст в статусной строке')

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(panel, label='Адрес: ')

        vbox.Add(st, flag=wx.ALL, border=10)

        imp = wx.TextCtrl(panel, value='г. Москва')
        vbox.Add(imp, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.BOTTOM, border=10)

        # разделительная вертикальная черта
        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        # создаём блок интерфейса при помощи GridBagSizer
        rtb = wx.ToggleButton(panel, id=TB_RED, label='red')
        gtb = wx.ToggleButton(panel, id=TB_GREEN, label='green')
        btb = wx.ToggleButton(panel, id=TB_BLUE, label='blue')

        # цвет для панели (по умолчанию - чёрный)
        self.col = wx.Colour(0, 0, 0)

        self.pn = wx.Panel(panel)
        self.pn.SetOwnBackgroundColour(self.col.GetAsString())

        vb1 = wx.GridBagSizer(10, 10)
        vb1.Add(rtb, (0, 0))
        vb1.Add(gtb, (1, 0))
        vb1.Add(btb, (2, 0))
        vb1.Add(self.pn, (0, 1), (3, 1), flag=wx.EXPAND)
        vb1.AddGrowableCol(1)

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)

        vbox.Add(vb1, flag=wx.EXPAND | wx.ALL, border=10)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)

        # сайзер StaticBox
        pn2 = wx.Panel(panel)
        wx.StaticBox(pn2, label='Ваш пол:', size=(150, 50))
        rd1 = wx.RadioButton(pn2, label='Муж.', pos=(10, 20), style=wx.RB_GROUP)
        rd2 = wx.RadioButton(pn2, label='Жен.', pos=(80, 20))

        vb2 = wx.BoxSizer(wx.HORIZONTAL)
        vb2.Add(pn2)

        agree = wx.CheckBox(panel, label='Согласен на обработку')
        agree.SetValue(True)
        vb2.Add(agree, flag=wx.LEFT | wx.TOP, border=20)

        links = ['Телефон', 'Email', 'Skype']
        cb = wx.ComboBox(panel, pos=(50, 30), choices=links, style=wx.CB_READONLY)
        cb.SetSelection(0)
        vb2.Add(cb, flag=wx.LEFT | wx.TOP, border=15)

        vbox.Add(vb2, flag=wx.EXPAND | wx.ALL, border=10)

        self.gauge = wx.Gauge(panel, range=100)
        vbox.Add(self.gauge, flag=wx.EXPAND | wx.ALL, border=10)

        bStart = wx.Button(panel, label='Старт')
        bStop = wx.Button(panel, label='Стоп')

        hb3 = wx.BoxSizer()

        hb3.AddMany([(bStart, 0, wx.LEFT | wx.RIGHT, 10), (bStop, 0, wx.LEFT | wx.RIGHT, 10)])
        vbox.Add(hb3, flag=wx.ALIGN_CENTRE)

        bStart.Bind(wx.EVT_BUTTON, self.OnStart)
        bStop.Bind(wx.EVT_BUTTON, self.OnStop)

        self.count = 0
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.gauge.SetValue(self.count)

        sld = wx.Slider(panel, value=50, minValue=0, maxValue=100, style=wx.HORIZONTAL)
        vbox.Add(sld, flag=wx.EXPAND | wx.ALL, border=10)

        sld.Bind(wx.EVT_SCROLL, self.OnScroll)

        panel.SetSizer(vbox)

    def OnTimer(self, e):
        self.count += 1
        self.gauge.SetValue(self.count)

        if self.count >= 100:
            self.timer.Stop()

    def OnStop(self, e):
        self.timer.Stop()
        self.count = 0

    def OnStart(self, e):
        if self.count > 100:
            return
        self.timer.Start(100)

    def OnToggle(self, e):
        btn = e.GetEventObject()
        val = 255 if btn.GetValue() else 0
        id_ = btn.GetId()

        r = self.col.Red()
        g = self.col.Green()
        b = self.col.Blue()

        if id_ == TB_RED:
            self.col.Set(val, g, b)
        elif id_ == TB_BLUE:
            self.col.Set(r, g, val)
        elif id_ == TB_GREEN:
            self.col.Set(r, val, b)

        self.pn.SetBackgroundColour(self.col)
        self.pn.Refresh()

    def OnScroll(self, e):
        val = e.GetEventObject().GetValue()
        self.sb.SetStatusText(
            'Громкость: ' + str(val)
        )


app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()
