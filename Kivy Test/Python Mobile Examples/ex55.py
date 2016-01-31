# ex55.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Ex55(BoxLayout):
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass

class Ex55App(App):
    def build(self):
        return Ex55()
    
if __name__ == '__main__':
    Ex55App().run()