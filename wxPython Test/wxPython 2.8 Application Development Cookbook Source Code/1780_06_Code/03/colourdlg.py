# Chapter 6: Retrieving Information from Users, Common Dialogs
# Recipe 3: ColourDialog
#
import wx

class ColourDialogApp(wx.App):
    def OnInit(self):
        self.frame = ColourDialogFrame(None,
                                       title="ColourDialog")
        self.frame.Show()
        return True

class ColourDialogFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ColourDialogFrame, self).__init__(*args,
                                                **kwargs)

        # Attributes
        self.panel = ColourDialogPanel(self)

class ColourDialogPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(ColourDialogPanel, self).__init__(*args, **kwargs)

        # Attributes
        self.btn = wx.Button(self, label="Change Colour")

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer.Add(self.btn, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()
        hsizer.Add(vsizer, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()
        self.SetSizer(hsizer)

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnShowDialog, self.btn)

    def OnShowDialog(self, event):
        colour_data = wx.ColourData()
        # Initialize to the current colour of the panel
        colour = self.GetBackgroundColour()
        colour_data.SetColour(colour)
        # Use the extended dialog when available
        colour_data.SetChooseFull(True)
        # Construct the dialog
        dlg = wx.ColourDialog(self, colour_data)
        if dlg.ShowModal() == wx.ID_OK:
            # Change the background colour
            colour = dlg.GetColourData().GetColour()
            self.SetBackgroundColour(colour)
            self.Refresh()
        dlg.Destroy()

if __name__ == '__main__':
    app = ColourDialogApp(False)
    app.MainLoop()
