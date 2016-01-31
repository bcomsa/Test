# Chapter 10: Creating Components and Extending Functionality
# Recipe 5: Working with ListCtrl Mixins
#
import wx
import wx.lib.mixins.listctrl as listmix

#---- Recipe Code ----#

class CheckListCtrl(wx.ListCtrl,
                    listmix.CheckListCtrlMixin,
                    listmix.ListRowHighlighter,
                    listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListRowHighlighter.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

        # Attributes
        self._observers = list()

    def OnCheckItem(self, index, flag):
        """Overrides CheckListCtrlMixin.OnCheckItem callback"""
        # Notify observers that a checkbox was checked/unchecked
        for observer in self._observers:
            observer(index, flag)

    def GetItems(self, checked=True):
        """Gets a list of all the (un)checked items"""
        indexes = list()
        for index in range(self.GetItemCount()):
            if self.IsChecked(index) == checked:
                indexes.append(index)
        return indexes

    def RegisterObserver(self, callback):
        """Register OnCheckItem callback
        @param callaback: callable(index, checked)
        """
        self._observers.append(callback)

#---- End Recipe Code ----#

#---- Example usage of the CheckListCtrl ----#

class IngredientsList(CheckListCtrl):
    def __init__(self, *args, **kwargs):
        super(IngredientsList, self).__init__(*args, **kwargs)

        # Setup
        self.InsertColumn(0, "Include")
        self.InsertColumn(1, "Ingredient Name")

    def Append(self, item):
        """Overrides ListCtrl.Append. item should be
        a tuple with the first item being a boolean value.
        """
        assert len(item) == 2
        assert isinstance(item[0], bool)
        super(IngredientsList, self).Append(('', item[1]))
        idx = self.GetItemCount() - 1
        self.CheckItem(idx, item[0])

    def GetSelectedIngredients(self):
        items = self.GetItems(checked=True)
        stritems = list()
        for item in items:
            val = self.GetItem(item, 1).GetText()
            stritems.append(val)
        return stritems

#---- End Recipe Code ----#

class CheckListApp(wx.App):
    def OnInit(self):
        self.frame = CheckListFrame(None,
                                    title="ListCtrl Mixins")
        self.frame.Show()
        return True

class CheckListFrame(wx.Frame):
    """Main application window"""
    def __init__(self, parent, *args, **kwargs):
        super(CheckListFrame, self).__init__(parent, *args, **kwargs)

        # Attributes
        self.panel = CheckListPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((300, 150))

class CheckListPanel(wx.Panel):
    def __init__(self, parent):
        super(CheckListPanel, self).__init__(parent)

        # Attributes
        self._list = IngredientsList(self, style=wx.LC_REPORT)
        self.pbtn = wx.Button(self, label="Print Selected")
        self.pbtn.Enable(False)

        # Setup
        self.__DoLayout()
        ingredients = ("flour", "salt", "sugar", "eggs", "milk",
                       "raisins", "baking soda", "cream", "garlic",
                       "chocolate", "coconut", "carrots", "onions")
        for item in ingredients:
            self._list.Append((False, item))

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnPrintBtn)
        self._list.RegisterObserver(self.OnItemChecked)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(self.pbtn, 0, wx.ALIGN_CENTER|wx.ALL, 10)
        hsizer.AddStretchSpacer()
        vsizer.Add(self._list, 1, wx.EXPAND)
        vsizer.Add(hsizer, 0, wx.EXPAND)
        self.SetSizer(vsizer)

    def OnPrintBtn(self, event):
        items = self._list.GetSelectedIngredients()
        print "Selected Ingredients"
        print "\n".join(items)

    def OnItemChecked(self, index, checked):
        if len(self._list.GetItems(checked=True)):
            self.pbtn.Enable(True)
        else:
            self.pbtn.Enable(False)

if __name__ == '__main__':
    app = CheckListApp(False)
    app.MainLoop()
