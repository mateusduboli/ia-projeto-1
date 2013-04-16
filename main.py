from lig4 import Game
from window import Window
from oponent import Oponent

def main():
	comp = Oponent()
	game = Game()
	w = Window(game, comp)
	w.show()

if __name__ == "__main__":
	main()