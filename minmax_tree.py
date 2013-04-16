from random import shuffle
class MinmaxTreeNode( object ):

	def __init__( self, is_max_node ):
		if is_max_node:
			self.obj_value = float( "-inf" )
		else:
			self.obj_value = float( "inf" )
		self.alpha = float( "-inf" )
		self.beta = float( "inf" )
		self.childs = []
		self.is_leaf = False
		self.is_max_node = is_max_node
		self.state = None
		self.value = -1

	def add( self, child ):
		self.childs.append( child )

	def cut( self, child ):
		self.childs.remove( child )

	def is_max( self ):
		return self.is_max_node

	def __getitem__( self, i ):
		return self.childs[i]

	def __str__( self ):
		my_str = "{ "
		my_str = my_str + " \"t\" : \"" + ( "MAX " if self.is_max_node else "MIN" ) + "\", "
		my_str = my_str + " \"v\" : \"" + str( self.value ) + "\", "
		my_str = my_str + " \"a\" : \"" + str( self.alpha ) + "\", "
		my_str = my_str + " \"b\" : \"" + str( self.beta ) + "\", "
		my_str = my_str + " \"o\" : \"" + str( self.obj_value ) + "\""
		if( not self.is_leaf ):
			my_str = my_str + ", \"childs\" : [ "
			for child in self.childs:
				my_str = my_str + ", " + str( child )
			my_str = my_str + " ]"
		my_str = my_str + " }"
		return my_str

class MinmaxTree( object ):

	def __init__( self, obj_func, depth ):
		self.root = MinmaxTreeNode( True )
		self.depth = depth
		self.obj_func = obj_func

	def build( self, game ):
		self.root = self.__rec_build( game, self.root, 0 )


	def __rec_build( self, game, root, depth ):
		if depth >= self.depth or game.has_ended():
			root.is_leaf = True
			root.obj_value = self.obj_func( game )
			return root
		root.state = game
		temp_obj_value = root.obj_value
		order = range( 7 )
		shuffle( order )
		for i in order :
			new_node = MinmaxTreeNode( not root.is_max() )
			new_game = game.copy()
			new_node.value = i
			x, y = new_game.drop_disc( i )
			if not ( ( x, y ) == ( -1, -1 ) ):
				new_node.state = new_game
				root.add( self.__rec_build( new_game, new_node, depth + 1 ) )
				if root.is_max():
					root.alpha = max( root.alpha, new_node.obj_value )
					temp_obj_value = max( root.obj_value, new_node.obj_value )
				else :
					root.beta = min( root.beta, new_node.obj_value )
					temp_obj_value = min( root.obj_value, new_node.obj_value )
				if temp_obj_value <> root.obj_value:
					root.obj_value = temp_obj_value
					root.value = new_node.value
				if root.alpha >= root.beta:
					break
		return root

	def __str__( self ):
		return str( self.root )

	def __repr__( self ):
		return str( self )
