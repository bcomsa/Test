# Chapter 7: Window Layout and Design
# Recipe 6: Making a Custom Resource Handlers
#
import wx
import wx.xrc as xrc

class XrcTestApp(wx.App):
    def OnInit(self):
        self.frame = XrcTestFrame(None,
                                  size=(300,300),
                                  title="Custom Resource Handlers")
        self.frame.Show()
        return True

# Xml to load our object
RESOURCE = r"""<?xml version="1.0"?>
<resource>
<object class="TextEditPanel" name="TextEdit">
</object>
</resource>
"""

class XrcTestFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(XrcTestFrame, self).__init__(*args, **kwargs)

        # Attributes
        resource = xrc.EmptyXmlResource()
        handler = TextEditPanelXmlHandler()
        resource.InsertHandler(handler)
        resource.LoadFromString(RESOURCE)
        self.panel = resource.LoadObject(self,
                                         "TextEdit",
                                         "TextEditPanel")

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

class TextEditPanel(wx.Panel):
    """Custom Panel containing a TextCtrl and Buttons
    for Copy and Paste actions.
    """
    def __init__(self, *args, **kwargs):
        super(TextEditPanel, self).__init__(*args, **kwargs)

        # Attributes
        self.txt = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.copy = wx.Button(self, wx.ID_COPY)
        self.paste = wx.Button(self, wx.ID_PASTE)

        # Layout
        self._DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnCopy, self.copy)
        self.Bind(wx.EVT_BUTTON, self.OnPaste, self.paste)

    def _DoLayout(self):
        """Layout the controls"""
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(self.txt, 1, wx.EXPAND)
        hsizer.AddStretchSpacer()
        hsizer.Add(self.copy, 0, wx.RIGHT, 5)
        hsizer.Add(self.paste)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND|wx.ALL, 10)

        # Finally assign the main outer sizer to the panel
        self.SetSizer(vsizer)

    def OnCopy(self, event):
        self.txt.Copy()

    def OnPaste(self, event):
        self.txt.Paste()

class TextEditPanelXmlHandler(xrc.XmlResourceHandler):
    """Resource handler for our TextEditPanel"""
    def CanHandle(self, node):
        """Required override. Returns a bool to say
        whether or not this handler can handle the given class
        """
        return self.IsOfClass(node, "TextEditPanel")

    def DoCreateResource(self):
        """Required override to create the object"""
        panel = TextEditPanel(self.GetParentAsWindow(),
                              self.GetID(),
                              self.GetPosition(),
                              self.GetSize(),
                              self.GetStyle("style",
                                            wx.TAB_TRAVERSAL),
                              self.GetName())
        self.SetupWindow(panel)
        self.CreateChildren(panel)
        return panel

if __name__ == '__main__':
    app = XrcTestApp(False)
    app.MainLoop()
