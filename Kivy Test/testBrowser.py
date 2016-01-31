from kivy.garden.cefpython import CefBrowser, cefpython
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.core.window import Window

class CefBrowserApp(App):
    def build(self):
    	Window.size = (1280, 650)
    	self.box = BoxLayout(orientation = 'vertical')
    	self.header_box = BoxLayout(size_hint = (1, .06))
    	self.browser = CefBrowser(start_url='http://web.zaloapp.com')
    	self.url_box = TextInput(size_hint = (5, 1), multiline = False, on_text_validate = self.go)
    	self.back_btn = Button(text = 'back', on_press = self.back)
        self.forward_btn = Button(text = 'forward', on_press = self.forward)
        self.header_box.add_widget(self.url_box)
        self.header_box.add_widget(self.back_btn)
        self.header_box.add_widget(self.forward_btn)
        #self.box.add_widget(self.header_box)
        self.box.add_widget(self.browser)
        return self.box
    
    def back(self, *args):
    	#self.browser.go_back()
		print dir(self.browser.browser)
        
    def forward(self, *args):
    	self.browser.go_forward()

    def go(self, *args):
    	url = 'http://' + args[0].text if 'http://' not in args[0].text else args[0].text
    	self.browser.change_url(url)

CefBrowserApp().run()

cefpython.Shutdown()