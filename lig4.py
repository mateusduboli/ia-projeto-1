from compiler.ast import List
class Square:
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
		return str(self.value)
	def __repr__(self):
		return str(self)
	
	def __ne__(self, b):
		if(self.value != b):
			return True
		else :
			return False
		
	def __eq__(self, b):
		if(self.value == b):
			return True
		else:
			return False
		
class Game:
	def __init__(self):
		self.matrix = [[0] * 7 for i in range(7)]
		for i in range(7):
			for j in range(7):
				self.matrix[i][j] = Square()
		
	def get(self, i, j):
		return self.matrix[i][j]
	
	def print_matrix(self):
		for row in self.matrix:
			print row
	
	def drop_disc_human(self, i):
		k = 6
		while (k != -1) and (self.matrix[k][i] != 0):
			k = k - 1
			print k
		if(k != -1):
			self.matrix[k][i].mark_human()
			return k, i
		else :
			return -1, -1
