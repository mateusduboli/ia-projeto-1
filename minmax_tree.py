from random import shuffle

class MinmaxTree( object ):

	def __init__( self, obj_func, depth ):
		self.depth = depth
		self.obj_func = obj_func
		self.value = float( "-Inf" )
		self.order = range( 7 )
#		shuffle( self.order )

	def build( self, game ):
		self.value = self.__rec_build( game, 0, True, float( "-Inf" ), float( "Inf" ) )
		print self.value, self.move

	def __rec_build( self, game, depth, is_max, alpha, beta ):
		if depth >= self.depth or game.has_ended():
			obj_value = self.obj_func( game )
			return obj_value
		n_alpha = alpha
		n_beta = beta
		move = -1
		state = game
		if is_max :
			obj_value = float( "-inf" )
		else:
			obj_value = float( "inf" )
		temp_obj_value = obj_value
		for i in self.order :
			new_game = game.copy()
			x, y = new_game.drop_disc( i )
			if not ( ( x, y ) == ( -1, -1 ) ):
				new_state = new_game
				new_obj_value = self.__rec_build( new_game, depth + 1, not is_max, n_alpha, n_beta )
				if is_max:
					n_alpha = max( n_alpha, new_obj_value )
					temp_obj_value = max( obj_value, new_obj_value )
				else :
					n_beta = min( n_beta, new_obj_value )
					temp_obj_value = min( obj_value, new_obj_value )
				if temp_obj_value <> obj_value:
					obj_value = temp_obj_value
					self.move = i
				if alpha >= beta:
					break
		return obj_value

	def __str__( self ):
		return str( self.root )

	def __repr__( self ):
		return str( self )
