# Chapter 4: An Applications Building Blocks, Advanced Controls
# Recipe 5: Tray Icons
#
import wx

#---- Recipe Code ----#

class CustomTaskBarIcon(wx.TaskBarIcon):
    ID_HELLO = wx.NewId()
    ID_HELLO2 = wx.NewId()
    def __init__(self):
        super(CustomTaskBarIcon, self).__init__()

        # Setup
        icon = wx.Icon("face-monkey.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def CreatePopupMenu(self):
        """Base class virtual method for creating the
        popup menu for the icon.
        """
        menu = wx.Menu()
        menu.Append(CustomTaskBarIcon.ID_HELLO, "HELLO")
        menu.Append(CustomTaskBarIcon.ID_HELLO2, "Hi!")
        menu.AppendSeparator()
        menu.Append(wx.ID_CLOSE, "Exit")
        return menu

    def OnMenu(self, event):
        evt_id = event.GetId()
        if evt_id == CustomTaskBarIcon.ID_HELLO:
            wx.MessageBox("Hello World!", "HELLO")
        elif evt_id == CustomTaskBarIcon.ID_HELLO2:
            wx.MessageBox("Hi Again!", "Hi!")
        elif evt_id == wx.ID_CLOSE:
            self.Destroy()
        else:
            event.Skip()

#---- End Recipe Code ----#

class MyApp(wx.App):
    def OnInit(self):
        self.tbicon = CustomTaskBarIcon()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
