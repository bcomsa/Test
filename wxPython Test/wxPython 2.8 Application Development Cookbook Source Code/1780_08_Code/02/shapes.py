# Chapter 8: Drawing to the Screen, Using Device Contexts
# Recipe 1: Screen Drawing
#
import os
import wx

#---- Recipe Code ----#

class Smiley(wx.PyControl):
    def __init__(self, parent, size=(50,50)):
        super(Smiley, self).__init__(parent,
                                     size=size,
                                     style=wx.NO_BORDER)

        # Event Handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        """Draw the image on to the panel"""
        dc = wx.PaintDC(self) # Must create a PaintDC

        # Get the working rectangle we can draw in
        rect = self.GetClientRect()

        # Setup the DC
        dc.SetPen(wx.BLACK_PEN) # for drawing lines / borders
        yellowbrush = wx.Brush(wx.Colour(255, 255, 0))
        dc.SetBrush(yellowbrush) # Yellow fill

        # Find the center and draw the circle
        cx = (rect.width / 2) + rect.x
        cy = (rect.width / 2) + rect.y
        radius = min(rect.width, rect.height) / 2
        dc.DrawCircle(cx, cy, radius)

        # Give it some square blue eyes
        # Calc the size of the eyes 1/8th total
        eyesz = (rect.width / 8, rect.height / 8)
        eyepos = (cx / 2, cy / 2)
        dc.SetBrush(wx.BLUE_BRUSH)
        dc.DrawRectangle(eyepos[0], eyepos[1],
                         eyesz[0], eyesz[1])
        eyepos = (eyepos[0] + (cx - eyesz[0]), eyepos[1])
        dc.DrawRectangle(eyepos[0], eyepos[1],
                         eyesz[0], eyesz[1])
        
        # Draw the smile
        dc.SetBrush(yellowbrush)
        startpos = (cx / 2, (cy / 2) + cy)
        endpos = (cx + startpos[0], startpos[1])
        dc.DrawArc(startpos[0], startpos[1],
                   endpos[0], endpos[1], cx, cy)

        # Draw a yellow rectangle to cover up the
        # unwanted black lines from the wedge part of
        # our arc
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(startpos[0], cy,
                         endpos[0] - startpos[0],
                         startpos[1] - cy)

#---- End Recipe Code ----#

class SmileyApp(wx.App):
    def OnInit(self):
        self.frame = SmileyFrame(None,
                                 title="Drawing Shapes",
                                 size=(300,400))
        self.frame.Show()
        return True

class SmileyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = SmileyPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

class SmileyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        # Layout a grid of 4 smileys
        msizer = wx.GridSizer(2, 2, 0, 0)

        for x in range(4):
            smile = Smiley(self)
            msizer.Add(smile, 0, wx.EXPAND)

        self.SetSizer(msizer)

if __name__ == '__main__':
    app = SmileyApp(False)
    app.MainLoop()
