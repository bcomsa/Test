# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 2: Understanding Thread Safety
#
import wx
import time
import threading

# Define a new custom event type
wxEVT_THREAD_UPDATE = wx.NewEventType()
EVT_THREAD_UPDATE = wx.PyEventBinder(wxEVT_THREAD_UPDATE, 1)
class ThreadUpdateEvent(wx.PyCommandEvent):
    def __init__(self, eventType, id):
        super(ThreadUpdateEvent, self).__init__(eventType, id)

        # Attributes
        self.value = None

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value

class CountingThread(threading.Thread):
    """Simple thread that sends an update to its 
    target window once a second with the new count value.
    """
    def __init__(self, targetwin, id):
        super(CountingThread, self).__init__()

        # Attributes
        self.window = targetwin
        self.id = id
        self.count = 0
        self.stop = False

    def run(self):
        while not self.stop:
            time.sleep(1) # wait a second
            # Notify the main thread its time to update the ui
            if self.window:
                event = ThreadUpdateEvent(wxEVT_THREAD_UPDATE,
                                          self.id)
                event.SetValue(self.count)
                wx.PostEvent(self.window, event)
            self.count += 1

    def Stop(self):
        # Stop the thread
        self.stop = True

class ThreadSafetyApp(wx.App):
    def OnInit(self):
        self.frame = ThreadSafeFrame(None,
                                     title="Thread Safety")
        self.frame.Show()
        return True

class ThreadSafeFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(ThreadSafeFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ThreadSafePanel(self)
        self.threadId = wx.NewId()
        self.worker = CountingThread(self, self.threadId)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

        # Start the worker thread
        self.worker.start()

        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(EVT_THREAD_UPDATE, self.OnThreadEvent)

    def OnClose(self, event):
        # Stop the worker thread
        self.worker.Stop()
        event.Skip()

    def OnThreadEvent(self, event):
        if event.GetId() == self.threadId():
            # Handle event to update Displayed Count
            value = event.GetValue()
            self.panel.DisplayCount(value)
        else:
            event.Skip()

class ThreadSafePanel(wx.Panel):
    def __init__(self, parent):
        super(ThreadSafePanel, self).__init__(parent)

        # Attributes
        self.count = wx.StaticText(self, label="Count: ")

        # Setup
        self.__DoLayout()

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.Add(self.count)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def DisplayCount(self, value):
        self.count.SetLabel("Count: %d" % value)

if __name__ == '__main__':
    app = ThreadSafetyApp(False)
    app.MainLoop()

