# Chapter 8: Drawing to the Screen, Using Device Contexts
# Recipe 5: Drawing with RendererNative
#
import wx

#---- Recipe Code ----#

class DropArrowButton(wx.PyControl):
    def __init__(self, parent, id=wx.ID_ANY,
                 label="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0,
                 validator=wx.DefaultValidator,
                 name="DropArrowButton"):
        style |= wx.BORDER_NONE
        super(DropArrowButton, self).__init__(parent, id,
                                              pos, size,
                                              style,
                                              validator, name)

        # Attributes
        self._label = label
        self._menu = None
        self._state = 0

        # Event Handlers
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_LEAVE_WINDOW,
                  lambda event:
                  self.SetState(0))
        self.Bind(wx.EVT_ENTER_WINDOW,
                  lambda event:
                  self.SetState(wx.CONTROL_CURRENT))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def DoGetBestSize(self):
        size = self.GetTextExtent(self._label)
        size = (size[0]+16, size[1]+16) # Drop Arrow
        size = (size[0]+8, size[1]+4) # Padding
        self.CacheBestSize(size)
        return size

    def OnLeftDown(self, event):
        """Show the drop menu"""
        self.SetState(wx.CONTROL_PRESSED)
        if self._menu:
            size = self.GetSizeTuple()
            self.PopupMenu(self._menu, (0, size[1]))

    def OnLeftUp(self, event):
        """Send a button click event"""
        if self._state != wx.CONTROL_PRESSED:
            return

        self.SetState(wx.CONTROL_CURRENT)

    def OnPaint(self, event):
        """Draw the Conrol"""
        dc = wx.PaintDC(self)
        gc = wx.GCDC(dc) # AA text

        # Get the renderer singleton
        render = wx.RendererNative.Get()

        # Get the working rectangle we can draw in
        rect = self.GetClientRect()

        # Draw the button
        render.DrawPushButton(self, gc, rect, self._state)
        # Draw the label on the button
        lblrect = wx.Rect(rect.x+4, rect.y+2,
                          rect.width-24, rect.height-4)
        gc.DrawLabel(self._label, lblrect, wx.ALIGN_CENTER)
        # Draw drop arrow
        droprect = wx.Rect((rect.x+rect.width)-20,
                           rect.y+2, 16, rect.height-4)
        state = self._state
        if state != wx.CONTROL_PRESSED:
            state = wx.CONTROL_CURRENT
        render.DrawDropArrow(self, gc, droprect, state)

    def SetMenu(self, menu):
        """Set the buttons drop menu
        @param menu: wx.Menu
        """
        if self._menu:
            self._menu.Destroy()
        self._menu = menu

    def SetState(self, state):
        self._state = state
        self.Refresh()

#---- End Recipe Code ----#

class DropMenuApp(wx.App):
    def OnInit(self):
        self.frame = DropMenuFrame(None,
                                   title="RendererNative")
        self.frame.Show()
        return True

class DropMenuFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(DropMenuFrame, self).__init__(*args, **kwargs)

        # Attributes
        self.panel = DropMenuPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.CreateStatusBar()

class DropMenuPanel(wx.Panel):
    def __init__(self, parent):
        super(DropMenuPanel, self).__init__(parent)

        # Attributes
        self.button = DropArrowButton(self, label="Hello")
        menu = wx.Menu()
        menu.Append(wx.NewId(), "Item1")
        menu.Append(wx.NewId(), "Item2")
        menu.Append(wx.NewId(), "Item3")
        self.button.SetMenu(menu)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        msizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        msizer.AddStretchSpacer()
        hsizer.AddStretchSpacer()
        hsizer.Add(self.button)
        hsizer.AddStretchSpacer()
        msizer.Add(hsizer, 0, wx.EXPAND)
        msizer.AddStretchSpacer()
        self.SetSizer(msizer)

if __name__ == '__main__':
    app = DropMenuApp(False)
    app.MainLoop()
