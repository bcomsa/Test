# Chapter 2: Responding to Events
# Recipe 4: UpdateUI Events
#
import wx

ID_CHECK_ITEM = wx.NewId()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = TextFrame(None, title="Handling KeyEvents")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class TextFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(TextFrame, self).__init__(parent,
                                        *args,
                                        **kwargs)

        # Attributes
        self.panel = wx.Panel(self)
        self.txtctrl = wx.TextCtrl(self.panel,
                                   value="Hello World",
                                   style=wx.TE_MULTILINE)

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.CreateStatusBar() # For output display

        # Menu
        menub = wx.MenuBar()
        editm = wx.Menu()
        editm.Append(wx.ID_COPY, "Copy\tCtrl+C")
        editm.Append(wx.ID_CUT, "Cut\tCtrl+X")
        editm.Append(ID_CHECK_ITEM, "Selection Made?",
                     kind=wx.ITEM_CHECK)
        menub.Append(editm, "Edit")
        self.SetMenuBar(menub)

        # Event Handlers
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateEditMenu)

    def OnUpdateEditMenu(self, event):
        event_id = event.GetId()
        sel = self.txtctrl.GetSelection()
        has_sel = sel[0] != sel[1]
        if event_id in (wx.ID_COPY, wx.ID_CUT):
            event.Enable(has_sel)
        elif event_id == ID_CHECK_ITEM:
            event.Check(has_sel)
        else:
            event.Skip()

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
