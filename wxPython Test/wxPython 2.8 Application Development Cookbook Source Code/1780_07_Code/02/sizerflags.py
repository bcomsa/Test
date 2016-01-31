# Chapter 7: Window Layout and Design
# Recipe 2: Understanding Proportions, Flags, and Borders
#
import wx

class SizerFlagsApp(wx.App):
    def OnInit(self):
        self.frame = SizerFlagsFrame(None,
                                     title="Sizer Flags")
        self.frame.Show()
        return True

class SizerFlagsFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SizerFlagsFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = SizerFlagsPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class SizerFlagsPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(SizerFlagsPanel, self).__init__(*args, **kwargs)

        # Attributes
        self._field1 = wx.TextCtrl(self)
        self._field2 = wx.TextCtrl(self)

        # Layout
        self._DoLayout()

    def _DoLayout(self):
        """Layout the controls"""
        vsizer = wx.BoxSizer(wx.VERTICAL)
        field1_sz = wx.BoxSizer(wx.HORIZONTAL)
        field2_sz = wx.BoxSizer(wx.HORIZONTAL)

        # Make the labels
        field1_lbl = wx.StaticText(self, label="Field 1:")
        field2_lbl = wx.StaticText(self, label="Field 2:")

        # 1) HORIZONTAL BOXSIZERS
        field1_sz.Add(field1_lbl, 0,
                      wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5)
        field1_sz.Add(self._field1, 1, wx.EXPAND)

        field2_sz.Add(field2_lbl, 0,
                      wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5)
        field2_sz.Add(self._field2, 1, wx.EXPAND)

        # 2) VERTICAL BOXSIZER
        vsizer.AddStretchSpacer()
        BOTH_SIDES = wx.EXPAND|wx.LEFT|wx.RIGHT
        vsizer.Add(field1_sz, 0, BOTH_SIDES|wx.TOP, 50)
        vsizer.AddSpacer(15)
        vsizer.Add(field2_sz, 0, BOTH_SIDES|wx.BOTTOM, 50)
        vsizer.AddStretchSpacer()

        # Finally assign the main outer sizer to the panel
        self.SetSizer(vsizer)

if __name__ == '__main__':
    app = SizerFlagsApp(False)
    app.MainLoop()
