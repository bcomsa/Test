# Chapter 5: Providing Information and Alerting Users
# Recipe 1: MessageBox
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="MessageBoxes", 
                             size=(300,200))
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        # Layout
        self.CreateStatusBar()
        self.PushStatusText("Close this window")

        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        result = wx.MessageBox("Are you sure you want "
                               "to close this window?",
                               style=wx.CENTER|\
                                     wx.ICON_QUESTION|\
                                     wx.YES_NO)
        if result == wx.NO:
            event.Veto()
        else:
            event.Skip()

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
