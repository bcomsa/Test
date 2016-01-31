# Chapter 10: Creating Components and Extending Functionality
# Recipe 2: Adding Controls to a StatusBar
#
import wx
import pstatbar

class ProgressBarApp(wx.App):
    def OnInit(self):
        self.frame = ProgressFrame(None,
                                   title="ProgressStatusBar")
        self.frame.Show()
        return True

class ProgressFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(ProgressFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ProgressPanel(self)

        # Setup
        bar = pstatbar.ProgressStatusBar(self)
        self.SetStatusBar(bar)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 100))

class ProgressPanel(wx.Panel):
    """Simple 2 button panel to test status bar out with"""
    def __init__(self, parent):
        super(ProgressPanel, self).__init__(parent)

        # Attributes
        self.busybtn = wx.Button(self, label="Start Busy")
        self.incbtn = wx.Button(self, label="Increment Gauge")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(self.busybtn, 0, wx.ALIGN_CENTER|wx.ALL, 10)
        hsizer.Add(self.incbtn, 0, wx.ALIGN_CENTER|wx.ALL, 10)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnButton(self, event):
        evt_obj = event.GetEventObject()
        frame = self.GetTopLevelParent()
        statbar = frame.GetStatusBar()
        if evt_obj == self.busybtn:
            if statbar.IsBusy():
                statbar.StopBusy()
                statbar.PushStatusText("Stopped busy mode.")
                evt_obj.SetLabel("Start Busy")
            else:
                statbar.StartBusy()
                statbar.PushStatusText("Started busy mode...")
                evt_obj.SetLabel("Stop Busy")
        else:
            # Increment the status by 10
            statbar.SetRange(100)
            cval = statbar.GetProgress() + 10
            if cval < 100:
                statbar.SetProgress(cval)
                statbar.PushStatusText("Updated to %d/100" % cval)
            else:
                statbar.SetProgress(cval)
                statbar.PushStatusText("Progress complete")

if __name__ == '__main__':
    app = ProgressBarApp(False)
    app.MainLoop()
