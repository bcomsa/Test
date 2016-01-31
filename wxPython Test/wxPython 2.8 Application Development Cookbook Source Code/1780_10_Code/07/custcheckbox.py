# Chapter 10: Creating Components and Extending Functionality
# Recipe 7: Creating a Custom Control
#
import wx

class CustomCheckBox(wx.PyControl):
    """Custom CheckBox implementation where label is
    below the CheckBox.
    """
    def __init__(self, parent, id_=wx.ID_ANY, label=""):
        style = wx.BORDER_NONE
        super(CustomCheckBox, self).__init__(parent,
                                             id_,
                                             style=style)

        # Attributes
        self.InheritAttributes()
        self._hstate = 0
        self._checked = False
        self._ldown = False
        self.SetLabel(label)

        # Event Handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnErase)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_ENTER_WINDOW,
                  lambda event:
                  self._SetState(wx.CONTROL_CURRENT))
        self.Bind(wx.EVT_LEAVE_WINDOW,
                  lambda event: self._SetState(0))

    def _SetState(self, state):
        if self._hstate != state:
            if state == 0:
                self._ldown = False
            self._hstate = state
            self.Refresh()

    #-- Implementation --#

    def DoGetBestSize(self):
        lblsz = self.GetTextExtent(self.GetLabel())
        width = max(lblsz[0], 16) + 4 # 2px padding l/r
        height = lblsz[1] + 16 + 6
        best_sz = wx.Size(width, height)
        self.CacheBestSize(best_sz)
        return best_sz

    #-- Event Handlers --#

    def OnPaint(self, event):
        dc = wx.AutoBufferedPaintDCFactory(self)
        gc = wx.GCDC(dc)
        renderer = wx.RendererNative.Get()

        # Setup GCDC
        rect = self.GetClientRect()
        bcolour = self.GetBackgroundColour()
        brush = wx.Brush(bcolour)
        gc.SetBackground(brush)
        gc.Clear()

        # Center checkbox
        cb_x = (rect.width - 16) / 2
        cb_y = 2 # padding from top
        cb_rect = wx.Rect(cb_x, cb_y, 16, 16)

        # Draw the checkbox
        state = 0
        if self._checked:
            state = wx.CONTROL_CHECKED
        if not self.IsEnabled():
            state |= wx.CONTROL_DISABLED
        renderer.DrawCheckBox(self, dc, cb_rect,
                              state|self._hstate)

        # Draw the label
        lbl_rect = wx.Rect(0, cb_rect.bottom, rect.width,
                           rect.height - cb_rect.height)
        gc.DrawLabel(self.GetLabel(),
                     lbl_rect,
                     wx.ALIGN_CENTER)

    def OnErase(self, event):
        pass # do nothing

    def OnLeftDown(self, event):
        self._ldown = True
        event.Skip()

    def OnLeftUp(self, event):
        if self._ldown:
            self._ldown = False
            self._checked = not self._checked
            self.Refresh()
            # Generate EVT_CHECKBOX event
            etype = wx.wxEVT_COMMAND_CHECKBOX_CLICKED
            chevent = wx.CommandEvent(etype, self.GetId())
            chevent.SetEventObject(self)
            self.ProcessEvent(chevent)
        event.Skip()

    #---- Public Api ----#
    
    def SetValue(self, state):
        self._checked = state
        self.Refresh()

    def GetValue(self):
        return self._checked

    def IsChecked(self):
        return self.GetValue()
