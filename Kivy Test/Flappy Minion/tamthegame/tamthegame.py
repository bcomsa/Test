import random
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.image import Image as CoreImage
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('tamthegame.kv')

class Tam(Image):
	def __init__(self, **kwargs):
		super(Tam, self).__init__(**kwargs)
		self.gravity = 5
		self.jump_accelerate_max = 35
		self.jump_accelerate = 0
		self.jump = False
		self.move_left = False
		self.move_right = False
		self.speed = 3

class TamTheGame(RelativeLayout):
	tam = ObjectProperty()
	def __init__(self, **kwargs):
		super(TamTheGame, self).__init__(**kwargs)

		with self.canvas.before:
			texture = CoreImage('Image/Sky.png').texture
			texture.wrap = 'repeat'
			self.rect_1 = Rectangle(texture=texture, size=self.size, pos=self.pos)
			texture = CoreImage('Image/Vegetation.png').texture
			texture.wrap = 'repeat'
			self.rect_2 = Rectangle(texture=texture, size=self.size, pos=self.pos)
			texture = CoreImage('Image/Ground.png').texture
			texture.wrap = 'repeat'
			self.rect_3 = Rectangle(texture=texture, size=self.size, pos=self.pos)

		Window.bind(on_key_down = self._on_keyboard_down,on_key_up = self._on_keyboard_up)
			
		Clock.schedule_interval(self.update, 1.0 / 30.0)

	def update(self, time):

		t = Clock.get_boottime()
		self.rect_1.tex_coords = -(t * 0.001), 0, -(t * 0.001 + 5), 0,  -(t * 0.001 + 5), -5, -(t * 0.001), -5
		self.rect_2.tex_coords = -(t * 0.01), 0, -(t * 0.01 + 1), 0,  -(t * 0.01 + 1), -1, -(t * 0.01), -1
		self.rect_3.tex_coords = -(t * 0.1), 0, -(t * 0.1 + 1), 0,  -(t * 0.1 + 1), -1, -(t * 0.1), -1

		self.tam.gravity += 0.3
		self.tam.y -= self.tam.gravity
		if self.tam.y < self.height / 5.4:
			self.tam.gravity = 5
			self.tam.y = self.height / 5.4
		if self.tam.jump:
			self.tam.jump_accelerate += 3
			if self.tam.jump_accelerate > self.tam.jump_accelerate_max:
				self.tam.jump = False
				self.tam.jump_accelerate = 0
			self.tam.y += self.tam.jump_accelerate
		if self.tam.move_left:
			self.tam.x -= self.tam.speed
		if self.tam.move_right:
			self.tam.x += self.tam.speed
		self.tam.x = min(max(self.tam.x, self.x), self.right - self.tam.width)

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers,*args):
		if keycode == 32 or keycode == 273:
			self.tam.jump = True
		if keycode == 275:
			self.tam.move_right = True
		elif keycode == 276:
			self.tam.move_left = True
	def _on_keyboard_up(self, keyboard, keycode, text,*args):
		if keycode == 275:
			self.tam.move_right = False
		elif keycode == 276:
			self.tam.move_left = False
if __name__ == '__main__':
    class TamTheGameNotDuplicateApp(App):
        def build(self):
        	#Window.size = (300,300) 
        	return TamTheGame(size=Window.size)
    TamTheGameNotDuplicateApp().run()
