# ex27.py

from kivy.uix.widget import Widget
from kivy.app import App

class Ball(Widget):
    def on_touch_down(self, touch):
        self.center=touch.pos
    
class Ex27(Widget):
    pass
       
class Ex27App(App):
    def build(self):
        return Ex27()

if __name__=='__main__':
    Ex27App().run()
