# Chapter 9: Design Approaches and Techniques
# Recipe 6: Using Decorators
#
import wx

#---- Recipe Code ----#

class expose(object):
    """Expose a panels method to a to a specified class
    The panel that is having its method exposed by this
    decorator must be a child of the class its exposing
    itself too.
    """
    def __init__(self, cls):
        """@param cls: class to expose the method to"""
        super(expose, self).__init__()
        self.cls = cls

    def __call__(self, funct):
        """Dynamically bind and expose the function
        to the toplevel window class.
        """
        fname = funct.func_name
        def delegate(*args, **kwargs):
            """Delegate method for panel"""
            self = args[0] # The TLW
            # Find the panel this method belongs to
            panel = None
            for child in self.GetChildren():
                if isinstance(child, wx.Panel) and \
                   hasattr(child, fname):
                    panel = child
                    break
            assert panel is not None, "No matching child!"
            # Call the panels method
            return getattr(panel, fname)(*args[1:], **kwargs)

        # Bind the new delegate method to the tlw class
        delegate.__name__ = funct.__name__
        delegate.__doc__ = funct.__doc__
        setattr(self.cls, fname, delegate)

        # Return original function to the current class
        return funct

class CommentDialog(wx.Dialog):
    """Simple dialog to retrieve a comment
    string from a user.
    """
    def __init__(self, parent, title="Comment Dialog"):
        style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER
        super(CommentDialog, self).__init__(parent,
                                            title=title,
                                            style=style)

        # Attribute
        self._panel = CommentPanel(self)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self._panel, 1, wx.EXPAND)
        btnsz = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        vsizer.Add(btnsz, 0, wx.EXPAND|wx.ALL, 8)
        self.SetSizer(vsizer)

class CommentPanel(wx.Panel):
    def __init__(self, parent):
        super(CommentPanel, self).__init__(parent)

        # Attributes
        self._title = wx.TextCtrl(self)
        self._comment = wx.TextCtrl(self,
                                    style=wx.TE_MULTILINE)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)

        # Title Field
        tsizer = wx.BoxSizer(wx.HORIZONTAL)
        tsizer.Add(wx.StaticText(self, label="Title:"),
                   0, wx.RIGHT, 5)
        tsizer.Add(self._title, 1, wx.EXPAND)

        vsizer.Add(tsizer, 0, wx.EXPAND|wx.ALL, 5)
        vsizer.Add(self._comment, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(vsizer)

    @expose(CommentDialog)
    def GetCommentTitle(self):
        return self._title.GetValue()

    @expose(CommentDialog)
    def SetCommentTitle(self, title):
        self._title.SetValue(title)

    @expose(CommentDialog)
    def GetComment(self):
        return self._comment.GetValue()

    @expose(CommentDialog)
    def SetComment(self, comment):
        self._comment.SetValue(comment)

#---- End Recipe Code ----#

class DynamicMethodApp(wx.App):
    def OnInit(self):
        self.frame = DynamicMethodFrame(None,
                                        title="Dynamic Method")
        self.frame.Show()
        return True

class DynamicMethodFrame(wx.Frame):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = DynamicMethodPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class DynamicMethodPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Attributes
        self._button = wx.Button(self, label="Get Comment")

        # Setup
        self.__DoLayout()

        # Event Handler
        self.Bind(wx.EVT_BUTTON, self.OnGetComment, self._button)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.AddStretchSpacer()
        hsizer.Add(self._button)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnGetComment(self, event):
        dlg = CommentDialog(self)
        dlg.SetCommentTitle("Comment Title")
        dlg.SetComment("Enter Comment Here")
        if dlg.ShowModal() == wx.ID_OK:
            print "OK Clicked"
            print "Title: ", dlg.GetCommentTitle()
            print "Comment: ", dlg.GetComment()
        else:
            print "Cancel Clicked"

if __name__ == '__main__':
    app = DynamicMethodApp(False)
    app.MainLoop()

