#!/usr/bin/python3

# -*- coding: utf-8 -*-

from __future__ import division  # So 8/3 = 2.666 not 2
import wx
from math import sqrt  # So we can evaluate square roots

"""

Simple calculator on wxPython

(c) Cairocoders

"""


class Calc(wx.Dialog):
    """ Main calculator dialog window """

    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'wxCalculator')
        sizer = wx.BoxSizer(wx.VERTICAL)  # main vertical sizer

        # ___________________ v
        # calculation area
        self.display = wx.ComboBox(self, -1)
        sizer.Add(self.display, 0, wx.EXPAND)
        # [7][8][9][/]
        # [4][5][6][*]
        # [1][2][3][-]
        # [0][.][C][+]
        # digits and operations area

        gsizer = wx.GridSizer(4, 4, 4, 4)
        for row in (('7', '8', '9', '/'),
                    ('4', '5', '6', '*'),
                    ('1', '2', '3', '-'),
                    ('0', '.', 'C', '+')):
            for label in row:
                b = wx.Button(self, -1, label)
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)

        sizer.Add(gsizer, 1, wx.EXPAND)

        # [     =    ]
        # equals button here
        b = wx.Button(self, -1, '=')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b, 0, wx.EXPAND)
        self.equal = b

        # set sizer and center it
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()

    def OnButton(self, event):
        # gets title of clicked button
        label = event.GetEventObject().GetLabel()
        if label == '=':
            try:
                compute = self.display.GetValue()
                # ignore empty calculation
                if not compute.strip():
                    return
                # calculate result
                result = eval(compute)

                # add to history
                self.display.Insert(compute, 0)

                # show result
                self.display.SetValue(str(result))

            except Exception as e:
                wx.LogError(str(e))
                return

        elif label == 'C':
            # clears digits area
            self.display.SetValue('')
        else:
            # adds button text to current calculation
            self.display.SetValue(self.display.GetValue() + label)
            # sets focus on '=' button
            self.equal.SetFocus()


if __name__ == '__main__':
    # runs the app
    app = wx.App()
    dlg = Calc()
    dlg.ShowModal()
    dlg.Destroy()
