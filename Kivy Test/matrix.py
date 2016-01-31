from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Example(BoxLayout):
    pass
class matrixApp(App):
    def build(self):
        return Example()

if __name__ == '__main__':
    matrixApp().run()
