# Chapter 10: Creating Components and Extending Functionality
# Recipe 1: Customizing the ArtProvider
#
import os
import wx

#---- Recipe Code ----#

class TangoArtProvider(wx.ArtProvider):
    def __init__(self):
        super(TangoArtProvider, self).__init__()

        # Attributes
        self.bmps = [bmp.replace('.png', '')
                     for bmp in os.listdir('tango')
                     if bmp.endswith('.png')]

    def CreateBitmap(self, id,
                     client=wx.ART_OTHER,
                     size=wx.DefaultSize):

        # Return NullBitmap on GTK to allow
        # the default artprovider to get the
        # system theme bitmap.
        if wx.Platform == '__WXGTK__':
            return wx.NullBitmap

        # Non GTK Platform get custom resource
        # when one is available.
        bmp = wx.NullBitmap
        if client == wx.ART_MENU or size == (16,16):
            if id in self.bmps:
                path = os.path.join('tango', id+'.png')
                bmp = wx.Bitmap(path)
        else:
            # TODO add support for other bitmap sizes
            pass

        return bmp

#---- End Recipe Code ----#

class ArtProviderApp(wx.App):
    def OnInit(self):
        # Push our custom ArtProvider on to
        # the provider stack.
        wx.ArtProvider.PushProvider(TangoArtProvider())
        self.frame = ArtProviderFrame(None,
                                      title="Tango ArtProvider")
        self.frame.Show()
        return True

class ArtProviderFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(ArtProviderFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ArtProviderPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class ArtProviderPanel(wx.Panel):
    def __init__(self, parent):
        super(ArtProviderPanel, self).__init__(parent)

        # Attributes
        # Lookup all the art provider ids
        art = [ getattr(wx, x) for x in dir(wx)
                if x.startswith('ART_') and 
                not getattr(wx, x).endswith('_C')]
        art.sort()
        self.artch = wx.Choice(self, choices=art)
        self.bmp = wx.StaticBitmap(self)

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_CHOICE, self.OnChoice)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.Add(self.bmp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        hsizer.Add(self.artch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnChoice(self, event):
        sel = self.artch.GetStringSelection()
        bmp = wx.ArtProvider.GetBitmap(sel, wx.ART_MENU)
        self.bmp.SetBitmap(bmp)
        self.bmp.Refresh()
        self.Layout()

if __name__ == '__main__':
    app = ArtProviderApp(False)
    app.MainLoop()
