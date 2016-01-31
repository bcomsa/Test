from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty

class MyLayout(GridLayout):
    angle_shift = NumericProperty(0)

class TestApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    TestApp().run()
