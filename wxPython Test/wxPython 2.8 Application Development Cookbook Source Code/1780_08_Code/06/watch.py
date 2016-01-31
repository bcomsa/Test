# Chapter 8: Drawing to the Screen, Using Device Contexts
# Recipe 6: Reducing Flicker in Drawing Routines
#
import wx

class WristWatchApp(wx.App):
    def OnInit(self):
        self.frame = WristWatchFrame(None,
                                     title="Reducing Flicker")
        self.frame.Show()
        return True

class WristWatchFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WristWatchFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.back = wx.Panel(self)
        self.back.SetBackgroundColour(wx.BLACK)
        self.watch = WristWatchCtrl(self.back)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        bsizer = wx.BoxSizer(wx.VERTICAL)
        bsizer.AddStretchSpacer()
        bsizer.Add(self.watch, 0, wx.ALIGN_CENTER)
        bsizer.AddStretchSpacer()
        self.back.SetSizer(bsizer)
        sizer.Add(self.back, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()


class WristWatchCtrl(wx.PyControl):
    """Digital Wrist Watch Control"""
    def __init__(self, parent):
        super(WristWatchCtrl, self).__init__(parent)

        # Attributes
        self.timer = wx.Timer(self)
        self.timerect = wx.Rect()

        # Setup
        font = self.GetFont()
        font.SetPointSize(13)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.SetFont(font)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        # Event Handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnErase)
        self.Bind(wx.EVT_TIMER,
                  self.OnUpdateTime,
                  self.timer)

        self.timer.Start(1000)

    def __del__(self):
        self.timer.Stop()

    def DoGetBestSize(self):
        """Virtual override for PyPanel"""
        timesz = self.GetTextExtent("00:00:00")
        timesz = timesz + (40, 8) # padding
        # Fixed size (that accounts for diff font widths)
        return wx.Size(max(100, timesz[0]), 300)

    def OnUpdateTime(self, event):
        # Refresh causes the framework to generate
        # a new paint event.
        self.Refresh(rect=self.timerect)

    def OnErase(self, event):
        # Do nothing, reduces flicker by removing
        # unneeded background erasures and redraws
        pass

    def OnPaint(self, event):
        """Draw the image on to the panel"""
        # Create a Buffered PaintDC
        dc = wx.AutoBufferedPaintDCFactory(self)
#        dc = wx.PaintDC(self) # replace above line with this to see flicker
        # Transform to GCDC
        gcdc = wx.GCDC(dc)
        self.DoDrawWatch(gcdc)

    def DoDrawWatch(self, dc):
        """@param dc: Device Context"""
        # Get the working rectangle
        rect = self.GetClientRect()

        # Setup the DC
        dc.SetFont(self.GetFont())
        dc.SetTextForeground(wx.BLACK)
        dc.SetBrush(wx.WHITE_BRUSH)
        dc.SetPen(wx.WHITE_PEN)

        # Fill the background in with white to start
        dc.DrawRectangleRect(rect)

        # Change the pen back to black
        dc.SetPen(wx.BLACK_PEN)

        # Do some calculations to get some of our base sizes
        # Rectangle that will hold the time i.e "12:24:02"
        timesz = self.GetTextExtent("00:00:00") + (20, 8)
        # The rectangle for the main face of the watch
        facesz = (timesz[0] + 10, timesz[1] * 4)
        facesz = (max(facesz), max(facesz))
        # Band size is the height of the control and
        # half the width of the face.
        bandsz = (facesz[0] / 2, rect.height)

        # Draw the wrist band
        bandx = (rect.width - bandsz[0]) / 2 # x cord
        bandrect = wx.Rect(bandx, 0, bandsz[0], bandsz[1])
        self.DoDrawBand(dc, bandrect)

        # Draw the face on the center of the band
        facex = (rect.width - facesz[0]) / 2
        facey = (rect.height - facesz[1]) / 2
        frect = wx.Rect(facex, facey, facesz[0], facesz[1])
        self.DoDrawFace(dc, frect, timesz)

    def DoDrawBand(self, dc, rect):
        """Draw one part of the wrist band
        @param dc: Device Context
        @param rect: wx.Rect
        """
        # Save current brush
        cbrush = dc.GetBrush()
        
        # create a graphics context to
        gc = dc.GetGraphicsContext()
        gc.SetPen(dc.GetPen())

        # Draw the band as 16 smaller rectangles
        rh = rect.height / 16
        bandrects = list()
        for part in range(16):
            cy = (part * rh) + rect.y
            band = wx.Rect(rect.x, cy, rect.width, cy + rh)
            brush = gc.CreateLinearGradientBrush(band.x,
                                                 band.y,
                                                 band.x,
                                                 band.height,
                                                 wx.BLACK,
                                                 wx.WHITE)
            gc.SetBrush(brush)
            dc.DrawRectangle(band.x, band.y,
                             band.width, band.height)

        # Restore brush
        dc.SetBrush(cbrush)

    def DoDrawFace(self, dc, rect, timesz):
        """Draw the face of the watch
        @param dc: Device Context
        @param rect: face rect
        @param timesz: Size of time rect
        """
        cbrush = dc.GetBrush()

        # Create a GraphicsContext
        gc = dc.GetGraphicsContext()

        # Find the center of the rect
        center = (rect.x + (rect.width / 2),
                  rect.y + (rect.height / 2))

        # Draw a circle for the face
        radius = rect.width/2
        brush = gc.CreateRadialGradientBrush(center[0],
                                             center[1],
                                             center[0],
                                             center[1],
                                             radius*1.25,
                                             wx.WHITE,
                                             wx.BLACK)
        gc.SetBrush(brush)
        pen = dc.GetPen()
        dc.SetPen(wx.Pen(wx.BLACK, 2))
        dc.DrawCircle(center[0], center[1], rect.width/2)
        dc.SetPen(pen)

        # Draw a rectangle for the time display in the center
        # of the face.
        timerect = wx.Rect(width=timesz[0], height=timesz[1])
        timerect = timerect.CenterIn(rect)
        self.timerect = timerect # save time rect
        x, y = timerect.x, timerect.y
        y2 = y + timerect.height
        brush = gc.CreateLinearGradientBrush(x, y*.9,
                                             x, y2,
                                             wx.BLUE,
                                             wx.WHITE)
        gc.SetBrush(brush)
        dc.DrawRectangleRect(timerect)

        # Draw the current time in the watch
        dt = wx.DateTime_Now()
        timestr = dt.FormatTime()
        dc.DrawLabel(timestr, timerect, wx.ALIGN_CENTER)

        # Restore the brush
        dc.SetBrush(cbrush)

if __name__ == '__main__':
    app = WristWatchApp(False)
    app.MainLoop()
