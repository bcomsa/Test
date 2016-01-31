# Chapter 10: Creating Components and Extending Functionality
# Recipe 7: Creating a Custom Control
#
import wx

# Recipe's code
import custcheckbox

class CustomCheckBoxApp(wx.App):
    def OnInit(self):
        self.frame = CustomCheckBoxFrame(None,
                                         title="Custom Controls")
        self.frame.Show()
        return True

class CustomCheckBoxFrame(wx.Frame):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        super(CustomCheckBoxFrame, self).__init__(parent, *args, **kwargs)

        # Attributes
        self.panel = CustomCheckBoxPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 100))

class CustomCheckBoxPanel(wx.Panel):
    def __init__(self, parent):
        super(CustomCheckBoxPanel, self).__init__(parent)

        # Attributes
        self.checkbox = custcheckbox.CustomCheckBox(self, label="Hello World")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(self.checkbox, 0, wx.ALIGN_CENTER|wx.ALL, 10)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnCheckBox(self, event):
        eobj = event.GetEventObject()
        print "CheckBox Clicked", eobj.GetValue()

if __name__ == '__main__':
    app = CustomCheckBoxApp(False)
    app.MainLoop()

