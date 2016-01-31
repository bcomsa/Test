# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 6: Supporting Internationalization
#
import wx
import os

# Make a shorter alias
_ = wx.GetTranslation

class I18NApp(wx.App):
    def OnInit(self):
        self.SetAppName("I18NTestApp")
        # Get Language from last run if set
        config = wx.Config()
        language = config.Read('lang', 'LANGUAGE_DEFAULT')

        # Setup the Locale
        self.locale = wx.Locale(getattr(wx, language))
        path = os.path.abspath("./locale") + os.path.sep
        self.locale.AddCatalogLookupPathPrefix(path)
        self.locale.AddCatalog(self.GetAppName())

        # Local is not setup so we can create things that
        # may need it to retrieve translations.
        self.frame = TestFrame(None,
                               title=_("Sample App"))
        self.frame.Show()
        return True

class TestFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(TestFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = TestPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class TestPanel(wx.Panel):
    def __init__(self, parent):
        super(TestPanel, self).__init__(parent)

        # Attributes
        self.closebtn = wx.Button(self, wx.ID_CLOSE)
        self.langch = wx.Choice(self,
                                choices=[_("English"),
                                         _("Japanese")])

        # Layout
        self.__DoLayout()

        # Event Handler
        self.Bind(wx.EVT_CHOICE, self.OnChoice)
        self.Bind(wx.EVT_BUTTON,
                  lambda event: self.GetParent().Close())

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, label=_("Hello"))
        hsizer.AddStretchSpacer()
        hsizer.Add(label, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()

        langsz = wx.BoxSizer(wx.HORIZONTAL)
        langlbl = wx.StaticText(self, label=_("Language"))
        langsz.AddStretchSpacer()
        langsz.Add(langlbl, 0, wx.ALIGN_CENTER_VERTICAL)
        langsz.Add(self.langch, 0, wx.ALL, 5)
        langsz.AddStretchSpacer()
        
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.Add(langsz, 0, wx.EXPAND|wx.ALL, 5)
        vsizer.Add(self.closebtn, 0, wx.ALIGN_CENTER)
        vsizer.AddStretchSpacer()

        self.SetSizer(vsizer)

    def OnChoice(self, event):
        sel = self.langch.GetSelection()
        config = wx.Config()
        if sel == 0:
            val = 'LANGUAGE_ENGLISH'
        else:
            val = 'LANGUAGE_JAPANESE'
        config.Write('lang', val)

if __name__ == '__main__':
    app = I18NApp(False)
    app.MainLoop()
