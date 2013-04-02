import random

class Square(object):
	def __init__(self):
		self.NONE = 0
		self.COMPUTER = 1
		self.HUMAN = 2
		self.value = self.NONE
	
	def mark_human(self):
		self.value = self.HUMAN
	
	def mark_computer(self):
		self.value = self.COMPUTER

	def __str__(self):
		if(self.value == self.HUMAN):
			return "HUMAN"
		elif(self.value == self.COMPUTER):
			return "COMPUTER"
		else :
			return "NONE"
		
	def __repr__(self):
		return str(self)
	
	def __ne__(self, b):
		if(self.value != b):
			return True
		else :
			return False
		
	def __eq__(self, b):
		if(type(b) is Square):
			return self.value == b.value
		if(self.value == b):
			return True
		else:
			return False
		
class Game(object):
	def __init__(self, oponent):
		self.ended = False
		self.oponent = oponent
		self.height = 7
		self.width = 7
		self.matrix = [[0] * self.width for i in range(self.height)]
		for i in range(self.width):
			for j in range(self.height):
				self.matrix[i][j] = Square()
		
	
	def end_game(self):
		self.ended = True
	
	def has_ended(self):
		return self.ended
	
	def __drop_disc(self, i, isHuman):
		k = 6
		
		while (k != -1) and (self.matrix[k][i] != 0):
			k = k - 1
		if(k != -1):
			if(isHuman):
				self.matrix[k][i].mark_human()
			else:
				self.matrix[k][i].mark_computer()
		else :
			k, i = -1, -1
		return k, i

	def get(self, i, j):
		return self.matrix[i][j]
	
	def print_matrix(self):
		for row in self.matrix:
			print row	

	def drop_disc_human(self, i):
		return self.__drop_disc(i, True)
	
	def drop_disc_computer(self):
		i = self.oponent.make_next_move(self)
		return self.__drop_disc(i, False)
	
	def check_victory(self, x, y):
		lack = 4 # Lack for victory
		new_disc = self.get(x, y)
		for i in range(-1, 2):
			for k in range(-1, 2):
				lack = 4
				current_disc = new_disc
				_x, _y = x, y
				while (new_disc == current_disc) and lack > 0:
					lack = lack - 1
					_x, _y = _x + i, _y + k
					if (0 <= _x <= 6) and (0 <= _y <= 6) and not(_x == x and _y == y):
						current_disc = self.get(_x, _y)
						print current_disc, _x, _y
					else:
						break
				if lack == 0:
					return True
		return False
