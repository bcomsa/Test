# ex18.py

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Ex18(BoxLayout):
    def newWeights(self, *args):
        t = args[1]
        self.ids['w0'].value = (1-t)**3
        self.ids['w1'].value = 3*t*(1-t)**2
        self.ids['w2'].value = 3*t**2*(1-t)
        self.ids['w3'].value = t**3
        
class Ex18App(App):
    def build(self):
        self.title="Weights of 4-point Bezier curve"
        return Ex18()

if __name__=='__main__':
    Ex18App().run()
