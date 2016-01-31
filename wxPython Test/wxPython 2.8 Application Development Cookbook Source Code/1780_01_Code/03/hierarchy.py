# Chapter 1: Getting Started
# Recipe 3: Window Hierarchy
#
import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Hierarchy")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", 
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,
                                      pos, size, style, name)

        # Attributes
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLACK)
        self.button = wx.Button(self.panel,
                                label="Push Me",
                                pos=(50, 50))

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
