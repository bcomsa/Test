# Chapter 7: Window Layout and Design
# Recipe 4: Standard Dialog Button Sizer
#
import wx

#---- Recipe Code ----#

class CustomMessageBox(wx.Dialog):
    def __init__(self, parent, message, title="",
                 bmp=wx.NullBitmap, style=wx.OK):
        super(CustomMessageBox, self).__init__(parent, title=title)

        # Attributes
        self._flags = style
        self._bitmap = wx.StaticBitmap(self, bitmap=bmp)
        self._msg = wx.StaticText(self, label=message)

        # Layout
        self.__DoLayout()
        self.SetInitialSize()
        self.CenterOnParent()

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        # Layout the bitmap and caption
        hsizer.AddSpacer(10)
        hsizer.Add(self._bitmap, 0, wx.ALIGN_CENTER_VERTICAL)
        hsizer.AddSpacer(8)
        hsizer.Add(self._msg, 0, wx.ALIGN_CENTER_VERTICAL)
        hsizer.AddSpacer(10)

        # Create the buttons specified by the style flags
        # and the StdDialogButtonSizer to manage them
        btnsizer = self.CreateButtonSizer(self._flags)

        # Finish the layout
        vsizer.AddSpacer(10)
        vsizer.Add(hsizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        vsizer.AddSpacer(8)
        vsizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)

        self.SetSizer(vsizer)

#---- End Recipe Code ----#

class ButtonSizerApp(wx.App):
    def OnInit(self):
        self.frame = ButtonSizerFrame(None,
                                      title="Button Sizer")
        self.frame.Show()
        return True

class ButtonSizerFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = ButtonSizerPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class ButtonSizerPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.button = wx.Button(self, label="Show Dialog")

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        hsizer = wx.BoxSizer()
        hsizer.AddStretchSpacer()
        hsizer.Add(self.button, 0, wx.ALL, 20)
        hsizer.AddStretchSpacer()
        sizer.Add(hsizer, 0, wx.EXPAND)
        sizer.AddStretchSpacer()
        self.SetSizer(sizer)

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnShowDlg, self.button)

    def OnShowDlg(self, event):
        """Shows the dialog when our button is clicked"""
        msg = "Look at how my buttons are in the right places!"
        bmp = wx.Bitmap("./face-monkey.png")
        dlg = CustomMessageBox(self, msg, "Button Sizer", bmp,
                               style=wx.OK|wx.CANCEL)
        dlg.ShowModal()

if __name__ == '__main__':
    app = ButtonSizerApp(False)
    app.MainLoop()
