# Chapter 5: Providing Information and Alerting Users
# Recipe 3: SuperToolTip
#
import wx

#---- Recipe Code ----#
import wx.lib.agw.supertooltip as supertooltip

class SuperToolTipTestPanel(wx.Panel):
    def __init__(self, parent):
        super(SuperToolTipTestPanel, self).__init__(parent)

        # Attributes
        self.button = wx.Button(self, label="Go")
        msg = "Launches the shuttle"
        self.stip = supertooltip.SuperToolTip(msg)

        # Setup SuperToolTip
        bodybmp = wx.Bitmap("earth.png", wx.BITMAP_TYPE_PNG)
        self.stip.SetBodyImage(bodybmp)
        self.stip.SetHeader("Launch Control")
        footbmp = wx.Bitmap("warning.png", wx.BITMAP_TYPE_PNG)
        self.stip.SetFooterBitmap(footbmp)
        footer = "Warning: This is serious business"
        self.stip.SetFooter(footer)
        self.stip.ApplyStyle("XP Blue")
        self.stip.SetTarget(self.button)

        # Setup remaining
        self.timer = wx.Timer(self)
        self.count = 11

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 0, wx.ALIGN_CENTER)
        msizer = wx.BoxSizer(wx.HORIZONTAL)
        msizer.Add(sizer, 1, wx.ALIGN_CENTER)
        self.SetSizer(msizer)

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnGo, self.button)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

    def OnGo(self, event):
        self.button.Disable()
        print self.timer.Start(1000)
        tlw = self.GetTopLevelParent()
        tlw.PushStatusText("Launch initiated...")

    def OnTimer(self, event):
        tlw = self.GetTopLevelParent()
        self.count -= 1
        tlw.PushStatusText("%d" % self.count)
        if self.count == 0:
            self.timer.Stop()
            wx.MessageBox("Shuttle Launched!")

#---- End Recipe Code ----#

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="SuperToolTip", 
                             size=(300,200))
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        # Attributes
        self.panel = SuperToolTipTestPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.CreateStatusBar()
        self.PushStatusText("Hover the mouse over the button")

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
