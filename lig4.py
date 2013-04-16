import copy
from array import array

class Square( object ):
	NONE = 0
	COMPUTER = 1
	HUMAN = 2
	HORIZONTAL = ( 0, -1 )
	IHORIZONTAL = ( 0, 1 )
	VERTICAL = ( -1, 0 )
	IVERTICAL = ( 1, 0 )
	MAINDIAG = ( -1, -1 )
	IMAINDIAG = ( 1, 1 )
	OPTDIAG = ( -1, 1 )
	IOPTDIAG = ( 1, -1 )

	def __init__( self ):
		self.mark = Square.NONE
		self.horizontal = [1]
		self.vertical = [1]
		self.maindiag = [1]
		self.optdiag = [1]
		self.value = 4

	def mark_human( self ):
		self.mark = Square.HUMAN

	def mark_computer( self ):
		self.mark = Square.COMPUTER

	def update_value( self, x, y, other ):
		if( other == Square.NONE or other == None ):
			return False
		elif( x, y == Square.HORIZONTAL ):
			self.value = self.value - self.horizontal[0]
			if other == self :
				if other.horizontal[0] >= self.horizontal[0]:
					self.horizontal = other.horizontal
					self.horizontal[0] = self.horizontal[0] + 1
				else:
					other.horizontal = self.horizontal
					self.horizontal[0] = self.horizontal[0] + 1
				self.value = self.value + self.horizontal[0]
			else:
				self.horizontal[0] = 0
				return False
			return True
		elif( x, y == Square.IHORIZONTAL ):
			self.value = self.value - self.horizontal[0]
			if other == self:
				if other.horizontal[0] >= self.horizontal[0]:
					self.horizontal = other.horizontal
					self.horizontal[0] = self.horizontal[0] + 1
				else:
					other.horizontal = self.horizontal
					self.horizontal[0] = self.horizontal[0] + 1
				self.value = self.value + self.horizontal[0]
			else:
				self.horizontal[0] = 0
				return False
			return True
		elif( x, y == Square.VERTICAL ):
			self.value = self.value - self.vertical[0]
			if other == self:
				if other.vertical[0] >= self.vertical[0]:
					self.vertical = other.vertical
					self.vertical[0] = self.vertical[0] + 1
				else:
					other.vertical = self.vertical
					self.vertical[0] = self.vertical[0] + 1
				self.value = self.value + self.vertical[0]
			else:
				self.vertical[0] = 0
				return False
			return True
		elif( x, y == Square.IVERTICAL ):
			self.value = self.value - self.vertical[0]
			if other == self:
				if other.vertical[0] >= self.vertical[0]:
					self.vertical = other.vertical
					self.vertical[0] = self.vertical[0] + 1
				else:
					other.vertical = self.vertical
					self.vertical[0] = self.vertical[0] + 1
				self.value = self.value + self.vertical[0]
			else:
				self.vertical[0] = 0
				return False
			return True
		elif( x, y == Square.MAINDIAG ):
			self.value = self.value - self.maindiag[0]
			if other == self:
				if other.maindiag[0] >= self.maindiag[0]:
					self.maindiag = other.maindiag
					self.maindiag[0] = self.maindiag[0] + 1
				else:
					other.maindiag = self.maindiag
					self.maindiag[0] = self.maindiag[0] + 1
				self.value = self.value + self.maindiag[0]
			else:
				self.maindiag[0] = 0
				return False
			return True
		elif( x, y == Square.IMAINDIAG ):
			self.value = self.value - self.maindiag[0]
			if other == self:
				if other.maindiag[0] >= self.maindiag[0]:
					self.maindiag = other.maindiag
					self.maindiag[0] = self.maindiag[0] + 1
				else:
					other.maindiag = self.maindiag
					self.maindiag[0] = self.maindiag[0] + 1
				self.value = self.value + self.maindiag[0]
			else:
				self.maindiag[0] = 0
				return False
			return True
		elif( x, y == Square.OPTDIAG ):
			self.value = self.value - self.optdiag[0]
			if other == self:
				if other.optdiag[0] >= self.optdiag[0]:
					self.optdiag = other.optdiag
					self.optdiag[0] = self.optdiag[0] + 1
				else:
					other.optdiag = self.optdiag
					self.optdiag[0] = self.optdiag[0] + 1
				self.value = self.value + self.optdiag[0]
			else:
				self.optdiag[0] = 0
				return False
			return True
		elif( x, y == Square.IOPTDIAG ):
			self.value = self.value - self.optdiag[0]
			if other == self :
				if other.optdiag[0] >= self.optdiag[0]:
					self.optdiag = other.optdiag
					self.optdiag[0] = self.optdiag[0] + 1
				else:
					other.optdiag = self.optdiag
					self.optdiag[0] = self.optdiag[0] + 1
				self.value = self.value + self.optdiag[0]
			else:
				self.optdiag[0] = 0
				return False
			return True

	def __str__( self ):
		if( self.mark == Square.HUMAN ):
			return "H"
		elif( self.mark == Square.COMPUTER ):
			return "C"
		else :
			return "N"

	def __repr__( self ):
		return str( self )

	def __ne__( self, b ):
		if( self.mark <> b ):
			return True
		else :
			return False

	def __eq__( self, b ):
		if( type( b ) is Square ):
			return self.mark == b.mark
		if( self.mark == b ):
			return True
		else:
			return False

class Game( object ):
	def __init__( self ):
		self.ended = False
		self.human_move = True
		self.winner = None
		self.height = 7
		self.width = 7
		self.value = 0
		self.matrix = [[0] * self.width for i in range( self.height )]
		for i in range( self.width ):
			for j in range( self.height ):
				self.matrix[i][j] = Square()


	def __end_game( self ):
		self.ended = True
		self.winner = Square.COMPUTER if self.human_move else Square.HUMAN

	def has_ended( self ):
		return self.ended

	def drop_disc( self, j ):
		i = 6
		while ( i <> -1 ) and ( self.get( i, j ) != 0 ):
			i = i - 1
		if( i <> -1 ):
			if( self.human_move ):
				self.get( i, j ).mark_human()
				self.human_move = False
			else:
				self.get( i, j ).mark_computer()
				self.human_move = True
			self.__update_value( i, j )
		else :
			i, j = -1, -1
		return i, j

	def get( self, i, j ):
		if i in range( 0, 7 ) and j in range( 0, 7 ):
			return self.matrix[i][j]
		else:
			return None

	def print_matrix( self ):
		for row in self.matrix:
			print row

	def __update_value( self, x, y ):
		lack = 4 # Lack for victory
		new_disc = self.get( x, y )
		for i in range( -1, 2 ):
			for j in range( -1, 1 ):
				if i == 0 and j == 0:
					continue
				revert = False
				lack = 4
				current_disc = new_disc
				_x, _y, _i, _j = x, y, i, j
				while True:
					if lack == 0:
						self.__end_game()
					updated = new_disc.update_value( _i, _j, current_disc )
					if( not updated ):
						if( revert ):
							break
						else:
							revert = True
							_x, _y = x, y
							_i, _j = i * -1, j * -1
					else :
						lack = lack - 1
					_x, _y = _x + _i, _y + _j
					current_disc = self.get( _x, _y )
		if( self.value < new_disc.value ):
			self.value = new_disc.value
			self.winner = new_disc.mark
		return self.ended

	def copy( self ):
		return copy.deepcopy( self )
