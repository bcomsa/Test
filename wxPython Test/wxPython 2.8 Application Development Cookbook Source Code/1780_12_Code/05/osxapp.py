# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 5: Optimizing for OSX
#
import wx
import sys

class OSXApp(wx.App):
    def OnInit(self):
        # Enable native spell checking and right
        # click menu for Mac TextCtrl's
        if wx.Platform == '__WXMAC__':
            spellcheck = "mac.textcontrol-use-spell-checker"
            wx.SystemOptions.SetOptionInt(spellcheck, 1)
        self.frame = OSXFrame(None,
                              title="Optimize for OSX")
        self.frame.Show()
        return True

    def MacReopenApp(self):
        self.GetTopWindow().Raise()

class OSXFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(OSXFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.textctrl = wx.TextCtrl(self,
                                    style=wx.TE_MULTILINE)

        # Setup Menus
        mb = wx.MenuBar()
        fmenu = wx.Menu()
        fmenu.Append(wx.ID_OPEN)
        fmenu.Append(wx.ID_EXIT)
        mb.Append(fmenu, "&File")
        emenu = wx.Menu()
        emenu.Append(wx.ID_COPY)
        emenu.Append(wx.ID_PREFERENCES)
        mb.Append(emenu, "&Edit")
        hmenu = wx.Menu()
        hmenu.Append(wx.NewId(), "&Online Help...")
        hmenu.Append(wx.ID_ABOUT, "&About...")
        mb.Append(hmenu, "&Help")
        
        if wx.Platform == '__WXMAC__':
            # Make sure we don't get duplicate
            # Help menu since we used non standard name
            app = wx.GetApp()
            app.SetMacHelpMenuTitleName("&Help")

        self.SetMenuBar(mb)
        self.SetInitialSize()

if __name__ == '__main__':
    app = OSXApp(False)
    app.MainLoop()

