# Chapter 7: Window Layout and Design
# Recipe 3: GridBagSizer
#
import wx

#---- Recipe Code ----#

class DetailsDialog(wx.Dialog):
    def __init__(self, parent, type, details, title=""):
        """Create the dialog
        @param type: event type string
        @param details: long details string
        """
        super(DetailsDialog, self).__init__(parent, title=title)

        # Attributes
        self.type = wx.TextCtrl(self, value=type,
                                style=wx.TE_READONLY)
        self.details = wx.TextCtrl(self, value=details,
                                   style=wx.TE_READONLY|
                                         wx.TE_MULTILINE)

        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        sizer = wx.GridBagSizer(vgap=8, hgap=8)

        type_lbl = wx.StaticText(self, label="Type:")
        detail_lbl = wx.StaticText(self, label="Details:")

        # Add the event type fields
        sizer.Add(type_lbl, (1, 1))
        sizer.Add(self.type, (1, 2), (1, 15), wx.EXPAND)

        # Add the details field
        sizer.Add(detail_lbl, (2, 1))
        sizer.Add(self.details, (2, 2), (5, 15), wx.EXPAND)

        # Add a spacer to pad out the right side
        sizer.Add((5, 5), (2, 17))
        # And another to the pad out the bottom
        sizer.Add((5, 5), (7, 0))

        self.SetSizer(sizer)

#---- End Recipe Code ----#

# Sample data to use when showing dialog
DATA = (
("Memory Error", "Unable to allocate the following blocks of memory for"
                 " the calling program (0x80f2, 0x80f3, 0x80f4). The"
                 " stack may be corrupted around around the variable"
                 " pMenu."),
("Access Violation", "Access violation at 0x0045E4C5 "
                     "(tried to read from 0x05AC0008), program terminated"),
("COM Error", "COM Error 0x8007005 - Access Denied. Please check that you"
              " have the required privileges to access the requested resource"
              " on the remote system."))

class GridBagApp(wx.App):
    def OnInit(self):
        self.frame = GridBagFrame(None,
                                  title="GridBagSizer")
        self.frame.Show()
        return True

class GridBagFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = GridBagPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class GridBagPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        # Attributes
        choices = [ x[0] for x in DATA ]
        self.list = wx.ListBox(self, choices=choices, style=wx.LB_SINGLE)
        self.button = wx.Button(self, label="Details")

        # Layout
        self._DoLayout()

        # Events
        self.Bind(wx.EVT_BUTTON, self.OnShowDetails, self.button)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, self.button)

    def _DoLayout(self):
        """Layout the controls"""
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.list, 1, wx.EXPAND)
        vsizer.Add(self.button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 8)
        self.SetSizer(vsizer)

    def OnUpdateUI(self, event):
        sel = self.list.GetSelection()
        # Only enable the button if a selection has been
        # made in the list.
        event.Enable(sel != wx.NOT_FOUND)

    def OnShowDetails(self, event):
        """Show the details for the item in the list"""
        item = DATA[self.list.GetSelection()]
        dlg = DetailsDialog(self, item[0], item[1], title="Error Details")
        dlg.ShowModal()
        dlg.Destroy()

if __name__ == '__main__':
    app = GridBagApp(False)
    app.MainLoop()
