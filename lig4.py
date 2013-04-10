import copy
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
	def __init__(self):
		self.ended = False
		self.human_move = True
		self.height = 7
		self.width = 7
		self.matrix = [[0] * self.width for i in range(self.height)]
		for i in range(self.width):
			for j in range(self.height):
				self.matrix[i][j] = Square()
		
	
	def __end_game(self):
		self.ended = True
	
	def has_ended(self):
		return self.ended
	
	def drop_disc(self, j):
		i = 6		
		while (i != -1) and (self.get(i, j) != 0):
			i = i - 1
		if(i != -1):
			if(self.human_move):
				self.get(i, j).mark_human()
				self.human_move = False
			else:
				self.get(i, j).mark_computer()
				self.human_move = True
		else :
			i, j = -1, -1
		return i, j

	def get(self, i, j):
		if i in range(0, 7) and j in range(0, 7):
			return self.matrix[i][j]
		else:
			return None
	
	def print_matrix(self):
		for row in self.matrix:
			print row	

	def check_victory(self, x, y):
		lack = 4 # Lack for victory
		new_disc = self.get(x, y)
		for i in range(-1, 2):
			for j in range(-1, 1):
				if i == 0 and j == 0:
					continue
				revert = False
				lack = 4
				current_disc = new_disc
				_x, _y, _i, _j = x, y, i, j
				while True:
					if lack == 0:
						self.__end_game()
						return True
					if current_disc <> new_disc :
						if(revert):
							break
						else:
							revert = True
							_x, _y = x, y
							_i, _j = i * -1, j * -1
					else :
						lack = lack - 1
					_x, _y = _x + _i, _y + _j
					current_disc = self.get(_x, _y)
					print current_disc, _x, _y
		return False
	
	def copy(self):
		return copy.deepcopy(self)
