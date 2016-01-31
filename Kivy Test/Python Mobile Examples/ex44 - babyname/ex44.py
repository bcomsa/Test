# ex44.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.properties import ListProperty
from bname import rlists

class FirstListItemButton(ListItemButton):
    pass

class SecondListItemButton(ListItemButton):
    pass

class ThirdListItemButton(ListItemButton):
    pass

class Ex44(BoxLayout):
    d1 = ListProperty(
        [str(i) for i in range(1880,2014)] )
    d2 = ListProperty(['']*100)
    d3 = ListProperty(['']*100)
    def change(self,c):
        try: self.d2,self.d3 = rlists(int(c.text))
        except:
            import os
            CurDir = os.getcwd()
            print('Can not find data in ' + CurDir) 
    def change1(self,c):
        print('M => '+c.text)
    def change2(self,c):
        print('F => '+c.text)

class Ex44App(App):
    def build(self):
        return Ex44()

if __name__ == '__main__':
    Ex44App().run()