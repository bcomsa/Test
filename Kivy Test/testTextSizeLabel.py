from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<Test@BoxLayout>:
	Button:
		text: 'hihi'*100
		text_size: self.width, 100
''')
class Test(BoxLayout):
	pass
class testApp(App):
	def build(self):
		pass
		return Test()

if __name__ == '__main__':
	testApp().run()
