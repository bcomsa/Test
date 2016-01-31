# Chapter 1: Getting Started
# Recipe 10: Two Stage Widget Creation
#
import wx

#-----------------------------------------------------------------------------#

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Two Stage Creation")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        pre = wx.PreFrame()
        pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
        pre.Create(parent, *args, **kwargs)
        self.PostCreate(pre)

        # Attributes
        self.panel = wx.Panel(self)

        # Setup
        self.CreateStatusBar()
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_HELP, self.OnHelp)

    def __DoLayout(self):
        """Layout the window"""
        # Layout the controls using a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add some buttons
        for x in range(5):
            btn = wx.Button(self.panel, label="Button %d" % x)
            sizer.Add(btn)
        self.panel.SetSizer(sizer)
        
        msizer = wx.BoxSizer()
        msizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(msizer)
        self.SetInitialSize(size=(300, 200))

    def OnHelp(self, evt):
        obj = evt.GetEventObject()
        self.PushStatusText("Help requested for: %s" % obj.GetLabel())

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
