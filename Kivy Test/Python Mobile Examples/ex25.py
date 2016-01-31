# ex25.py

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import NumericProperty

class Ex25(GridLayout):
    ANGLE = NumericProperty()
    pass
        
class Ex25App(App):
    def build(self):
        return Ex25()

if __name__=='__main__':
    Ex25App().run()
