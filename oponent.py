from minmax_tree import MinmaxTree
from lig4 import Square

class Oponent(object):

	def make_move(self, game):
		tree = MinmaxTree( self.objective_func, 4 )
		tree.build(game)
		return tree.root.value

	def objective_func(self, game):
		return game.value if game.winner == Square.COMPUTER else -game.value
