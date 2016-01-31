# Chapter 1: Getting Started
# Recipe 11: Virtualized Methods
#
import wx

#-----------------------------------------------------------------------------#

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

    def AddChild(self, child):
        sizer = self.GetSizer()
        sizer.Add(child, 0, wx.ALIGN_LEFT|wx.ALL, 8)
        return super(MyPanel, self).AddChild(child)

class MyVirtualPanel(wx.PyPanel):
    """Class that automatically adds children
    controls to sizer layout.
    """
    def __init__(self, parent):
        super(MyVirtualPanel, self).__init__(parent)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

    def AddChild(self, child):
        sizer = self.GetSizer()
        sizer.Add(child, 0, wx.ALIGN_LEFT|wx.ALL, 8)
        return super(MyVirtualPanel, self).AddChild(child)

#-----------------------------------------------------------------------------#

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent,
                                      *args, **kwargs)

        # Attributes
        self.mypanel = MyPanel(self)
        self.mypanel.SetBackgroundColour(wx.BLACK)
        self.virtpanel = MyVirtualPanel(self)
        self.virtpanel.SetBackgroundColour(wx.WHITE)

        # Setup
        self.__DoLayout()

    def __DoLayout(self):
        """Layout the window"""
        # Layout the controls using a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.mypanel, 1, wx.EXPAND)
        sizer.Add(self.virtpanel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        # Create 3 children for the top panel
        for x in range(3):
            wx.Button(self.mypanel,
                      label="MyPanel %d" % x)
        # Create 3 children for the bottom panel
        for x in range(3):
            wx.Button(self.virtpanel,
                      label="VirtPanel %d" % x)

        self.SetInitialSize(size=(300, 200))

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None,
                             title="Virtualized Methods")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()

