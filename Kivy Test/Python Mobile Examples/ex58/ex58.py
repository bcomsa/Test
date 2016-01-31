# ex58.py
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App

class Ex58(TabbedPanel):
    pass

class Ex58App(App):
    def build(self):
        return Ex58()
    
if __name__ == '__main__':
    Ex58App().run()