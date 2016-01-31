from kivy.garden.cefpython import CefBrowser, cefpython
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App

Builder.load_string('''
#:import Window kivy.core.window.Window
<Youtube>:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1, .06
        TextInput:
            id: search_box
            size_hint: 5, 1
            multiline: False
        Button:
            id: back_btn
            on_press: root.back()
        Button:
            id: forward_btn
            on_press: root.forward()
    YoutubeScreen:
        id: youtube_screen
''')
class YoutubeScreen(CefBrowser):
    def __init__(self, **kwargs):
        super(YoutubeScreen, self).__init__(**kwargs)
        self.start_url = 'https://www.youtube.com'

class Youtube(BoxLayout):
    def __init__(self, **kwargs):
        super(Youtube, self).__init__(**kwargs)
        self.youtube_screen = self.ids['youtube_screen']

    def back(self, *args):
        self.youtube_screen.go_back()

    def forward(self, *args):
        self.youtube_screen.go_forward()

    def on_search(self, *args):
        try:
            url = 'https://www.youtube.com/results?search_query=%s'%args[1]
            self.youtube_screen.change_url(url)
        except:
            pass

class YoutubeApp(App):
    def build(self):
        Window.size = (1280, 600)
        return Youtube()
    


YoutubeApp().run()

cefpython.Shutdown()