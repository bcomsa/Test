# Chapter 9: Design Approaches and Techniques
# Recipe 2: Implementing an Observer Pattern
#
import wx
from wx.lib.pubsub import Publisher

# PubSub message classification
MSG_CONFIG_ROOT = ('config',)

class Configuration(object):
    """Configuration object that provides
    notifications.
    """
    def __init__(self):
        super(Configuration, self).__init__()

        # Attributes
        self._data = dict()

    def SetValue(self, key, value):
        self._data[key] = value
        # Notify all observers of config change
        Publisher.sendMessage(MSG_CONFIG_ROOT + (key,),
                              value)

    def GetValue(self, key):
        """Get a value from the configuration"""
        return self._data.get(key, None)

class ObserverApp(wx.App):
    def OnInit(self):
        self.config = Configuration()
        self.frame = ObserverFrame(None,
                                   title="Observer Pattern")
        self.frame.Show()
        self.configdlg = ConfigDialog(self.frame,
                                      title="Config Dialog")
        self.configdlg.Show()
        return True

    def GetConfig(self):
        return self.config

class ConfigDialog(wx.Dialog):
    """Simple setting dialog"""
    def __init__(self, *args, **kwargs):
        super(ConfigDialog, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = ConfigPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class ConfigPanel(wx.Panel):
    def __init__(self, parent):
        super(ConfigPanel, self).__init__(parent)

        # Attributes
        self.picker = wx.FontPickerCtrl(self)

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_FONTPICKER_CHANGED,
                  self.OnFontPicker)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.AddWindow(self.picker)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnFontPicker(self, event):
        """Event handler for the font picker control"""
        font = self.picker.GetSelectedFont()
        # Update the configuration
        config = wx.GetApp().GetConfig()
        config.SetValue('font', font)

class ObserverFrame(wx.Frame):
    """Window that observes configuration messages"""
    def __init__(self, *args, **kwargs):
        super(ObserverFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.txt = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.txt.SetValue("Change the font in the config "
                          "dialog and see it update here.")
    
        # Observer of configuration changes
        Publisher.subscribe(self.OnConfigMsg, MSG_CONFIG_ROOT)

    def __del__(self):
        # Unsubscribe when deleted
        Publisher.unsubscribe(self.OnConfigMsg)

    def OnConfigMsg(self, msg):
        """Observer method for config change messages"""
        if msg.topic[-1] == 'font':
            # font has changed so update controls
            self.SetFont(msg.data)
            self.txt.SetFont(msg.data)

if __name__ == '__main__':
    app = ObserverApp(False)
    app.MainLoop()

