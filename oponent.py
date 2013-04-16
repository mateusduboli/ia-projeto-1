from minmax_tree import MinmaxTree
from lig4 import Square

class Oponent( object ):

	def __init__(self):
		self.tree = MinmaxTree( self.objective_func, 6)
		
	def make_move( self, game ):
		self.tree.build( game )
		return self.tree.move

	def objective_func( self, game ):
		return game.get_value() 
