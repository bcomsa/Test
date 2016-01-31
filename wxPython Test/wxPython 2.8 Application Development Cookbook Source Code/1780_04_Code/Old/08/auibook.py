# Chapter 4: An Applications Building Blocks, Advanced Controls
# Recipe 8: AuiNotebook
#
import wx
import wx.aui as aui

#---- Recipe Code ----#

class MyAuiNotebook(aui.AuiNotebook):
    def __init__(self, parent):
        super(MyAuiNotebook, self).__init__(parent)

        # Setup
        self._art = MyAuiTabRender()
        self.SetArtProvider(self._art)
        for x in range(3):
            self.AddPage(wx.TextCtrl(self), "Page %d" % x)

class MyAuiTabRender(aui.PyAuiTabArt):
    def __init__(self):
        super(MyAuiTabRender, self).__init__()

        # Attributes
        self.closeb = wx.Bitmap("closebtn.png",
                                wx.BITMAP_TYPE_PNG)

    def Clone(self):
        clone = MyAuiTabRender()
        clone.closeb = self.closeb
        return clone

    def DrawTab(self, dc, wnd, page, rect, close_btn_state):
        xpos = rect.x
        font = self.GetNormalFont()
        if page.active:
            font = self.GetSelectedFont()
        dc.SetFont(font)

        # Calculate text position
        xpos += 3
        extent = dc.GetTextExtent(page.caption)
        tx = xpos
        xpos += extent[0] + 3

        # Calculate close button position
        btn_rect = wx.Rect()
        btny = 0
        btnx = 0
        if page.active:
            bsz = self.closeb.GetSize()
            btny = (rect.height - bsz[1]) / 2
            btnx = xpos
            btn_rect = wx.Rect(xpos, btny, bsz[0], bsz[1])
            xpos += bsz[0] + 3

        # Draw the background and tab border
        tabrect = wx.Rect(rect.x, rect.y, xpos - rect.x, rect.height)
        dc.DrawRectangleRect(tabrect)

        # Draw the Label
        dc.DrawText(page.caption, tx,
                    (rect.height - extent[1]) / 2)

        # Draw the close button
        if page.active:
            dc.DrawBitmap(self.closeb, btnx, btny)

        return (tabrect, btn_rect, tabrect.width)

    def GetTabSize(self, dc, wnd, caption, bmp, active, close_btn_state):
        # Get the size of the tabs label
        tw, th = wnd.GetTextExtent(caption)

        # Account for a bitmap if any
        if bmp.IsOk():
            tw += bmp.GetSize()[0] + 5
            th = max(th, bmp.GetSize()[1])

        # Account for close button when active
        if active:
            tw += 24

        # Padding space for label
        tw += 8
        return (wx.Size(tw, th+8), tw)

#---- End Recipe Code ----#

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="AuiNotebook", size=(400,500))
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = MyPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Attributes
        self.nb = MyAuiNotebook(self)

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
