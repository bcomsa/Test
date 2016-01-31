from __future__ import print_function
import random, copy

class _2048MainGame:
	def initGame(self):
		self.score = 0
		self.undo_left = 2
		self.undo_game_array = []
		self.game_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.endGame = False
		self.generate_array = []  # list of new number is generated
		for i in range(2):
			self.generateNumber()  # generate 2 new numbers

	def checkExists(self, x, y):
		return self.game_array[y][x] != 0

	def generateNumber(self):
		while True:  # loop until the position is valid
			x = random.randint(0, 3)
			y = random.randint(0, 3)
			if not self.checkExists(x, y):
				number = 2
				if random.randint(1, 100) > 80:
					number = 4
				self.game_array[y][x] = number
				break
		self.generate_array.append((x, y))

	def slideUp(self, game_board=None):
		'''
		2 2 2 2
		0 0 0 0
		2 2 0 2
		0 0 1 1

		to

		2 2 2 2
		2 2 1 2
		0 0 0 1
		0 0 0 0
		'''
		if not game_board:  # because the method cannot pass "self" in parameter so making the default value by if statement
			game_board = self.game_array
		moved = False  # to check if it slides or not
		for x in range(len(game_board[0])):
			for y in range(len(game_board)):
				if game_board[y][x] == 0:  # ignore the blank value
					continue
				for stop_y in range(y - 1, -1, -1):  # find the postion have value and stop
					if game_board[stop_y][x] != 0:  # if exists, change position of current value and stop_y + 1
						game_board[stop_y + 1][x], game_board[y][x] = game_board[y][x], game_board[stop_y + 1][x]
						if y != stop_y + 1:  # check for moved (the stop_y + 1 and current position must different)
							moved = True
						break
					if stop_y == 0 and game_board[0][x] == 0 and game_board[y][x] != game_board[0][x]:
						game_board[0][x], game_board[y][x] = game_board[y][x], game_board[0][x]
						moved = True  # value 0 move to 0 is not moved
									  # 0 0 0 0   o 0 0 0  2 2 2 2
									  # 0 0 0 0   2 2 2 2  o 0 0 0
									  # o 0 0 0   0 0 0 0  0 0 0 0
									  # 2 2 2 2   0 0 0 0  0 0 0 0
									  # o -> 0 is not move
		return moved

	def combineUp(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		score = False
		for x in range(len(game_board[0])):
			if game_board[0][x] == game_board[1][x] != 0:        # 2 2 2 2      4 4 4 4
				if game_board[2][x] == game_board[3][x] != 0:    # 2 2 2 2  to  8 8 8 8
					game_board[0][x] = game_board[0][x] * 2      # 4 4 4 4      0 0 0 0
					game_board[1][x] = game_board[3][x] * 2      # 4 4 4 4      0 0 0 0
					game_board[2][x] = game_board[3][x] = 0
					score = game_board[0][x] + game_board[1][x]
					continue
			if game_board[0][x] == game_board[1][x] != 0:        # 2 2 2 2      4 4 4 4
				game_board[0][x] *= 2                            # 2 2 2 2  to  0 0 0 0
				game_board[1][x] = 0                             # 0 0 0 0      0 0 0 0
				score = game_board[0][x]                         # 0 0 0 0      0 0 0 0
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

	def checkForWin(self):
		return 2048 in [self.game_array[y][x] for y in range(len(self.game_array)) for x in range(len(self.game_array[0]))]

	def up(self):
		'''
		2 2 2 2       2 2 2 2       4 4 4 4       4 4 4 4
		0 0 2 2  (1)  2 2 2 2  (2)  0 0 0 0  (3)  4 2 2 4
		2 2 2 2       4 2 2 2       4 2 2 4       0 0 4 0
		4 2 4 2       0 0 4 2       0 0 4 0       0 0 0 0
		'''
		tmp_game_array = copy.deepcopy(self.game_array)  # array for undo
		tmp_score = self.score  # score for undo
		moved = self.slideUp()  # (1)
		score = self.combineUp()  # (2)
		self.slideUp()  # (3)
		moved = moved or score  # if have moved or combined ~ have moved
		self.score += score
		if not self.existsMove() and self.undo_left == 0:
			self.endGame = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()

	def down(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideDown()
		score = self.combineDown()
		self.slideDown()
		moved = moved or score
		self.score += score
		if not self.existsMove() and self.undo_left == 0:
			self.endGame = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()

	def left(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideLeft()
		score = self.combineLeft()
		self.slideLeft()
		moved = moved or score
		self.score += score
		if not self.existsMove() and self.undo_left == 0:
			self.endGame = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()

	def right(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved = self.slideRight()
		score = self.combineRight()
		self.slideRight()
		moved = moved or score
		self.score += score
		if not self.existsMove() and self.undo_left == 0:
			self.endGame = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()

	def existsMove(self):
		game_array_clone = copy.deepcopy(self.game_array)  # clone the game array to check
		exists = False
		if self.slideUp(game_array_clone) or self.combineUp(game_array_clone) or self.slideDown(game_array_clone) or self.combineDown(game_array_clone) or \
			self.slideLeft(game_array_clone) or self.combineLeft(game_array_clone) or self.slideRight(game_array_clone) or self.combineRight(game_array_clone):
			exists = True
		return exists

	def undo(self):
		if self.undo_left == 0 or len(self.undo_game_array) == 0:  # if start game or out of undo left, not do undo
			return
		self.undo_left -= 1
		temp_array, temp_score = self.undo_game_array.pop()  # pop the undo data (array and score)
		for y in range(len(temp_array)):         # dont do this : self.game_array = temp.array
			for x in range(len(temp_array[0])):  # because it reference to new list, not a current list, it wont work
				self.game_array[y][x] = temp_array[y][x]
		self.score = temp_score

if __name__ == '__main__':  # command line game test
	from getch import getch  # getch code from internet
	from colorama import init, Fore, Back, Style  # to draw color in command line
	import sys, os
	init(autoreset=True)
	game = _2048MainGame()
	game.initGame()
	blank = ' ' * 25
	help = "ESC : Quit Game\nr : Reset\tu : Undo\na : Left \td : Right\nw : Up   \ts : Down".split('\n')
	all_color = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
	all_number = [pow(2, i) for i in range(1, 15)]

	def numFormat(num):
		if num == 0:
			return '    .'
		return all_color[all_number.index(num) % len(all_color)] + "%5s" % num

	def clearScreen():
		if 'win' in sys.platform:
			os.system('cls')
		else:
			os.system('clear')

	def drawInfo(game):
		print(Back.CYAN + blank)
		score_str = "Your Score: " + str(game.score)
		undo_str = "Undo Left: " + str(game.undo_left)
		print(Back.CYAN + " " + Back.BLUE + "     " + score_str + " " * (23 - len(score_str) - 5) + Back.CYAN + " ")
		print(Back.CYAN + " " + Back.BLUE + "     " + undo_str + " " * (23 - len(undo_str) - 5) + Back.CYAN + " ")
		print(Back.CYAN + blank)

	def drawWinGame(game):
		board = game.game_array
		clearScreen()
		drawInfo(game)
		print(Back.YELLOW + blank)
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		for y in range(len(board)):
			if y == 1:
				print(Back.YELLOW + " " + Back.RESET + " " * 8 + "YOU WIN" + " " * 8 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			elif y == 2:
				print(Back.YELLOW + " " + Back.RESET + " " * 6 + "(C)ONTINUE" + " " * 7 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			elif y == 3:
				print(Back.YELLOW + " " + Back.RESET + " " * 8 + "(R)ESET" + " " * 8 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			else:
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + blank)

	def drawLostGame(game):
		board = game.game_array
		clearScreen()
		drawInfo(game)
		print(Back.YELLOW + blank)
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		for y in range(len(board)):
			if y == 1:
				print(Back.YELLOW + " " + Back.RESET + " " * 8 + "YOU LOST" + " " * 7 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			elif y == 2:
				print(Back.YELLOW + " " + Back.RESET + " " * 8 + "(R)ESET" + " " * 8 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			elif y == 3:
				print(Back.YELLOW + " " + Back.RESET + " " * 8 + "(Q)UIT" + " " * 9 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			else:
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
				print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + blank)

	def drawBoard(game):
		board = game.game_array
		clearScreen()
		drawInfo(game)
		print(Back.YELLOW + blank)
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		for y in range(len(board)):
			print(Back.YELLOW + " ", end="")
			for x in range(len(board[0])):
				print(Back.RESET + numFormat(board[y][x]), end='')
			print(Back.RESET + "   " + Back.YELLOW + " " + Back.RESET + "\t" + Fore.RED + help[y])
			print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
			print(Back.YELLOW + " " + Back.RESET + " " * 23 + Back.YELLOW + " ")
		print(Back.YELLOW + blank)
	
	continue_play_after_win_game = False
	
	while True:
		if game.checkForWin() and not continue_play_after_win_game:
			drawWinGame(game)
			key = getch().lower()
			if key == 'c':
				continue_play_after_win_game = True
			if key == 'r':
				continue_play_after_win_game = False
				game.initGame()
			if ord(key) == 27:  # ESC
				sys.exit(0)
			continue
		elif game.endGame:
			drawLostGame(game)
		else:
			drawBoard(game)
		key = getch().lower()
		if ord(key) == 27 or key == 'q':  # ESC
			sys.exit(0)
		if key == 'a':
			game.left()
		if key == 'd':
			game.right()
		if key == 'w':
			game.up()
		if key == 's':
			game.down()
		if key == 'r':
			continue_play_after_win_game = False
			game.initGame()
		if key == 'u':
			game.undo()
