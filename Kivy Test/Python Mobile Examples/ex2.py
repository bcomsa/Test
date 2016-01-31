from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class BindFunc(BoxLayout):
    def __init__(self, **kwargs):
        super(BindFunc, self).__init__(**kwargs)
        btn1 = Button(text = 'Hello')
        btn1.bind(on_press = self.hello)
        self.add_widget(btn1)
    def hello(self, obj):
        print 'Hello'
class BindApp(App):
    def build(self):
        return BindFunc()
if __name__ == '__main__':
    BindApp().run()
