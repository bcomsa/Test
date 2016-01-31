# ex42.py

from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class SquareWidget(Widget):
    pass

class ScatterWidget(Scatter):
    pass

class Ex42(RelativeLayout):
    pass
          
class Ex42App(App):
    def build(self):
        return Ex42()

if __name__=='__main__':
    Ex42App().run()
