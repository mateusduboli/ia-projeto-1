
class MinmaxTreeNode(object):

	def __init__(self, is_max_node):
		self.obj_value = 0
		self.move = -1
		self.alfa = float("-inf")
		self.beta = float("inf")
		self.childs = []
		self.is_leaf = True
		self.is_max_node = is_max_node

	def add(self, child):
		self.is_leaf = False
		self.childs.append(child)

	def cut(self, child):
		self.childs.remove(child)

	def is_max(self):
		return self.is_max_node

	def __str__(self):
		my_str = "[ "
		my_str = my_str + ("MAX " if self.is_max_node else "MIN")
		my_str = my_str + " v = " + str(self.value)
		my_str = my_str + " a = " + str(self.alfa)
		my_str = my_str + " b = " + str(self.beta)
		if(len(self.childs) != 0):
			for child in childs:
				my_str = mystr + ", " + str(child)
		my_str = my_str + " ]"
		return my_str

class MinmaxTree(object):
	
	def __init__(self, obj_func):
		self.root = MinmaxTreeNode(True)
		self.depth = 0	
		self.obj_func = obj_func

	def build(self):
		i = 0
		self.root.value = self.obj_func(i)
	
	def __str__(self):
		return str(self.root)

	def __repr__(self):
		return str(self)
