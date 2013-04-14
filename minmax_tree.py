
class MinmaxTreeNode(object):

	def __init__(self, is_max_node):
		self.obj_value = 0
		self.move = -1
		self.alpha = float("-inf")
		self.beta = float("inf")
		self.childs = []
		self.is_leaf = False
		self.is_max_node = is_max_node
		self.value = -1

	def add(self, child):
		self.childs.append(child)

	def cut(self, child):
		self.childs.remove(child)

	def is_max(self):
		return self.is_max_node

	def __str__(self):
		my_str = "{ "
		my_str = my_str + " \"t\" : \"" + ("MAX " if self.is_max_node else "MIN") + "\", "
		my_str = my_str + " \"v\" : \"" + str(self.value) + "\", "
		my_str = my_str + " \"a\" : \"" + str(self.alpha) + "\", "
		my_str = my_str + " \"b\" : \"" + str(self.beta) + "\", "
		my_str = my_str + " \"o\" : \"" + str(self.obj_value) + "\""
		if(not self.is_leaf):
			my_str = my_str + ", \"childs\" : [ "
			for child in self.childs:
				my_str = my_str + ", " + str(child)
			my_str = my_str + " ]"
		my_str = my_str + " }"
		return my_str

class MinmaxTree(object):
	
	def __init__(self, obj_func, depth):
		self.root = MinmaxTreeNode(True)
		self.depth = depth	
		self.obj_func = obj_func

	def build(self, game, root, depth):
		if depth >= self.depth:
			root.is_leaf = True
			root.obj_value = self.obj_func(game)
			return root
		root.state = game
		for i in range(0, 7):
			new_node = MinmaxTreeNode(not root.is_max())
			new_node.value = i
			new_node.state = game.copy()
			x, y = new_node.state.drop_disc(i)
			if not ((x, y) == (-1, -1)):
				new_node.state.check_victory(x, y)
				if new_node.state.has_ended():
					new_node.is_leaf = True
					new_node.obj_value = self.obj_func(game)
				else :
					root.add(self.build(new_node.state, new_node, depth + 1))
				if new_node.is_max():
					root.alpha = min(root.alpha, new_node.value) 
				else :
					root.beta = max(root.beta, new_node.obj_value)
			else:
				return root
		return root
	
	def calculate(self):
		self.root.obj_value = self.__calculate(self.root, self.depth)
		
	def __calculate(self, node, depth):
		if(depth <= 0 or node.is_leaf):
			node.obj_value = self.obj_func(node.state)
			return node.obj_value
		else :
			alpha = node.alpha
			for c in node.childs:
				if(-self.__calculate(c, depth - 1) >= alpha):
					node.value = c.value
					node.obj_value = c.obj_value
		return alpha

	def __str__(self):
		return str(self.root)

	def __repr__(self):
		return str(self)
