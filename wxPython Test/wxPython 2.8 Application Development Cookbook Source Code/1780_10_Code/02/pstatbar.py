# Chapter 10: Creating Components and Extending Functionality
# Recipe 2: Adding Controls to a StatusBar
#
import wx

class ProgressStatusBar(wx.StatusBar):
    """Custom StatusBar with a built-in progress bar"""
    def __init__(self, parent, id_=wx.ID_ANY,
                 style=wx.SB_FLAT,
                 name="ProgressStatusBar"):
        super(ProgressStatusBar, self).__init__(parent,
                                                id_,
                                                style,
                                                name)
  
        # Attributes
        self._changed = False   # position has changed ?
        self.busy = False       # Bar in busy mode ?
        self.timer = wx.Timer(self)
        self.prog = wx.Gauge(self, style=wx.GA_HORIZONTAL)
        self.prog.Hide() # Hide on init

        # Layout
        self.SetFieldsCount(2)
        self.SetStatusWidths([-1, 155])

        # Event Handlers
        self.Bind(wx.EVT_IDLE, lambda evt: self.__Reposition())
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def __del__(self):
        if self.timer.IsRunning():
            self.timer.Stop()

    def __Reposition(self):
        """Repositions the gauge as necessary"""
        if self._changed:
            lfield = self.GetFieldsCount() - 1
            rect = self.GetFieldRect(lfield)
            prog_pos = (rect.x + 2, rect.y + 2)
            self.prog.SetPosition(prog_pos)
            prog_size = (rect.width - 8, rect.height - 4)
            self.prog.SetSize(prog_size)
        self._changed = False

    def OnSize(self, evt):
        self._changed = True
        self.__Reposition()
        evt.Skip()

    def OnTimer(self, evt):
        if not self.prog.IsShown():
            self.Stop()

        if self.busy:
            # In busy (indeterminate) mode
            self.prog.Pulse()

    def Run(self, rate=100):
        if not self.timer.IsRunning():
            self.timer.Start(rate)

    def GetProgress(self):
        return self.prog.GetValue()

    def SetProgress(self, val):
        if not self.prog.IsShown():
            self.ShowProgress(True)

        # Check if we are finished
        if val == self.prog.GetRange():
            self.prog.SetValue(0)
            self.ShowProgress(False)
        else:
            self.prog.SetValue(val)

    def SetRange(self, val):
        if val != self.prog.GetRange():
            self.prog.SetRange(val)

    def ShowProgress(self, show=True):
        self.__Reposition()
        self.prog.Show(show)

    def StartBusy(self, rate=100):
        self.busy = True
        self.__Reposition()
        self.ShowProgress(True)
        if not self.timer.IsRunning():
            self.timer.Start(rate)

    def StopBusy(self):
        self.timer.Stop()
        self.ShowProgress(False)
        self.prog.SetValue(0)   # Reset progress value
        self.busy = False

    def IsBusy(self):
        """Is the gauge busy?"""
        return self.busy
