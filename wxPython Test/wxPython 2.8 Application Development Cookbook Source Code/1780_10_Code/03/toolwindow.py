# Chapter 10: Creating Components and Extending Functionality
# Recipe 3: Making a ToolWindow
#
import wx
import wx.lib.pubsub as pubsub

# message data will be tool id
MSG_TOOL_CLICKED = ('toolwin', 'clicked')

class ToolWindow(wx.MiniFrame):
    def __init__(self, parent, rows=1, columns=0, title=''):
        style = wx.CAPTION|wx.SYSTEM_MENU|\
                wx.SIMPLE_BORDER|wx.CLOSE_BOX
        super(ToolWindow, self).__init__(parent,
                                         title=title,
                                         style=style)

        # Attributes
        self.panel = ToolPanel(self, rows, columns)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def AddTool(self, id, bmp, helplbl=''):
        """Add a tool to the window"""
        self.panel.AddTool(id, bmp, helplbl)
        self.Fit()

class ToolPanel(wx.Panel):
    """Panel to hold the tools"""
    def __init__(self, parent, rows, columns):
        super(ToolPanel, self).__init__(parent)

        # Attributes
        self.sizer = wx.FlexGridSizer(rows, columns, 5, 5)

        # Setup
        self.SetSizer(self.sizer)

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def AddTool(self, id, bmp, helplbl=''):
        tool = wx.BitmapButton(self, id, bmp)
        tool.SetToolTipString(helplbl)
        self.sizer.Add(tool)
        self.Layout()

    def OnButton(self, event):
        """Notify clients when tool is clicked"""
        pubsub.Publisher.sendMessage(MSG_TOOL_CLICKED,
                                     event.GetId())

class EditorToolWindow(ToolWindow):
    def __init__(self, parent, rows, columns, title):
        ToolWindow.__init__(self, parent, rows, 
                            columns, title)

        # Setup
        for artid, tid in ((wx.ART_CUT, wx.ID_CUT),
                           (wx.ART_COPY, wx.ID_COPY),
                           (wx.ART_PASTE, wx.ID_PASTE),
                           (wx.ART_UNDO, wx.ID_UNDO),
                           (wx.ART_REDO, wx.ID_REDO)):
            bmp = wx.ArtProvider.GetBitmap(artid, wx.ART_MENU)
            self.AddTool(tid, bmp)

class ToolWindowApp(wx.App):
    def OnInit(self):
        self.frame = MainWindow(None,
                                title="ToolWindow Recipe")
        self.frame.CenterOnScreen()
        self.frame.Show()
        self.toolw = EditorToolWindow(None, rows=2, columns=3,
                                      title="Editor Commands")
        # Position ToolWindow to right of main window
        mpos = self.frame.GetPosition()
        msize = self.frame.GetSize()
        self.toolw.SetPosition((mpos[0] + msize[0], mpos[1]))
        self.toolw.Show()
        return True

class MainWindow(wx.Frame):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

        # Message Handler
        pubsub.Publisher.subscribe(self.OnTool, MSG_TOOL_CLICKED)

    def __del__(self):
        pubsub.Publisher.unsubscribe(self.OnTool)

    def OnTool(self, msg):
        """Observer function for tool window events"""
        toolid = msg.data
        actionmap = { wx.ID_CUT   : self.panel.Cut,
                      wx.ID_COPY  : self.panel.Copy,
                      wx.ID_PASTE : self.panel.Paste,
                      wx.ID_UNDO  : self.panel.Undo,
                      wx.ID_REDO  : self.panel.Redo }
        action = actionmap.get(toolid, lambda:x)
        action()

if __name__ == '__main__':
    app = ToolWindowApp(False)
    app.MainLoop()
