# ex26.py

from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class Ex26(GridLayout):
    pass
        
class Ex26App(App):
    def build(self):
        return Ex26()

if __name__=='__main__':
    Ex26App().run()