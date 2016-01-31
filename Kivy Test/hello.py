from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class MyWidget(BoxLayout):
    pass

class helloApp(App):
    def build(self):
        return MyWidget()
    
if __name__=="__main__":
    helloApp().run()
