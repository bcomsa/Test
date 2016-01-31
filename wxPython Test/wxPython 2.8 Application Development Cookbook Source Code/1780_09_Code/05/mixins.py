# Chapter 9: Design Approaches and Techniques
# Recipe 5: Using Mixin Classes
#
import os
import time
import wx

class LoggerMixin:
    def __init__(self, logfile="log.txt"):
        """@keyword logfile: path to log output file"""
        # Attributes
        self.logfile = logfile

    def Log(self, msg):
        """Write a message to the log.
        Automatically adds timestamp and originating class
        information.
        """
        if self.logfile is None:
            return

        # Open and write to the log file
        with open(self.logfile, 'ab') as handle:
            # Make a time stamp
            ltime = time.localtime(time.time())
            tstamp = "%s:%s:%s" % (str(ltime[3]).zfill(2),
                                   str(ltime[4]).zfill(2),
                                   str(ltime[5]).zfill(2))
            # Add client info
            client = getattr(self, 'GetName',
                             lambda: "unknown")()
            # Construct the final message
            output = "[%s][%s] %s%s" % (tstamp, client,
                                        msg, os.linesep)
            handle.write(output)

class MixinRecipeApp(wx.App, LoggerMixin):
    def __init__(self, *args, **kwargs):
        LoggerMixin.__init__(self)
        wx.App.__init__(self, *args, **kwargs)

    def OnInit(self):
        self.Log("OnInit called")
        self.frame = MixinRecipeFrame(None,
                                      title="Mixin Classes")
        self.frame.Show()
        return True

class MixinRecipeFrame(wx.Frame, LoggerMixin):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)
        LoggerMixin.__init__(self)
        self.Log("Creating instance...")

        # Attributes
        self.panel = MixinRecipePanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class MixinRecipePanel(wx.Panel, LoggerMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        LoggerMixin.__init__(self)

        # Attributes
        self.button = wx.Button(self, label="FooBar")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        self.Log("Begin Layout")
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.AddWindow(self.button)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)
        self.Log("End Layout")

    def OnButton(self, event):
        self.Log("Button %d: Clicked" % event.GetId())

if __name__ == '__main__':
    app = MixinRecipeApp(False)
    app.MainLoop()
