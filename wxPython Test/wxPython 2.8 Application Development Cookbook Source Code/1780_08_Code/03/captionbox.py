# Chapter 8: Drawing to the Screen, Using Device Contexts
# Recipe 3: Utilizing SystemSettings
#
import wx

#---- Recipe Code ----#

class CaptionBox(wx.PyPanel):
    def __init__(self, parent, caption):
        super(CaptionBox, self).__init__(parent,
                                         style=wx.NO_BORDER)

        # Attributes
        self._caption = caption
        self._csizer = wx.BoxSizer(wx.VERTICAL)

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def __DoLayout(self):
        msizer = wx.BoxSizer(wx.HORIZONTAL)
        self._csizer.AddSpacer(12) # extra space for caption
        msizer.Add(self._csizer, 0, wx.EXPAND|wx.ALL, 8)
        self.SetSizer(msizer)

    def DoGetBestSize(self):
        size = super(CaptionBox, self).DoGetBestSize()
        # Compensate for wide caption labels
        tw = self.GetTextExtent(self._caption)[0]
        size.SetWidth(max(size.width, tw+20))
        return size

    def AddItem(self, item):
        """Add a window or sizer item to the CaptionBox"""
        self._csizer.Add(item, 0, wx.ALL, 5)

    def OnPaint(self, event):
        """Draws the Caption and border around the controls"""
        dc = wx.PaintDC(self)

        # Get the working rectangle we can draw in
        rect = self.GetClientRect()

        # Get the sytem color to draw the caption
        ss = wx.SystemSettings
        color = ss.GetColour(wx.SYS_COLOUR_ACTIVECAPTION)
        txtcolor = ss.GetColour(wx.SYS_COLOUR_CAPTIONTEXT)
        dc.SetTextForeground(txtcolor)

        # Draw the border
        rect.Inflate(-2, -2)
        dc.SetPen(wx.Pen(color))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawRectangleRect(rect)

        # Add the Caption
        rect = wx.Rect(rect.x, rect.y,
                       rect.width, 16)
        dc.SetBrush(wx.Brush(color))
        dc.DrawRectangleRect(rect)
        rect.Inflate(-5, 0)
        dc.SetFont(self.GetFont())
        dc.DrawLabel(self._caption, rect, wx.ALIGN_LEFT)

#---- End Recipe Code ----#

class SystemSettingsApp(wx.App):
    def OnInit(self):
        self.frame = SystemSettingsFrame(None,
                                         title="SystemSettings")
        self.frame.Show()
        return True

class SystemSettingsFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = SystemSettingsPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

class SystemSettingsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Attributes
        self.box1 = CaptionBox(self, "CaptionBox One")
        self.box2 = CaptionBox(self, "CaptionBox Two")

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer = wx.BoxSizer(wx.VERTICAL)

        # Put some checkboxes in the box
        for x in range(2):
            cb = wx.CheckBox(self.box1,
                             label="CheckBox Item %d" % x)
            self.box1.AddItem(cb)

        # Put some Buttons in the other one
        for x in range(2):
            btn = wx.Button(self.box2,
                            label="Button %d" % x)
            self.box2.AddItem(btn)

        # Add the box to the Panel
        hsizer.AddStretchSpacer()
        hsizer.Add(self.box1, 0, wx.EXPAND)
        hsizer.AddSpacer(10)
        hsizer.Add(self.box2, 0, wx.EXPAND)
        hsizer.AddStretchSpacer()
        vsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.AddStretchSpacer()
        self.SetSizer(vsizer)

if __name__ == '__main__':
    app = SystemSettingsApp(False)
    app.MainLoop()
