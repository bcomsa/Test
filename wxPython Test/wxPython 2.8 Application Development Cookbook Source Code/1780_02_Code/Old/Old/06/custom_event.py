# Chapter 2: Responding to Events
# Recipe 6: Custom Events
#
import wx
import wx.lib.newevent as newevent

MyEvent, EVT_MY_EVENT = wx.lib.newevent.NewCommandEvent()

myEVT_TIME_EVENT = wx.NewEventType()
EVT_MY_TIME_EVENT = wx.PyEventBinder(myEVT_TIME_EVENT, 1)
class MyTimeEvent(wx.PyCommandEvent):
    def __init__(self, id=0, time="12:00:00"):
        evttype = myEVT_TIME_EVENT
        super(MyTimeEvent, self).__init__(evttype, id)

        # Attributes
        self.time = time

    def GetTime(self):
        return self.time

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Custom Events")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        # Attributes
        self.panel = wx.Panel(self)
        self.evt_btn = wx.Button(self.panel, label="Send EVT_MY_EVENT")
        self.time_btn = wx.Button(self.panel, label="Send EVT_MY_TIME_EVENT")

        # Panel Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.evt_btn, 0, wx.ALL|wx.ALIGN_CENTER, 10)
        sizer.Add(self.time_btn, 0, wx.ALL|wx.ALIGN_CENTER, 10)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.AddStretchSpacer()
        vsizer.Add(sizer, 0, wx.ALIGN_CENTER)
        vsizer.AddStretchSpacer()
        self.panel.SetSizer(vsizer)
        # Frame Layout
        self.CreateStatusBar()
        fsizer = wx.BoxSizer(wx.VERTICAL)
        fsizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(fsizer)
        self.SetInitialSize()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnSendEvent)
        self.Bind(EVT_MY_EVENT, self.OnMyEvent)
        self.Bind(EVT_MY_TIME_EVENT, self.OnMyTimeEvent)

    def OnSendEvent(self, event):
        e_obj = event.GetEventObject()
        if e_obj == self.evt_btn:
            # Send a EVT_MY_EVENT
            new_evt = MyEvent(self.GetId())
        else:
            # Send a EVT_MY_TIME_EVENT
            ctime = wx.DateTime_Now().FormatTime()
            new_evt = MyTimeEvent(self.GetId(), ctime)

        # Post the event to the event queue
        new_evt.SetEventObject(self)
        wx.PostEvent(self.panel, new_evt)

    def OnMyEvent(self, event):
        self.PushStatusText("EVT_MY_EVENT Recieved")

    def OnMyTimeEvent(self, event):
        self.PushStatusText("EVT_MY_TIME_EVENT Recieved: %s" % event.GetTime())

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
