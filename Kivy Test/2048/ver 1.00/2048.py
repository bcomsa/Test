from processor import _2048MainGame
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation

Builder.load_string('''
<_2048Button>:
	markup: True
	font_size: 25
	font_name: '2048.ttf'
	background_normal: 'bg_btn.png'
<_2048Game>:
	orientation: 'vertical'
	BoxLayout:
		size_hint: 1, .2
		Button:
			markup: True
			text: '[color=ffff00]New Game[/color]'
			on_release: root.newGame()
		Button:
			id: _undo_btn
			markup: True
			text: '[color=ffff00]Undo : 2[/color]'
			on_release: root.undo()
	Label:
		id: _score_lbl
		size_hint: 1, .2
	GridLayout:
		id: _main_game
		cols: 4
	TimerLabel:
		id: _timer
		size_hint: 1, .2
	BoxLayout:
		size_hint: 1, .2
		Button:
			id: _up
			text: 'up'
			on_release: root.up()
		Button:
			id: _down
			text: 'down'
			on_release: root.down()
		Button:
			id: _left
			text: 'left'
			on_release: root.left()
		Button:
			id: _right
			text: 'right'
			on_release: root.right()
''')

class _2048Button(Button):
	def __init__(self, **kwargs):
		super(_2048Button, self).__init__(**kwargs)
		self.rect = Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.update_rect, size=self.update_rect)  # bind rect in canvas to button
		self.mutexAnimation = False  # only one animation do at same time

	def update_rect(self, *args):
		self.rect.pos = self.pos
		self.rect.size = self.size

	def changeBackground(self, background=(1, 1, 1, 1)):
		self.canvas.before.add(Color(rgba=background))
		self.canvas.before.add(self.rect)

	def doAnimation(self):
		if not self.mutexAnimation:
			anim = Animation(pos=(self.x + 10, self.y + 10), duration=.05) + \
					Animation(pos=(self.x, self.y), duration=.05)
			anim.bind(on_start=self.on_start)
			anim.bind(on_progress=self.on_progress)
			anim.bind(on_complete=self.on_complete)
			anim.start(self)

	def on_start(self, *args):
		self.mutexAnimation = True

	def on_progress(self, *args):
		pass

	def on_complete(self, *args):
		self.mutexAnimation = False

class TimerLabel(Label):
	time = NumericProperty(0)

	def __init__(self, **kwargs):
		super(TimerLabel, self).__init__(**kwargs)
		self.markup = True
		self.text = "[b]Playing Time: 00:00[/b]"

	def on_time(self, obj, val):
		self.text = "[b][color=ff0000]" + "Playing Time: " + self.convertSecondToMinute(val) + "[/color][/b]"

	def convertSecondToMinute(self, second):
		minute = 0
		while second > 59:
			minute += 1
			second -= 60
		return "%02d:%02d" % (minute, second)

	def update_timer(self, dt):
		self.time += 1

	def resetTimer(self):
		self.text = "[b]Playing Time: 00:00[/b]"
		self.time = 0

	def scheduleTimer(self):
		Clock.schedule_interval(self.update_timer, 1)

	def unscheduleTimer(self):
		Clock.unschedule(self.update_timer)

class WinGamePopup(Popup):
	def __init__(self, **kwargs):
		super(WinGamePopup, self).__init__(**kwargs)
		self.title = '2048'
		self.title_align = 'center'
		self.auto_dismiss = False
		self.on_new_game = kwargs['on_new_game']  # callback when click new game
		self.on_continue = kwargs['on_continue']  # callback when click continue
		self.container = BoxLayout(orientation='vertical')
		self.status_lbl = Label(halign='center', valign='middle', \
								text='You Win', font_size=25)
		self.continue_btn = Button(text="Keep Going", on_release=self.continue_callback)
		self.new_game_btn = Button(text="New Game", on_release=self.new_game_callback)
		self.container.add_widget(self.status_lbl)
		self.container.add_widget(self.continue_btn)
		self.container.add_widget(self.new_game_btn)
		self.content = self.container

	def new_game_callback(self, *args):
		self.on_new_game()
		self.dismiss()

	def continue_callback(self, *args):
		self.on_continue()
		self.dismiss()

class EndGamePopup(Popup):
	def __init__(self, **kwargs):
		super(EndGamePopup, self).__init__(**kwargs)
		self.auto_dismiss = False
		self.on_new_game = kwargs['on_new_game']  # callback when click new game
		self.container = BoxLayout(orientation='vertical')
		self.status_lbl = Label(halign='center', valign='middle')
		self.new_game_btn = Button(text="New Game", on_release=self.new_game_callback)
		self.exit_btn = Button(text="Exit Game", on_release=App.get_running_app().stop)
		self.container.add_widget(self.status_lbl)
		self.container.add_widget(self.new_game_btn)
		self.container.add_widget(self.exit_btn)
		self.content = self.container

	def new_game_callback(self, *args):
		self.on_new_game()
		self.dismiss()

	def update_status(self, value):
		self.status_lbl.text = value

class _2048Game(BoxLayout):
	def __init__(self, **kwargs):
		super(_2048Game, self).__init__(**kwargs)
		self.main_game_processor = _2048MainGame()  # main processor
		self.main_game = self.ids['_main_game']  # main game box (include 16 buttons)
		for count in range(16):
			self.main_game.add_widget(_2048Button())
		self.all_game_button = self.main_game.children[::-1]  # copy a reverse list
		self.up_btn = self.ids['_up']
		self.down_btn = self.ids['_down']
		self.left_btn = self.ids['_left']
		self.right_btn = self.ids['_right']
		self.undo_btn = self.ids['_undo_btn']
		self.score_lbl = self.ids['_score_lbl']
		self.timer = self.ids['_timer']
		self.end_popup = EndGamePopup(size_hint=(.8, .8), on_new_game=self.newGame)
		self.win_popup = WinGamePopup(size_hint=(.8, .4), on_new_game=self.newGame, on_continue=self.continueGame)
		self.all_color = self.generateAllColor()  # generate color for display background
		self.play_game = False
		self.continue_play_after_win_game = False
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			#  If it exists, this widget is a VKeyboard object which you can use
			#  to change the keyboard layout.
			pass
		self._keyboard.bind(on_key_down=self._on_keyboard_down)

	def generateAllColor(self):
		all_color = []
		for i in range(1, 15):
			red = 50.0 * 500 * i % 255 / 255
			green = 50.0 * 200 * i % 255 / 255
			blue = 50.0 * 100 * i % 255 / 255
			alpha = 150
			all_color.append([pow(2, i), [red, green, blue, alpha]])  # ex: [(2, (1, 1, 1)), (4, (1, 2, 1) .... (2048, (1, 2, 2)))]
		return all_color

	def drawBoard(self):
		i = -1
		for row in self.main_game_processor.game_array:
			for num in row:
				i += 1
				color = (.7, .7, .7, 1)  # default color for 0
				if num == 0:  # dont draw 0
					self.all_game_button[i].text = ''
					self.all_game_button[i].changeBackground(color)
					continue
				for color_temp in self.all_color:  # get color from generated list
					if num == color_temp[0]:
						color = color_temp[1]
				template = '[color=ffffff][b]%s[/b][/color]'  # template to display 
				self.all_game_button[i].text = template % (num)
				self.all_game_button[i].changeBackground(color)
				if (i % 4, i / 4) in self.main_game_processor.generate_array:  # only animate new number
					self.main_game_processor.generate_array.remove((i % 4, i / 4))
					self.all_game_button[i].doAnimation()
		self.undo_btn.text = '[color=ffff00]Undo : [b]%s[/b][/color]' % self.main_game_processor.undo_left
		self.score_lbl.text = str(self.main_game_processor.score)

	def checkForWin(self):
		if not self.continue_play_after_win_game:
			if self.main_game_processor.checkForWin():
				self.play_game = False  # pause game
				self.continue_play_after_win_game = True
				self.timer.unscheduleTimer()
				self.win_popup.open()

	def up(self):
		if self.play_game:
			self.main_game_processor.up()
			if self.main_game_processor.endGame:
				self.endGame()
			self.drawBoard()
			self.checkForWin()

	def down(self):
		if self.play_game:
			self.main_game_processor.down()
			if self.main_game_processor.endGame:
				self.endGame()
			self.drawBoard()
			self.checkForWin()

	def left(self):
		if self.play_game:
			self.main_game_processor.left()
			if self.main_game_processor.endGame:
				self.endGame()
			self.drawBoard()
			self.checkForWin()

	def right(self):
		if self.play_game:
			self.main_game_processor.right()
			if self.main_game_processor.endGame:
				self.endGame()
			self.drawBoard()
			self.checkForWin()

	def undo(self):
		if self.play_game:
			self.main_game_processor.undo()
			self.drawBoard()

	def continueGame(self, *args):
		self.play_game = True
		self.timer.scheduleTimer()

	def newGame(self, *args):
		self.play_game = True
		self.continue_play_after_win_game = False
		self.timer.resetTimer()
		self.timer.unscheduleTimer()
		self.timer.scheduleTimer()
		self.main_game_processor.initGame()
		self.drawBoard()

	def endGame(self):
		self.play_game = False
		self.timer.unscheduleTimer()
		self.end_popup.update_status("You Lost\nYour Score: %s" % self.main_game_processor.score)
		self.end_popup.open()

	def _keyboard_closed(self):
		print('My keyboard have been closed!')
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		# Keycode is composed of an integer + a string
		# If we hit escape, release the keyboard
		if keycode[1] == 'escape':
			keyboard.release()
			return True
		elif keycode[1] in ('up', 'w'):
			self.up()
			return True
		elif keycode[1] in ('down', 's'):
			self.down()
			return True
		elif keycode[1] in ('left', 'a'):
			self.left()
			return True
		elif keycode[1] in ('right', 'd'):
			self.right()
			return True
		# Return True to accept the key. Otherwise, it will be used by
		# the system.
		return False

class _2048App(App):
	def build(self):
		Window.size = (320, 480)
		game = _2048Game()
		return game
if __name__ == '__main__':
	_2048App().run()
