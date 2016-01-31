# Chapter 3: An Applications Building Blocks, Basic Controls
# Recipe 2: Stock Buttons
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Stock Buttons")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        # Attributes
        self.panel = MyPanel(self)

        # Layout
        sizer = wx.BoxSizer()
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()
        
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # Make some buttons
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for bid in (wx.ID_OK, wx.ID_CANCEL,
                    wx.ID_APPLY, wx.ID_HELP):
            button = wx.Button(self, bid)
            sizer.Add(button, 0, wx.ALL, 5)
        self.SetSizer(sizer)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
