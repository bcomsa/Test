# Chapter 5: Providing Information and Alerting Users
# Recipe 4: BalloonTip
#
import wx

#---- Recipe Code ----#
import wx.lib.agw.balloontip as btip

class TaskBarBalloon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarBalloon, self).__init__()

        # Setup
        icon = wx.Icon("face-monkey.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        # Setup BallooTip
        title="BalloonTip Recipe"
        msg = "Welcome to the Balloon Tip Recipe"
        bmp = wx.BitmapFromIcon(icon)
        self.tip = btip.BalloonTip(topicon=bmp,
                                   toptitle=title,
                                   message=msg,
                                   shape=btip.BT_ROUNDED,
                                   tipstyle=btip.BT_BUTTON)
        self.tip.SetStartDelay(1000)
        self.tip.SetTarget(self)

        # Event Handlers
        self.Bind(wx.EVT_MENU, self.OnMenu)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_CLOSE, "Exit")
        return menu

    def OnMenu(self, event):
        self.RemoveIcon()
        self.tip.DestroyTimer()
        self.Destroy()

#---- End Recipe Code ----#

class MyApp(wx.App):
    def OnInit(self):
        self.tbicon = TaskBarBalloon()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
