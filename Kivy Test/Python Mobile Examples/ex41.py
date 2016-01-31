# ex41.py

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ListProperty

class ScreenCircle(Screen):
    pass

class ScreenSquare(Screen):
    pass

class ScreenColor(Screen):
    pass

class Ex41(ScreenManager):
    selected_color = ListProperty([1,0,0,1])
          
class Ex41App(App):
    def build(self):
        return Ex41()

if __name__=='__main__':
    Ex41App().run()
