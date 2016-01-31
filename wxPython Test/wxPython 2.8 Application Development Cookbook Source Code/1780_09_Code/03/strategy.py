# Chapter 9: Design Approaches and Techniques
# Recipe 3: Strategy Pattern
#
import wx

#---- Recipe Code ----#
class BaseDialogStrategy:
    """Defines the strategy interface"""
    def GetWindowObject(self, parent):
        """Must return a Window object"""
        raise NotImplementedError, "Required method"

    def DoOnOk(self):
        """@return: bool (True to exit, False to not)"""
        return True

    def DoOnCancel(self):
        """@return: bool (True to exit, False to not)"""
        return True

class StrategyDialog(wx.Dialog):
    """Simple dialog with builtin OK/Cancel button and
    strategy based content area.   
    """
    def __init__(self, parent, strategy, *args, **kwargs):
        super(StrategyDialog, self).__init__(parent,
                                             *args,
                                             **kwargs)

        # Attributes
        self.strategy = strategy
        self.pane = self.strategy.GetWindowObject(self)

        # Layout
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pane, 1, wx.EXPAND)
        btnsz = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        sizer.Add(btnsz, 0, wx.EXPAND|wx.ALL, 8)
        self.SetSizer(sizer)

    def GetStrategy(self):
        return self.strategy

    def OnButton(self, event):
        evt_id = event.GetId()
        bCanExit = False
        if evt_id == wx.ID_OK:
            bCanExit = self.strategy.DoOnOk()
        elif evt_id == wx.ID_OK:
            bCanExit = self.strategy.DoOnCancel()
        else:
            evt.Skip()

        if bCanExit:
            self.EndModal(evt_id)

class FileTreeStrategy(BaseDialogStrategy):
    """File chooser strategy"""
    def GetWindowObject(self, parent):
        assert not hasattr(self, 'dirctrl')
        self.dirctrl = wx.GenericDirCtrl(parent)
        return self.dirctrl

    def DoOnOk(self):
        path = self.dirctrl.GetPath()
        if path:
            wx.MessageBox("You selected: %s" % path)
            return True
        else:
            wx.MessageBox("No file selected!")
            return False

#---- End Recipe Code ----#

class StrategyRecipeApp(wx.App):
    def OnInit(self):
        self.frame = StrategyFrame(None,
                                   title="Strategy Pattern")
        self.frame.Show()
        return True

class StrategyFrame(wx.Frame):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = StrategyRecipePanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 300))

class StrategyRecipePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Attributes
        self.button = wx.Button(self, label="FileStrategy")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.AddWindow(self.button)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

    def OnButton(self, event):
        evt_obj = event.GetEventObject()
        strategy = None
        if evt_obj is self.button:
            # File strategy
            strategy = FileTreeStrategy()
        # elif # some other strategy...
        else:
            event.Skip()

        if strategy:
            dlg = StrategyDialog(self, strategy, title="Strategy")
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
    app = StrategyRecipeApp(False)
    app.MainLoop()
