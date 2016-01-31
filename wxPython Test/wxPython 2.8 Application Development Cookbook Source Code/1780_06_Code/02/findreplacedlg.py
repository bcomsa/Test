# Chapter 6: Retrieving Information from Users, Common Dialogs
# Recipe 2: FindReplaceDialog
#
import wx

# FileDialog recipe sample module
import filedialog

class FindReplaceEditorApp(wx.App):
    def OnInit(self):
        self.frame = FindReplaceEditorFrame(None,
                                            title="File Editor")
        self.frame.Show()
        return True

class FindReplaceEditorFrame(filedialog.FileEditorFrame):
    def __init__(self, *args, **kwargs):
        super(FindReplaceEditorFrame, self).__init__(*args,
                                                     **kwargs)

        # Attributes
        self.finddlg = None
        self.finddata = wx.FindReplaceData()

        # Setup
        menub = self.GetMenuBar()
        editmenu = wx.Menu()
        editmenu.Append(wx.ID_FIND, "Find\tCtrl+F")
        editmenu.Append(wx.ID_REPLACE, "Replace\tCtrl+R")
        menub.Append(editmenu, "Edit")

        # Event Handlers
        self.Bind(wx.EVT_MENU,
                  self.OnFindMenu,
                  id=wx.ID_FIND)
        self.Bind(wx.EVT_MENU,
                  self.OnFindMenu,
                  id=wx.ID_REPLACE)
        self.Bind(wx.EVT_FIND, self.OnFind)
        self.Bind(wx.EVT_FIND_NEXT, self.OnFind)
        self.Bind(wx.EVT_FIND_REPLACE, self.OnReplace)
        self.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnReplaceAll)
        self.Bind(wx.EVT_FIND_CLOSE, self.OnFindClose)

    def _InitFindDialog(self, mode):
        if self.finddlg:
            self.finddlg.Destroy()

        style = (wx.FR_NOUPDOWN
                 |wx.FR_NOMATCHCASE
                 |wx.FR_NOWHOLEWORD)
        if mode == wx.ID_REPLACE:
            style |= wx.FR_REPLACEDIALOG
            title = "Find/Replace"
        else:
            title = "Find"
        dlg = wx.FindReplaceDialog(self,
                                   self.finddata,
                                   title,
                                   style)
        self.finddlg = dlg

    # ---- Event Handlers ----#

    def OnFindMenu(self, event):
        evt_id = event.GetId()
        if evt_id in (wx.ID_FIND, wx.ID_REPLACE):
            self._InitFindDialog(evt_id)
            self.finddlg.Show()
        else:
            event.Skip()

    def OnFind(self, event):
        """Find text"""
        findstr = self.finddata.GetFindString()
        if not self.FindString(findstr):
            wx.Bell() # beep at the user for no match

    def OnReplace(self, event):
        """Replace text"""
        rstring = self.finddata.GetReplaceString()
        fstring = self.finddata.GetFindString()
        cpos = self.GetInsertionPoint()
        start, end = cpos, cpos
        if fstring:
            if self.FindString(fstring):
                start, end = self.txtctrl.GetSelection()
        self.txtctrl.Replace(start, end, rstring)

    def OnReplaceAll(self, event):
        """Do a replace all"""
        rstring = self.finddata.GetReplaceString()
        fstring = self.finddata.GetFindString()
        text = self.txtctrl.GetValue()
        newtext = text.replace(fstring, rstring)
        self.txtctrl.SetValue(newtext)

    def OnFindClose(self, event):
        if self.finddlg:
            self.finddlg.Destroy()
            self.finddlg = None

    #---- End Event Handlers ----#

    #---- Implementation ----#

    def FindString(self, findstr):
        """Find findstr in TextCtrl and set selection"""
        text = self.txtctrl.GetValue()
        csel = self.txtctrl.GetSelection()
        if csel[0] != csel[1]:
            cpos = max(csel)
        else:
            cpos = self.txtctrl.GetInsertionPoint()

        if cpos == self.txtctrl.GetLastPosition():
            cpos = 0

        # Do a simple case insensitive search 
        # to find the next match
        text = text.upper()
        findstr = findstr.upper()
        found = text.find(findstr, cpos)
        if found != -1:
            end = found + len(findstr)
            self.txtctrl.SetSelection(end, found)
            self.txtctrl.SetFocus()
            return True
        return False

    #---- End Implementation ----#

if __name__ == '__main__':
    app = FindReplaceEditorApp(False)
    app.MainLoop()

