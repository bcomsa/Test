# ex57.py
from kivy.uix.accordion import Accordion
from kivy.app import App

class Ex57(Accordion):
    pass

class Ex57App(App):
    def build(self):
        return Ex57()
    
if __name__ == '__main__':
    Ex57App().run()