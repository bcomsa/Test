import random, copy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_string('''
<_2048Button>:
	markup: True
<_2048Game>:
	orientation: 'vertical'
	BoxLayout:
		size_hint: 1, .2
		Button:
			markup: True
			text: '[color=ffff00]Reset[/color]'
			on_release: root.initGame()
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
	Widget:
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
	pass

class _2048Game(BoxLayout):
	def __init__(self, **kwargs):
		super(_2048Game, self).__init__(**kwargs)
		self.main_game = self.ids['_main_game']
		for count in range(16):
			self.main_game.add_widget(_2048Button())
		self.up_btn = self.ids['_up']
		self.down_btn = self.ids['_down']
		self.left_btn = self.ids['_left']
		self.right_btn = self.ids['_right']
		self.undo_btn = self.ids['_undo_btn']
		self.score_lbl = self.ids['_score_lbl']
		self.initGame()
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			#  If it exists, this widget is a VKeyboard object which you can use
			#  to change the keyboard layout.
			pass
		self._keyboard.bind(on_key_down=self._on_keyboard_down)

	def initGame(self):
		self.score = 0
		self.undo_left = 2
		self.undo_game_array = []
		self.all_game_button = self.main_game.children[::-1]
		self.game_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		for i in range(2):
			self.generateNumber()
		self.drawBoard()

	def drawBoard(self):
		i = -1
		for row in self.game_array:
			for num in row:
				i += 1
				if num == 0:
					self.all_game_button[i].text = ''
					continue
				template = '[color=ff0000]%s[/color]'
				if num == 2:
					template = '[color=ff0000]%s[/color]'
				if num == 4:
					template = '[color=00ff00]%s[/color]'
				if num == 8:
					template = '[color=0000ff]%s[/color]'
				if num == 16:
					template = '[color=ffff00]%s[/color]'
				if num == 32:
					template = '[color=ff00ff]%s[/color]'
				if num == 64:
					template = '[color=00ffff]%s[/color]'
				if num == 128:
					template = '[color=fff000]%s[/color]'
				if num == 256:
					template = '[color=0fff00]%s[/color]'
				if num == 512:
					template = '[color=00fff0]%s[/color]'
				if num == 1024:
					template = '[color=000fff]%s[/color]'
				if num == 2048:
					template = '[color=f0000f]%s[/color]'
				self.all_game_button[i].text = template % (num)
		self.score_lbl.text = str(self.score)

	def checkExists(self, x, y):
		return self.game_array[y][x] != 0

	def generateNumber(self):
		while True:
			x = random.randint(0, 3)
			y = random.randint(0, 3)
			if not self.checkExists(x, y):
				number = 2
				if random.randint(1, 100) > 80:
					number = 4
				self.game_array[y][x] = number
				break
		self.drawBoard()

	def checkFull(self):
		return False not in [self.game_array[y][x] > 0 for y in range(len(self.game_array)) for x in range(len(self.game_array))]

	def slideUp(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		for x in range(len(game_board[0])):
			for y in range(len(game_board[0])):
				if game_board[y][x] == 0:
					continue
				for stop_y in range(y - 1, -1, -1):
					if game_board[stop_y][x] != 0:
						game_board[stop_y + 1][x], game_board[y][x] = game_board[y][x], game_board[stop_y + 1][x]
						if y != stop_y + 1:
							moved = True
						break
					if stop_y == 0 and game_board[0][x] == 0 and game_board[y][x] != game_board[0][x]:
						game_board[0][x], game_board[y][x] = game_board[y][x], game_board[0][x]
						moved = True
		return moved

	def combineUp(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		score = False
		for x in range(len(game_board[0])):
			if game_board[0][x] == game_board[1][x] != 0:
				if game_board[2][x] == game_board[3][x] != 0:
					game_board[0][x] = game_board[0][x] * 2
					game_board[1][x] = game_board[3][x] * 2
					game_board[2][x] = game_board[3][x] = 0
					score = game_board[0][x] + game_board[1][x]
					continue
			if game_board[0][x] == game_board[1][x] != 0:
				game_board[0][x] *= 2
				game_board[1][x] = 0
				score = game_board[0][x]
				continue
			if game_board[1][x] == game_board[2][x] != 0:
				game_board[1][x] *= 2
				game_board[2][x] = 0
				score = game_board[1][x]
				continue
			if game_board[2][x] == game_board[3][x] != 0:
				game_board[2][x] *= 2
				game_board[3][x] = 0
				score = game_board[2][x]
				continue
		return score

	def slideDown(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		for x in range(len(game_board[0])):
			for y in range(len(game_board[0]) - 1, -1, -1):
				if game_board[y][x] == 0:
					continue
				for stop_y in range(y + 1, 4):
					if game_board[stop_y][x] != 0:
						game_board[stop_y - 1][x], game_board[y][x] = game_board[y][x], game_board[stop_y - 1][x]
						if y != stop_y - 1:
							moved = True
						break
					if stop_y == 3 and game_board[3][x] == 0 and game_board[y][x] != game_board[3][x]:
						game_board[3][x], game_board[y][x] = game_board[y][x], game_board[3][x]
						moved = True
		return moved

	def combineDown(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		score = False
		for x in range(len(game_board[0])):
			if game_board[2][x] == game_board[3][x] != 0:
				if game_board[0][x] == game_board[1][x] != 0:
					game_board[2][x] = game_board[1][x] * 2
					game_board[3][x] = game_board[3][x] * 2
					game_board[0][x] = game_board[1][x] = 0
					score = game_board[2][x] + game_board[3][x]
					continue
			if game_board[2][x] == game_board[3][x] != 0:
				game_board[3][x] *= 2
				game_board[2][x] = 0
				score = game_board[3][x]
				continue
			if game_board[1][x] == game_board[2][x] != 0:
				game_board[2][x] *= 2
				game_board[1][x] = 0
				score = game_board[2][x]
				continue
			if game_board[0][x] == game_board[1][x] != 0:
				game_board[1][x] *= 2
				game_board[0][x] = 0
				score = game_board[1][x]
				continue
		return score

	def slideLeft(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		for y in range(len(game_board)):
			for x in range(len(game_board[0])):
				if game_board[y][x] == 0:
					continue
				for stop_x in range(x - 1, -1, -1):
					if game_board[y][stop_x] != 0:
						game_board[y][stop_x + 1], game_board[y][x] = game_board[y][x], game_board[y][stop_x + 1]
						if x != stop_x + 1:
							moved = True
						break
					if stop_x == 0 and game_board[y][0] == 0 and game_board[y][x] != game_board[y][0]:
						game_board[y][0], game_board[y][x] = game_board[y][x], game_board[y][0]
						moved = True
		return moved

	def combineLeft(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		score = False
		for y in range(len(game_board)):
			if game_board[y][0] == game_board[y][1] != 0:
				if game_board[y][2] == game_board[y][3] != 0:
					game_board[y][0] = game_board[y][0] * 2
					game_board[y][1] = game_board[y][2] * 2
					game_board[y][2] = game_board[y][3] = 0
					score = game_board[y][0] + game_board[y][1]
					continue
			if game_board[y][0] == game_board[y][1] != 0:
				game_board[y][0] *= 2
				game_board[y][1] = 0
				score = game_board[y][0]
				continue
			if game_board[y][1] == game_board[y][2] != 0:
				game_board[y][1] *= 2
				game_board[y][2] = 0
				score = game_board[y][1]
				continue
			if game_board[y][2] == game_board[y][3] != 0:
				game_board[y][2] *= 2
				game_board[y][3] = 0
				score = game_board[y][2]
				continue
		return score

	def slideRight(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		for y in range(len(game_board)):
			for x in range(len(game_board[0]) - 1, -1, -1):
				if game_board[y][x] == 0:
					continue
				for stop_x in range(x + 1, 4):
					if game_board[y][stop_x] != 0:
						game_board[y][stop_x - 1], game_board[y][x] = game_board[y][x], game_board[y][stop_x - 1]
						if x != stop_x - 1:
							moved = True
						break
					if stop_x == 3 and game_board[y][3] == 0 and game_board[y][x] != game_board[y][3]:
						game_board[y][3], game_board[y][x] = game_board[y][x], game_board[y][3]
						moved = True
		return moved

	def combineRight(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		score = False
		for y in range(len(game_board)):
			if game_board[y][2] == game_board[y][3] != 0:
				if game_board[y][0] == game_board[y][1] != 0:
					game_board[y][2] = game_board[y][1] * 2
					game_board[y][3] = game_board[y][3] * 2
					game_board[y][0] = game_board[y][1] = 0
					score = game_board[y][2] + game_board[y][3]
					continue
			if game_board[y][2] == game_board[y][3] != 0:
				game_board[y][3] *= 2
				game_board[y][2] = 0
				score = game_board[y][3]
				continue
			if game_board[y][1] == game_board[y][2] != 0:
				game_board[y][2] *= 2
				game_board[y][1] = 0
				score = game_board[y][2]
				continue
			if game_board[y][0] == game_board[y][1] != 0:
				game_board[y][1] *= 2
				game_board[y][0] = 0
				score = game_board[y][1]
				continue
		return score

	def up(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideUp()
		score = self.combineUp()
		self.slideUp()
		moved = moved or score
		self.score += score
		if self.checkFull() and not self.existsMove():
			self.initGame()
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		self.drawBoard()

	def down(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideDown()
		score = self.combineDown()
		self.slideDown()
		moved = moved or score
		self.score += score
		if self.checkFull() and not self.existsMove():
			self.initGame()
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		self.drawBoard()

	def left(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideLeft()
		score = self.combineLeft()
		self.slideLeft()
		moved = moved or score
		self.score += score
		if self.checkFull() and not self.existsMove():
			self.initGame()
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		self.drawBoard()

	def right(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideRight()
		score = self.combineRight()
		self.slideRight()
		moved = moved or score
		self.score += score
		if self.checkFull() and not self.existsMove():
			self.initGame()
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		self.drawBoard()

	def existsMove(self):
		game_array_clone = copy.deepcopy(self.game_array)
		exists = False
		if self.slideUp(game_array_clone) or self.combineUp(game_array_clone) or self.slideDown(game_array_clone) or self.combineDown(game_array_clone) or \
			self.slideLeft(game_array_clone) or self.combineLeft(game_array_clone) or self.slideRight(game_array_clone) or self.combineRight(game_array_clone):
			exists = True
		return exists

	def undo(self):
		if self.undo_left == 0 or len(self.undo_game_array) == 0:
			return
		self.undo_left -= 1
		temp_array, temp_score = self.undo_game_array.pop()
		for y in range(len(temp_array)):
			for x in range(len(temp_array[0])):
				self.game_array[y][x] = temp_array[y][x]
		self.score = temp_score
		self.drawBoard()
		self.undo_btn.text = '[color=ffff00]Undo : %s[/color]' % self.undo_left

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
		elif keycode[1] == 'up':
			self.up()
			return True
		elif keycode[1] == 'down':
			self.down()
			return True
		elif keycode[1] == 'left':
			self.left()
			return True
		elif keycode[1] == 'right':
			self.right()
			return True
		# Return True to accept the key. Otherwise, it will be used by
		# the system.
		return False

class _2048App(App):
	def build(self):
		Window.size = (320, 480)
		return _2048Game()
if __name__ == '__main__':
	_2048App().run()
