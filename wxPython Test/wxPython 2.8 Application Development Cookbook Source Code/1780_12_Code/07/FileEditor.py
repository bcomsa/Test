# Chapter 6: Retrieving Information from Users, Common Dialogs
# Recipe 1: FileDialog
#
import wx

class FileEditorApp(wx.App):
    def OnInit(self):
        self.frame = FileEditorFrame(None,
                                     title="File Editor",
                                     size=(350,300))
        self.frame.Show()
        return True

class FileEditorFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.file = None
        style = style=wx.TE_MULTILINE|wx.TE_RICH2
        self.txtctrl = wx.TextCtrl(self, style=style)

        # Setup
        self._SetupMenus()

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

    def _SetupMenus(self):
        """Make the frames menus"""
        menub = wx.MenuBar()
        fmenu = wx.Menu()
        fmenu.Append(wx.ID_OPEN, "Open\tCtrl+O")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_SAVE, "Save\tCtrl+S")
        fmenu.Append(wx.ID_SAVEAS, "Save As\tCtrl+Shift+S")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_EXIT, "Exit\tCtrl+Q")
        menub.Append(fmenu, "File")
        self.SetMenuBar(menub)

    #---- Event Handlers ----#

    def OnOpen(self, event):
        """Handle Open"""
        if event.GetId() == wx.ID_OPEN:
            self.DoOpen()
        else:
            event.Skip()

    def OnSave(self, event):
        """Handle Save/SaveAs"""
        evt_id = event.GetId()
        if evt_id in (wx.ID_SAVE,
                      wx.ID_SAVEAS):
            if self.file:
                self.Save(self.file)
            else:
                self.DoSaveAs()
        else:
            event.Skip()

    def OnExit(self, event):
        """Handle window close event"""
        # Give warning about unsaved changes
        if self.txtctrl.IsModified():
            message = ("There are unsaved changes.\n\n"
                       "Would you like to save them?")
            style = wx.YES_NO|wx.ICON_WARNING|wx.CENTRE
            result = wx.MessageBox(message,
                                   "Save Changes?",
                                   style=style)
            if result == wx.YES:
                if self.file is None:
                    self.DoSaveAs()
                else:
                    self.Save(self.file)
        event.Skip()

    #---- End Event Handlers ----#

    #---- Implementation ----#

    def DoOpen(self):
        """Show file open dialog and open file"""
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self,
                            message="Open a File",
                            wildcard=wildcard,
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            with open(path, "rb") as handle:
                text = handle.read()
                self.txtctrl.SetValue(text)
                self.file = path
        dlg.Destroy()

    def DoSaveAs(self):
        """Show SaveAs dialog"""
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self,
                            message="Save As",
                            wildcard=wildcard,
                            style=wx.FD_SAVE
                                  |wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.Save(path)
            self.file = path
        dlg.Destroy()

    def Save(self, path):
        """Save the file"""
        with open(path, "wb") as handle:
            text = self.txtctrl.GetValue()
            handle.write(text)
            self.txtctrl.SetModified(False)
        
    #---- End Implementation ----#

#---- Main Execution ----#
if __name__ == "__main__":
    app = FileEditorApp(False)
    app.MainLoop()
