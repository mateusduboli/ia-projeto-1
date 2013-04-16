from minmax_tree import MinmaxTree
from lig4 import Square

class Oponent(object):

	def make_move(self, game):
		tree = MinmaxTree(self.objective_func, 4)
		tree.build(game)
		return tree.root.value

	def objective_func(self, game):
		if(game.has_ended()):
			return 1 if game.winner == Square.COMPUTER else -1
		else:
			return 0