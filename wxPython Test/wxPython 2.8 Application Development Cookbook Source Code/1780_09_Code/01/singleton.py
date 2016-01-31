# Chapter 9: Design Approaches and Techniques
# Recipe 1: Creating Singletons
#
import wx

#---- Recipe Code ----#

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None
 
    def __call__(cls, *args, **kw):
        if not cls.instance:
            # Not created or has been Destroyed
            obj = super(Singleton, cls).__call__(*args, **kw)
            cls.instance = obj
            cls.instance.SetupWindow()
 
        return cls.instance

class SingletonDialog(wx.Dialog):
    __metaclass__ = Singleton

    def SetupWindow(self):
        """Hook method for initializing window"""
        self.field = wx.TextCtrl(self)
        self.check = wx.CheckBox(self, label="Enable Foo")

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="FooBar")
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.AddMany([(label, 0, wx.ALIGN_CENTER_VERTICAL),
                        ((5, 5), 0),
                        (self.field, 0, wx.EXPAND)])
        btnsz = self.CreateButtonSizer(wx.OK)
        vsizer.AddMany([(hsizer, 0, wx.ALL|wx.EXPAND, 10),
                        (self.check, 0, wx.ALL, 10),
                        (btnsz, 0, wx.EXPAND|wx.ALL, 10)])
        self.SetSizer(vsizer)
        self.SetInitialSize()

#---- End Recipe Code ----#

class SingeltonRecipeApp(wx.App):
    def OnInit(self):
        self.frame = SingletonRecipeFrame(None,
                                          title="Singelton Pattern")
        self.frame.Show()
        return True

class SingletonRecipeFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(SingletonRecipeFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = SingletonRecipePanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class SingletonRecipePanel(wx.Panel):
    def __init__(self, parent):
        super(SingletonRecipePanel, self).__init__(parent)

        # Attributes
        self.button = wx.Button(self, label="Show Dialog")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.AddWindow(self.button)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnButton(self, event):
        dlg = SingletonDialog(self, title="Singleton Dialog")
        dlg.Show()
        dlg.Raise()

if __name__ == '__main__':
    app = SingeltonRecipeApp(False)
    app.MainLoop()
