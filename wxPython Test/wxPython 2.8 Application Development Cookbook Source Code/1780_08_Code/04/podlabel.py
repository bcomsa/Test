# Chapter 8: Drawing to the Screen, Using Device Contexts
# Recipe 4: Using a GraphicsContext
#
import wx

#---- Recipe Code ----#

class PodLabel(wx.PyControl):
    def __init__(self, parent, label, color):
        super(PodLabel, self).__init__(parent,
                                       style=wx.NO_BORDER)

        # Attributes
        self._label = label
        self._color = color

        # Event Handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def DoGetBestSize(self):
        txtsz = self.GetTextExtent(self._label)
        size = wx.Size(txtsz[0] + 10, txtsz[1] + 6)
        return size

    def OnPaint(self, event):
        """Draws the Caption and border around the controls"""
        dc = wx.PaintDC(self)
        gcdc = wx.GCDC(dc)
        gc = gcdc.GetGraphicsContext()

        # Get the working rectangle we can draw in
        rect = self.GetClientRect()

        # Setup the GraphicsContext
        gc.SetPen(wx.TRANSPARENT_PEN)
        rgb = self._color.Get(False)
        alpha = self._color.Alpha() *.2 # fade to transparent
        color2 = wx.Colour(*rgb, alpha=alpha)
        x1, y1 = rect.x, rect.y
        y2 = y1 + rect.height
        gradbrush = gc.CreateLinearGradientBrush(x1, y1,
                                                 x1, y2,
                                                 self._color,
                                                 color2)
        gc.SetBrush(gradbrush)

        # Draw the background
        gc.DrawRoundedRectangle(rect.x, rect.y,
                                rect.width, rect.height,
                                rect.height/2)
        # Use the GCDC to help draw the aa text
        gcdc.DrawLabel(self._label, rect, wx.ALIGN_CENTER)

#---- End Recipe Code ----#

class GraphicsContextApp(wx.App):
    def OnInit(self):
        self.frame = GraphicsContextFrame(None,
                                          title="GraphicsContext")
        self.frame.Show()
        return True

class GraphicsContextFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(GraphicsContextFrame, self).__init__(self, *args, **kwargs)

        # Attributes
        self.panel = GraphicsContextPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class GraphicsContextPanel(wx.Panel):
    def __init__(self, parent):
        super(GraphicsContextPanel, self).__init__(parent)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.AddStretchSpacer()
        # Add some labels and fields
        for color in (wx.RED, wx.GREEN, wx.BLUE):
            field = wx.BoxSizer(wx.HORIZONTAL)
            pod = PodLabel(self, "Label Text:", color)
            field.Add(pod, 0, wx.ALIGN_CENTER_VERTICAL)
            field.Add(wx.TextCtrl(self), 1, wx.EXPAND|wx.LEFT, 8)
            vsizer.Add(field, 0, wx.ALL, 5)
        vsizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.Add(vsizer, 0, wx.EXPAND)
        hsizer.AddStretchSpacer()

        self.SetSizer(hsizer)

if __name__ == '__main__':
    app = GraphicsContextApp(False)
    app.MainLoop()
