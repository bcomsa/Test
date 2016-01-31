# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 1: Non-Blocking GUI
#
import wx
import threading

class FibThread(threading.Thread):
    def __init__(self, window, n):
        super(FibThread, self).__init__()

        # Attributes
        self.window = window
        self.n = n

    def run(self):
        val = SlowFib(self.n)
        wx.CallAfter(self.window.output.SetValue, str(val))
        wx.CallAfter(self.window.StopBusy)

def SlowFib(n):
    """Calculate Fibonacci numbers
    using slow recursive method to demonstrate
    blocking the UI.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return SlowFib(n-1) + SlowFib(n-2)

class BlockingApp(wx.App):
    def OnInit(self):
        self.frame = BlockingFrame(None,
                                   title="Non-Blocking Gui")
        self.frame.Show()
        return True

class BlockingFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(BlockingFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = BlockingPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class BlockingPanel(wx.Panel):
    def __init__(self, parent):
        super(BlockingPanel, self).__init__(parent)

        # Attributes
        self.timer = wx.Timer(self)
        self.input = wx.SpinCtrl(self, value="35", min=1)
        self.output = wx.TextCtrl(self)
        self.block = wx.Button(self, label="Blocking")
        self.noblock = wx.Button(self, label="Non-Blocking")
        self.prog = wx.Gauge(self)

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_TIMER, self.OnPulse, self.timer)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        gridsz = wx.GridSizer(2, 2, 5, 5)

        # Layout controls
        vsizer.Add(self.prog, 0, wx.EXPAND)
        gridsz.Add(wx.StaticText(self, label="fib(n):"))
        gridsz.Add(self.input, 0, wx.EXPAND)
        gridsz.Add(wx.StaticText(self, label="result:"))
        gridsz.Add(self.output, 0, wx.EXPAND)
        vsizer.Add(gridsz, 0, wx.EXPAND|wx.ALL, 10)
        hsizer.Add(self.block, 0, wx.ALL, 5)
        hsizer.Add(self.noblock, 0, wx.ALL, 5)
        vsizer.Add(hsizer, 0, wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(vsizer)

    def OnButton(self, event):
        input = self.input.GetValue()
        self.output.SetValue("") # clear output
        self.StartBusy() # give busy feedback
        if event.GetEventObject() == self.block:
            # Calculate value in blocking mode
            val = SlowFib(input)
            self.output.SetValue(str(val))
            self.StopBusy()
        else:
            # Non-Blocking mode
            task = FibThread(self, input)
            task.start()

    def OnPulse(self, event):
        self.prog.Pulse() # Pulse busy feedback

    def StartBusy(self):
        self.timer.Start(100)
        self.block.Disable()
        self.noblock.Disable()

    def StopBusy(self):
        self.timer.Stop()
        self.prog.SetValue(0)
        self.block.Enable()
        self.noblock.Enable()

if __name__ == '__main__':
    app = BlockingApp(False)
    app.MainLoop()
