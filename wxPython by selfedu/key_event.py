# -*- coding: utf-8 -*-
# Note: There is a problem in wxPython to handle keyboard events in Linux
# I've combined this example from https://github.com/wxWidgets/Phoenix/issues/1144 and selfedu tutor
import wx
import wx.stc


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Key test")
        self.SetSize((600, 500))

        self.textCrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.styledTextCtrl = wx.stc.StyledTextCtrl(self)
        self.styledTextCtrl.SetFocus()
        self.logCtrl = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE)

        self.textCrl.Bind(wx.EVT_KEY_DOWN, handler=self._onTextCtrlKeyDown)
        self.styledTextCtrl.Bind(wx.EVT_KEY_DOWN, handler=self._onStyledTextCtrlKeyDown)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textCrl, 1, wx.EXPAND)
        sizer.Add(self.styledTextCtrl, 1, wx.EXPAND)
        sizer.Add(self.logCtrl, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def _onTextCtrlKeyDown(self, event):
        key = event.GetKeyCode()
        if key != wx.WXK_ESCAPE:
            text = '[TextCtrl] EVT_KEY_DOWN. Key code = {}\n'.format(key)
            self.logCtrl.AppendText(text)
        else:
            ret = wx.MessageBox('Вы действительно хотите выйти?', 'Вопрос', wx.YES_NO | wx.NO_DEFAULT, self)
            if ret == wx.YES:
                self.Close()
        event.Skip()

    def _onStyledTextCtrlKeyDown(self, event):
        key = event.GetKeyCode()
        if key != wx.WXK_ESCAPE:
            text = '[TextCtrl] EVT_KEY_DOWN. Key code = {}\n'.format(key)
            self.logCtrl.AppendText(text)
        else:
            ret = wx.MessageBox('Вы действительно хотите выйти?', 'Вопрос', wx.YES_NO | wx.NO_DEFAULT, self)
            if ret == wx.YES:
                self.Close()

        event.Skip()


if __name__ == '__main__':
    app = wx.App(0)

    frame = MyFrame(None)
    app.SetTopWindow(frame)
    frame.Show()

    app.MainLoop()