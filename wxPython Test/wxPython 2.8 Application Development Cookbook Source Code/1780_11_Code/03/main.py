# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 3: Threading Tools
#
# Sample test module to test usage of threadtools module
import wx
import urllib2
import threading

import threadtools # <- Recipe module

class DownloaderThread(threading.Thread):
    def __init__(self, window):
        super(DownloaderThread, self).__init__()

        # Attributes
        self.window = window

    def run(self):
        """Fetch the text at the given url and update the UI"""
        # Get the URL from the UI
        url = self.window.GetURL() # safe because of synchfunct
        if not url:
            # Notify user that no URL was entered
            notify = Notifier()
            notify.ShowError("Must Enter a URL!")
            self.window.EnableFetch(True)
        else:
            try:
                if not url.startswith("http://"):
                    url = "http://" + url
                handle = urllib2.urlopen(url)
                txt = handle.read()
                handle.close()
            except Exception, msg:
                txt = str(msg)
            self.window.SetOutputText(txt) # Update text control
            self.window.EnableFetch(True) # Reenable button

class ThreadTipsApp(wx.App):
    def OnInit(self):
        self.frame = ThreadTipsFrame(None, title="Simple URL Fetcher")
        self.frame.Show()
        return True

class ThreadTipsFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(ThreadTipsFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ThreadTipsPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((400, 300))

class ThreadTipsPanel(wx.Panel):
    def __init__(self, parent):
        super(ThreadTipsPanel, self).__init__(parent)

        # Attributes
        self.output = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_RICH2)
        self.address = wx.TextCtrl(self)
        self.button = wx.Button(self, label="Get")

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnGetURL, self.button)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        # Setup hsizer
        hsizer.Add(wx.StaticText(self, label="URL: "), 0,
                   wx.ALIGN_CENTER_VERTICAL)
        hsizer.Add(self.address, 1, wx.EXPAND)
        hsizer.Add(self.button, 0, wx.LEFT, 5)

        # Finish layout
        vsizer.Add(self.output, 1, wx.EXPAND)
        vsizer.Add(hsizer, 0, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(vsizer)

    @threadtools.callafter
    def SetOutputText(self, text):
        self.output.SetValue(text)

    @threadtools.callafter
    def EnableFetch(self, enable):
        self.button.Enable(enable)

    @threadtools.synchfunct
    def GetURL(self):
        """Uses synchfunct since we need to get a return value"""
        return self.address.GetValue().strip()

    def OnGetURL(self, event):
        """Fetch the HTML from the URL"""
        self.thread = DownloaderThread(self)
        self.thread.start()
        self.EnableFetch(False)

class Notifier(object):
    """Sample class to show how to use the ClassSynchronizer
    to make all methods in a class thread safe.
    """
    __metaclass__ = threadtools.ClassSynchronizer

    def ShowWarning(self, msg):
        return wx.MessageBox(msg, style=wx.ICON_WARNING|wx.OK)

    def ShowError(self, msg):
        return wx.MessageBox(msg, style=wx.ICON_ERROR|wx.OK)


if __name__ == '__main__':
    app = ThreadTipsApp(False)
    app.MainLoop()
