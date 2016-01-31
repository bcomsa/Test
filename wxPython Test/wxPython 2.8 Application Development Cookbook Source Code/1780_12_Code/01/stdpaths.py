# Chapter 12: Application Infrastructure,
#             Building and Managing Applications for Distribution
# Recipe 1: Working with StandardPaths
#
import wx
import os

class ConfigHelper(object):
    def __init__(self, userdirs=None):
        """@keyword userdirs: list of user config
                              subdirectories names
        """
        super(ConfigHelper, self).__init__()

        # Attributes
        self.userdirs = userdirs

        # Setup
        self.InitializeConfig()

    def InitializeConfig(self):
        """Setup config directories"""
        # Create main user config directory if it does
        # not exist.
        datap = wx.StandardPaths_Get().GetUserDataDir()
        if not os.path.exists(datap):
            os.mkdir(datap)
        # Make sure that any other application specific
        # config subdirectories have been created.
        if self.userdirs:
            for dname in userdirs:
                self.CreateUserCfgDir(dname)

    def CreateUserCfgDir(self, dirname):
        """Create a user config subdirectory"""
        path = wx.StandardPaths_Get().GetUserDataDir()
        path = os.path.join(path, dirname)
        if not os.path.exists(path):
            os.mkdir(path)

    def GetUserConfigPath(self, relpath):
        """Get the path to a resource file
        in the users configuration directory.
        @param relpath: relative path (i.e config.cfg)
        @return: string
        """
        path = wx.StandardPaths_Get().GetUserDataDir()
        path = os.path.join(path, relpath)
        return path

    def HasConfigFile(self, relpath):
        """Does a given config file exist"""
        path = self.GetUserConfigPath(relpath)
        return os.path.exists(path)

#---- Sample Application ----#

class ConfigHelperApp(wx.App):
    def OnInit(self):
        self.SetAppName("ConfigHelperTestApp")
        self.config = ConfigHelper()
        self.frame = ConfigHelperFrame(None, title="Config Helper")
        self.frame.Show()
        return True

    def GetConfig(self):
        return self.config

class ConfigHelperFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(ConfigHelperFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ConfigHelperPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class ConfigHelperPanel(wx.Panel):
    def __init__(self, parent):
        super(ConfigHelperPanel, self).__init__(parent)

        # Attributes
        val = self.FetchConfigVal()
        self.configval = wx.StaticText(self, label="Stored Size: %s" % val)
        self.store = wx.Button(self, label="Store")
        self.store.SetToolTipString("Store current window size")
        self.fetch = wx.Button(self, label="Fetch")
        self.fetch.SetToolTipString("Fetch stored window size")

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        vsizer.Add(self.configval, 0, wx.ALL, 20)
        btnsz = wx.BoxSizer(wx.HORIZONTAL)
        btnsz.Add(self.store, 0, wx.ALL, 5)
        btnsz.Add(self.fetch, 0, wx.ALL, 5)
        vsizer.Add(btnsz, 0, wx.ALIGN_CENTER)
        vsizer.AddStretchSpacer()

        hsizer.AddStretchSpacer()
        hsizer.Add(vsizer, 0, wx.EXPAND)
        hsizer.AddStretchSpacer()
        self.SetSizer(hsizer)

    def OnButton(self, event):
        e_obj = event.GetEventObject()
        if e_obj == self.store:
            # Store window size in config file
            config = wx.GetApp().GetConfig()
            resource = config.GetUserConfigPath("app.config")
            handle = open(resource, 'wb')
            winsize = self.GetTopLevelParent().GetSize()
            handle.write(str(winsize))
            handle.close()
        elif e_obj == self.fetch:
            # Get window size from config file
            val = self.FetchConfigVal()
            if val == "??":
                wx.MessageBox("No config value stored yet!")
            self.configval.SetLabel("Stored Size: %s" % val)
        else:
            event.Skip()

    def FetchConfigVal(self):
        config = wx.GetApp().GetConfig()
        resource = config.GetUserConfigPath("app.config")
        if not os.path.exists(resource):
            val = "??"
        else:
            handle = open(resource, 'rb')
            val = handle.read()
            handle.close()
        return val

if __name__ == '__main__':
    app = ConfigHelperApp(False)
    app.MainLoop()
