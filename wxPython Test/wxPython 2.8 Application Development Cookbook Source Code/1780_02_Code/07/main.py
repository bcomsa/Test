# Chapter 2: Responding to Events
# Recipe 7: Managing Events with EventStack
#
# This is the sample application that uses the recipe
# presented in the topic "Managing Events with EventStack"
#
import wx
import appevtmgr # <- Our recipe file

class MyApp(appevtmgr.EventMgrApp):
    def OnInit(self):
        self.frame = MyFrame(None, title="EventStackApp")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(appevtmgr.EventMgrFrame):
    def __init__(self, parent, *args, **kwargs):
        appevtmgr.EventMgrFrame.__init__(self, parent,
                                         *args, **kwargs)

        # Attributes
        self.panel = wx.Panel(self)
        self.txt = wx.TextCtrl(self.panel,
                               value="Hello World",
                               style=wx.TE_MULTILINE)

        # Add a MenuBar
        menub = wx.MenuBar()
        filem = wx.Menu()
        filem.Append(wx.ID_NEW, "New\tCtrl+N")
        menub.Append(filem, "File")
        editm = wx.Menu()
        editm.Append(wx.ID_CUT, "Cut\tCtrl+X")
        editm.Append(wx.ID_COPY, "Copy\tCtrl+C")
        editm.Append(wx.ID_PASTE, "Paste\tCtrl+P")
        editm.Append(wx.ID_SELECTALL, "Select All\tCtrl+A")
        menub.Append(editm, "Edit")
        self.SetMenuBar(menub)

        # Add a ToolBar
        toolb = wx.ToolBar(self)
        for itemid, bmpid in [(wx.ID_CUT, wx.ART_CUT),
                              (wx.ID_COPY, wx.ART_COPY),
                              (wx.ID_PASTE, wx.ART_PASTE)]:
            bmp = wx.ArtProvider.GetBitmap(bmpid, wx.ART_TOOLBAR)
            toolb.AddTool(itemid, bmp)
        toolb.Realize()
        self.SetToolBar(toolb)

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txt, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar()

        # Event Handlers
        # Use the base classes Register* methods instead
        # of the usual Bind.
        self.RegisterMenuHandler(wx.ID_NEW, self.OnNewWindow)
        self.RegisterMenuHandler(wx.ID_CUT, self.OnCut)
        self.RegisterMenuHandler(wx.ID_COPY, self.OnCopy)
        self.RegisterMenuHandler(wx.ID_PASTE, self.OnPaste)
        self.RegisterMenuHandler(wx.ID_SELECTALL, self.OnSelectAll)
        self.RegisterUpdateUIHandler(wx.ID_CUT, self.OnUpdateCut)
        self.RegisterUpdateUIHandler(wx.ID_COPY, self.OnUpdateCopy)
        self.RegisterUpdateUIHandler(wx.ID_PASTE, self.OnUpdatePaste)
        self.RegisterUpdateUIHandler(wx.ID_SELECTALL, self.OnUpdateSelectAll)

    def OnCut(self, event):
        self.txt.Cut()

    def OnCopy(self, event):
        self.txt.Copy()

    def OnPaste(self, event):
        self.txt.Paste()

    def OnSelectAll(self, event):
        self.txt.SelectAll()

    def OnUpdateCut(self, event):
        event.Enable(self.txt.CanCopy())

    def OnNewWindow(self, event):
        """Create a new window"""
        num = len(wx.GetTopLevelWindows())
        win = MyFrame(None, title="Frame %d" % num)
        win.Show()

    def OnUpdateCopy(self, event):
        event.Enable(self.txt.CanCopy())

    def OnUpdatePaste(self, event):
        event.Enable(self.txt.CanPaste())

    def OnUpdateSelectAll(self, event):
        """Only enable SelectAll if there is text in the control"""
        event.Enable(bool(self.txt.GetValue()))

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
