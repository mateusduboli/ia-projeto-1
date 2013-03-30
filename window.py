from Tkconstants import CENTER
from Tkinter import *
import tkMessageBox


class Window:
	def __init__(self, game):
		self.labels = [[0] * 7 for i in range(7)]
		self.game = game
		self.root = Tk()
		self.root.title("Lig 4 - Minimax")
		self.frame = Frame(self.root)
		self.frame.pack()
		for i in range(7):
			for j in range(7):
				self.labels[i][j] = self.__init_label(i, j)

	def __init_label(self, i, j):
		label = Label(self.frame, name=str(i) + ", " + str(j))
		label['text'] = self.__label_value(self.game.get(i, j))
		label['justify'] = CENTER
		label['width'] = 7
		label['height'] = 3
		label.bind("<Button-1>", self.__button_callback)
		label.grid(row=i, column=j, sticky=W + E + N + S)
		return label

	def __button_callback(self, event):
		grid_info = event.widget.grid_info()
		x, y = self.game.drop_disc_human(int(grid_info['column']))
		if(not self.game.has_ended()):
			self.__update_label(x , y)
			if (self.game.check_victory(x, y)):
				self.__human_win()
		if(not self.game.has_ended()):
			x, y = self.game.drop_disc_computer()
			self.__update_label(x, y)
			if(self.game.check_victory(x, y)):
				self.__computer_win()
			

	def __label_value(self, value):
		if(value == 1):
			return 'O'
		elif (value == 2):
			return 'X'
		else :
			return '-'

	def __update_label(self, x, y):
		self.__label_value(self.game.get(x, y))
		self.labels[x][y]['text'] = self.__label_value(self.game.get(x, y))

	def __human_win(self):
		tkMessageBox.showinfo("Vitoria", "Voce venceu!")
		self.game.end_game()
		
	def __computer_win(self):
		tkMessageBox.showinfo("Derrota", "Voce perdeu")
		self.game.end_game()
		
	def show(self):
		self.root.mainloop()
