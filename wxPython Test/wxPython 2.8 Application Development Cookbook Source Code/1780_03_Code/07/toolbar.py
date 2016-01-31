# Chapter 3: An Applications Building Blocks, Basic Controls
# Recipe 7: ToolBars
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = ToolBarFrame(None, title="ToolBars")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class ToolBarFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ToolBarFrame, self).__init__(*args, **kwargs)

        # Setup the ToolBar
        toolb = EasyToolBar(self)
        toolb.AddEasyTool(wx.ID_CUT)
        toolb.AddEasyTool(wx.ID_COPY)
        toolb.AddEasyTool(wx.ID_PASTE)
        toolb.Realize()
        self.SetToolBar(toolb)

        # Event Handlers
        self.Bind(wx.EVT_TOOL, self.OnToolBar)

    def OnToolBar(self, event):
        print "ToolBarItem Clicked", event.GetId()

ART_MAP = { wx.ID_CUT : wx.ART_CUT,
            wx.ID_COPY : wx.ART_COPY,
            wx.ID_PASTE : wx.ART_PASTE }

class EasyToolBar(wx.ToolBar):
    def AddEasyTool(self, id, shortHelp="", longHelp=""):
        """Simplifies adding a tool to the toolbar
        @param id: Stock ID

        """
        assert id in ART_MAP, "Unknown Stock ID"
        art_id = ART_MAP.get(id)
        bmp = wx.ArtProvider.GetBitmap(art_id, wx.ART_TOOLBAR)
        self.AddSimpleTool(id, bmp, shortHelp, longHelp)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
