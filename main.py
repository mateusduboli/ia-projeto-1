from lig4 import Game
from window import Window
from oponent import Oponent
import thread
from copy import deepcopy

def showW1(p):
	w1.show()
	
def showW2(p):
	w2.show()

def main():
	global w1, w2 
	comp1 = Oponent()
	comp2 = Oponent()
	game1 = Game(comp1)
	game2 = Game(comp2)
	w1 = Window(game1)
	w2 = Window(game2)
	p1 = 0
	p2 = 0
	thread.start_new(showW1, (p1,))
	thread.start_new(showW2, (p2,))
	while(True):
		pass
	
if __name__ == "__main__":
	main()
