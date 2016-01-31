# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 2: Persisting the UI's State
#
import wx
import os

class PersistentFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(PersistentFrame, self).__init__(*args, **kwargs)

        # Setup
        wx.CallAfter(self.RestoreState)

        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self._OnClose)

    def _OnClose(self, event):
        position = self.GetPosition()
        size = self.GetSize()
        cfg = wx.Config()
        cfg.Write('pos', repr(position.Get()))
        cfg.Write('size', repr(size.Get()))
        event.Skip()

    def RestoreState(self):
        """Restore the saved position and size"""
        cfg = wx.Config()
        name = self.GetName()
        position = cfg.Read(name + '.pos',
                            repr(wx.DefaultPosition))
        size = cfg.Read(name + '.size',
                        repr(wx.DefaultSize))
        # Turn strings back into tuples
        position = eval(position)
        size = eval(size)
        # Restore settings to Frame
        self.SetPosition(position)
        self.SetSize(size)

#---- Sample Application ----#

class PersistentApp(wx.App):
    def OnInit(self):
        self.SetAppName("PersistentTestApp")
        self.frame = TestFrame(None, title="Persistent Frame")
        self.frame.Show()
        return True

class TestFrame(PersistentFrame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(TestFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = TestPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class TestPanel(wx.Panel):
    def __init__(self, parent):
        super(TestPanel, self).__init__(parent)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, label="Resize then close the window")
        hsizer.AddStretchSpacer()
        hsizer.Add(label, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

if __name__ == '__main__':
    app = PersistentApp(False)
    app.MainLoop()
