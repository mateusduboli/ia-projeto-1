from minmax_tree import MinmaxTree, MinmaxTreeNode
from random import randint

class Oponent(object):

	def make_next_move(self, game):
		tree = MinmaxTree(self.objective_func)
		tree.build()
		i = tree.root.value
		return i
		
	
	def objective_func(self, i):
		return randint(0, 6)
