# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 5: Capturing Output
#
import wx
import outputwin # <- Recipe module

class PingApp(wx.App):
    def OnInit(self):
        self.frame = PingFrame(None, title="Ping O' Matic")
        self.frame.Show()
        return True

class PingFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(PingFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = PingPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((400, 300))

class PingPanel(wx.Panel):
    def __init__(self, parent):
        super(PingPanel, self).__init__(parent)

        # Attributes
        self.output = outputwin.OutputWindow(self)
        self.address = wx.TextCtrl(self)
        self.ping = wx.Button(self, label="Ping")

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.ping)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        # Setup hsizer
        hsizer.Add(wx.StaticText(self, label="Address: "), 0,
                   wx.ALIGN_CENTER_VERTICAL)
        hsizer.Add(self.address, 1, wx.EXPAND)
        hsizer.Add(self.ping, 0, wx.LEFT, 5)

        # Finish layout
        vsizer.Add(self.output, 1, wx.EXPAND)
        vsizer.Add(hsizer, 0, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(vsizer)

    def OnStart(self, event):
        """Start pinging website"""
        url = self.address.GetValue().strip()
        if not url:
            wx.MessageBox("Must enter a URL to ping!")
        else:
            self.output.StartProcess("ping %s" % url, blocksize=64)

if __name__ == '__main__':
    app = PingApp(False)
    app.MainLoop()
