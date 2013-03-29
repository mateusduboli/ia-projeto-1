from Tkconstants import CENTER
from Tkinter import *

def label_value(value):
	if(value == 1):
		return 'O'
	elif (value == 2):
		return 'X'
	else :
		return '-'

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
				self.labels[i][j] = self.init_label(i, j)

	def button_callback(self, event):
		grid_info = event.widget.grid_info()
		x, y = self.game.drop_disc_human(int(grid_info['column']))
		self.update_label(x , y)
		self.game.print_matrix()
		
	def show(self):
		self.root.mainloop()

	def init_label(self, i, j):
		label = Label(self.frame, name=str(i) + ", " + str(j))
		label['text'] = label_value(self.game.get(i, j))
		label['justify'] = CENTER
		label['width'] = 7
		label['height'] = 3
		label.bind("<Button-1>", self.button_callback)
		label.grid(row=i, column=j, sticky=W + E + N + S)
		return label
	
	def update_label(self, x, y):
		print label_value(self.game.get(x,y))
		self.labels[x][y]['text'] = label_value(self.game.get(x, y))
