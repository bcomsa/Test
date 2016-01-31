# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 4: Exception Handling
#
import wx
import sys
import traceback

def ExceptionHook(exctype, value, trace):
    """Handler for all unhandled exceptions
    @param exctype: Exception Type
    @param value: Error Value
    @param trace: Trace back info
    """
    # Format the traceback
    exc = traceback.format_exception(exctype, value, trace)
    ftrace = "".join(exc)
    app = wx.GetApp()
    if app:
        msg = "An unexpected error has occurred: %s" % ftrace
        wx.MessageBox(msg, app.GetAppName(),
                      style=wx.ICON_ERROR|wx.OK)
        app.Exit()
    else:
        sys.stderr.write(ftrace)

class ExceptionHandlerApp(wx.App):
    def OnInit(self):
        sys.excepthook = ExceptionHook
        return True

#---- Sample Application ----#

class TestApp(ExceptionHandlerApp):
    def OnInit(self):
        rval = super(TestApp, self).OnInit()
        self.SetAppName("Exception Handling")
        self.frame = TestFrame(None,
                               title="Exception Handling")
        self.frame.Show()
        return rval

class TestFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(TestFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = TestPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class TestPanel(wx.Panel):
    def __init__(self, parent):
        super(TestPanel, self).__init__(parent)

        # Attributes
        self.button = wx.Button(self, label="Crash Me!")

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(self.button, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnButton(self, event):
        raise Exception("CRASHED!")

if __name__ == '__main__':
    app = TestApp(False)
    app.MainLoop()
