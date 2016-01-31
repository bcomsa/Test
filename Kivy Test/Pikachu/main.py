# Pikachu
import random
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle
class GameButton(ToggleButton):
	def on_state(self, *args):
		self.parent.selected.append(self.game_xy)

class Game(GridLayout):
	selected = ListProperty([])

	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		self.game_array = self.makeGameArray()
		self.addGameButton()

	def makeGameArray(self):
		array = []
		for i in range(1, self.rows * self.cols / 2 + 1):
			color = (random.random(), random.random(), random.random())
			button_temp = self.makeButton(color=color, text=str(i))
			button_temp = GameButton(text=str(i))
			array.append([1, button_temp])
			button_temp_2 = self.makeButton(color=color, text=str(i))
			button_temp_2 = GameButton(text=str(i))
			array.append([1, button_temp_2])
		random.shuffle(array)
		return self.chunks(array, self.cols)

	def makeButton(self, color=(1, 1, 1), text=''):
		temp = GameButton(text=text)
		temp.canvas.add(Color(rgb=color))
		temp.bind(size=self.bindBackgroundButton)
		return temp

	def bindBackgroundButton(self, *args):
		temp = args[0]
		with temp.canvas:
			Rectangle(pos=temp.pos, size=temp.size)

	def addGameButton(self):
		for row in range(len(self.game_array)):
			for col in range(len(self.game_array[0])):
				button = self.game_array[row][col][1]
				button.game_xy = (col, row)
				self.add_widget(button)

	def chunks(self, l, n):
		return [l[i:i + n] for i in range(0, len(l), n)]

	def checkLineX(self, x, X, y):
		if x == X:
			return False
		for offset in range(min(x, X) + 1, max(x, X) + 1):
			if self.game_array[y][offset][0] == 1:
				print 'False X'
				return False
		return True

	def checkLineY(self, y, Y, x):
		if y == Y:
			return False
		for offset in range(min(y, Y) + 1, max(y, Y) + 1):
			if self.game_array[offset][x][0] == 1:
				print 'False Y'
				return False
		return True

	def checkBox(self, x, y, X, Y):
		minY = min(y, Y)
		maxY = max(y, Y)
		minX = x if y == minY else X
		maxX = x if y == maxY else X
		for offset in range(minY, maxY):
			if self.checkLineY(minY, offset, minX):
				print str(minY) + ' ok11 ' + str(offset)
				if self.checkLineX(minX, maxX, offset):
					print str(minY) + ' ok12 ' + str(offset)
					if self.checkLineY(offset, maxY, maxX):
						print str(minY) + ' ok13 ' + str(offset) + ' ok13 ' + str(maxX)
						return True
		return False

	def checkValid(self, x, y, X, Y):
		#if self.game_array[y][x][1].text != self.game_array[Y][X][1].text:
		#	return False
		if abs(x - X) == 1 or abs(y - Y) == 1:
			return True
		if x == X:
			return self.checkLineY(y, Y, x)
		elif y == Y:
			return self.checkLineX(x, X, y)
		else:
			return self.checkBox(x, y, X, Y)
		return False

	def on_selected(self, *args):
		if len(self.selected) > 1:
			first_x, first_y = self.selected[0]
			last_x, last_y = self.selected[1]
			del self.selected[:]
			firstObj = self.game_array[first_y][first_x]
			lastObj = self.game_array[last_y][last_x]
			firstObj[1].state = 'normal'
			lastObj[1].state = 'normal'
			if self.checkValid(first_x, first_y, last_x, last_y):
				with firstObj[1].canvas:
					Color(rgb=(0, 0, 0))
					Rectangle(pos=firstObj[1].pos, size=firstObj[1].size)
				with lastObj[1].canvas:
					Color(rgb=(0, 0, 0))
					Rectangle(pos=lastObj[1].pos, size=lastObj[1].size)
				firstObj[1].disabled = True
				lastObj[1].disabled = True
				firstObj[0] = 0
				lastObj[0] = 0
		if self.winGame():
			self.clear_widgets()

	def winGame(self):
		for row in self.game_array:
			for obj in row:
				if obj[0] != 0:
					return False
		return True
class PikachuApp(App):
	def build(self):
		return Game(rows=5, cols=10, padding=50)

if __name__ == '__main__':
	PikachuApp().run()
