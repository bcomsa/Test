# Chapter 2: Responding to Events
# Recipe 9: AppleEvents
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="AppleEvents")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

    def MacNewFile(self):
        """Called for an open-application event"""
        self.frame.PushStatusText("MacNewFile Called")

    def MacOpenFile(self, filename):
        """Called for an open-document event"""
        self.frame.PushStatusText("MacOpenFile: %s" % filename)

    def MacOpenURL(self, url):
        """Called for a get-url event"""
        self.frame.PushStatusText("MacOpenURL: %s" % url)

    def MacPrintFile(self, filename):
        """Called for a print-document event"""
        self.frame.PushStatusText("MacPrintFile: %s" % filename)

    def MacReopenApp(self):
        """Called for a reopen-application event"""
        self.frame.PushStatusText("MacReopenApp")
        # Raise the application from the Dock
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        self.frame.Raise()


class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = wx.Panel(self)
        self.CreateStatusBar()

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
