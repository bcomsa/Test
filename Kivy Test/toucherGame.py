import random, sys
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

Builder.load_string('''

<Player>:
	canvas.before:
		Color:
			rgb: (1, 0, 0)
		Ellipse:
			size: self.size
			pos: self.pos

<Enemy>:
	canvas.before:
		Color:
			rgb: self.enemy_color
		Ellipse:
			size: self.size
			pos: self.pos
<Life>:
	canvas.before:
		Color:
			rgb: (1, 0, 0)
		Ellipse:
			size: 30, 30
			pos: self.x + self.width/2 - 15, self.y + self.height/2 - 15

<TouchGame>:
	RelativeLayout:
		id: _game_box
		canvas.before:
			Color:
				rgb: (0, 1, 0)
			Rectangle:
				size: self.size
				pos: 0, 0
		Label:
			id: _attack_lbl
			pos_hint: {'center': (.5, .5)}
			size_hint: .3, .2
	BoxLayout:
		orientation: 'vertical'
		canvas.before:
			Color:
				rgb: (1, 1, 0)
			Rectangle:
				size: self.size
				pos: self.pos
		BoxLayout:
			id: _enemy_hp_box
			Life:
			Life:
			Life:
		BoxLayout:
			id: _player_hp_box
			Life:
			Life:
			Life:
		Label:
			id: _score_box
			text: str(0)
	RelativeLayout:
		canvas.before:
			Color:
				rgb: (0, 0, 1)
			Rectangle:
				size: self.size
				pos: 0, 0
		Button:
			id: _attack_btn
			pos_hint: {'center': (.5, .5)}
			size_hint: .3, .2
			on_press: root.attack()

''')
class Life(Widget):
	pass

class Player(Widget):
	"""docstring for Player"""
	def __init__(self, **kwargs):
		super(Player, self).__init__(**kwargs)


class Enemy(Widget):
	"""docstring for Enemy"""
	ENEMY_X = 200
	ENEMY_HP = 3
	enemy_color = ListProperty([random.random(), random.random(), random.random()])

	def __init__(self, **kwargs):
		super(Enemy, self).__init__(**kwargs)

class TouchGame(BoxLayout):

	def __init__(self, **kwargs):
		super(TouchGame, self).__init__(**kwargs)
		self.attack_btn = self.ids['_attack_btn']
		self.attack_lbl = self.ids['_attack_lbl']
		self.player_hp_box = self.ids['_player_hp_box']
		self.enemy_hp_box = self.ids['_enemy_hp_box']
		self.score_box = self.ids['_score_box']
		self.game_box = self.ids['_game_box']
		self.score = 0
		self.player = Player(pos=(100, 200), size_hint=(None, None), size=(20, 20))
		self.enemy = Enemy(pos=(Enemy.ENEMY_X, 200), size_hint=(None, None), size=(20, 20))
		self.enemy.hp = Enemy.ENEMY_HP
		self.game_box.add_widget(self.player)
		self.game_box.add_widget(self.enemy)
		Clock.schedule_interval(self.loop, 0.01)

	def attack(self):
		self.enemy.x += 20

	def loop(self, dt):
		self.enemy.x -= 3
		self.enemy.x = min(self.enemy.x, Enemy.ENEMY_X + 1)
		if self.enemy.collide_widget(self.player):
			self.enemy.x = 200
			self.player_lose_hp()
		if self.enemy.x == Enemy.ENEMY_X + 1:
			self.enemy_lose_hp()

	def enemy_reset(self):
		self.score += 1
		self.score_box.text = str(self.score)
		self.enemy.x = Enemy.ENEMY_X
		self.enemy.hp = Enemy.ENEMY_HP
		self.enemy.enemy_color = [random.random(), random.random(), random.random()]
		for i in range(Enemy.ENEMY_HP):
			self.enemy_hp_box.add_widget(Life())

	def player_reset(self):
		sys.exit(0)

	def player_lose_hp(self):
		try:
			self.player_hp_box.remove_widget(self.player_hp_box.children[0])
		except:
			self.player_reset()

	def enemy_lose_hp(self):
		self.enemy.hp -= 1
		try:
			self.enemy_hp_box.remove_widget(self.enemy_hp_box.children[0])
		except:
			self.enemy_reset()
class TouchApp(App):
	def build(self):
		Window.size = (800, 400)
		return TouchGame()
if __name__ == '__main__':
	TouchApp().run()
