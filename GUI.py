# idea: 
# grid in mask. each thing is a button. clicking the button degrids it, and grids in grid[y][x], the number, there as a label.

import MSGrid
import time
from tkinter import *
# from PIL import Image, ImageTk

while(1):
	try:
		n = int(input("How tall should the grid be? >> "))
		m = int(input("How wide should the grid be? >> "))
		if(n<=0 or m<=0): raise IndexError
		break
	except IndexError: 
		print("must be positive.")
	except ValueError:
		print("must be valid integers.")
numMines = int((n*m)/6)

grid = MSGrid.gridInitialize(n, m, numMines)
remainingBlocks = n*m


root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
buttonHeight = int(h/n/20)
buttonWidth = int(w/m/20)

def sweep(y, x):
	
	
	#out of bounds check
	if( y < 0 or x < 0 or y >= n or x >= m):
		return 0
	#already been here?	
	if str(type(board[y][x])) != "<class '__main__.cell'>": 
		return 0
	board[y][x].core.destroy()
	board[y][x] = None
	
	timeLabel.config(text = "Time taken: "+str(int(time.time()) - start)+" seconds")
	
	if grid[y][x] == 0:
		Label(root, text = " ", width = buttonWidth, height = buttonHeight).grid(row = y, column = x)
	else: 
		Label(root, text = grid[y][x], width = buttonWidth, height = buttonHeight).grid(row = y, column = x)
		return 1
	
	retval = 1
	for horz1 in [-1, 0, 1]:
		retval += sweep(y-1, x+horz1)
	for horz2 in [-1, 1]:
		retval += sweep(y, x+horz2)
	for horz3 in [-1, 0, 1]:
		retval += sweep(y+1, x+horz3)
	return retval
	
start = time.time()
timeLabel = Label(root, text = "Time taken: 0", font = ("Helvetica", 16))

#reveals all mines and diables all buttons
def gameOver():
	for y in range(n):
		for x in range(m):
			try:
				B = board[y][x].core
			except:
				continue	
			B.config(state = DISABLED)
			B.unbind("<Button-3>")
			if grid[y][x] == 9:
				B.grid_forget()
				Label(root, text = "B", fg = "RED", width = buttonWidth, height = buttonHeight).grid(row = y, column = x)

class cell():
	
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.core = Button(root, text = "  ",width = buttonWidth, height = buttonHeight,  bg = "#3333ff")
		
	def leftClick(self):
		if grid[self.y][self.x] == 9:
			timeLabel.config(text = "BOOM! YOU LOSE")
			gameOver()
			
		else:
			global remainingBlocks
			global numMines
			remainingBlocks -= sweep(self.y, self.x)
			if remainingBlocks == numMines:
				timeLabel.config(text = "YOU WIN! Time taken: "+str(int(time.time()) - start)+" seconds")
				for y in range(n):
					for x in range(m):
						try:
							B = board[y][x].core
						except:
							continue	
						B.config(state = DISABLED)
		
	def rightClick(self, event):
		if(self.core.config()["background"][4] == "#3333ff"):
			self.core.config(bg = "RED", state = DISABLED)
		elif(self.core.config()["background"][4] == "RED"):
			self.core.config(bg = "#ff00ff", state = NORMAL)
		else: self.core.config(bg = "#3333ff")
		
board = []		
for y in range(n):
	board.append([])
	for x in range(m):
		board[y].append(cell(x, y))
		B = board[y][x]
		B.core.config(command = B.leftClick)
		B.core.bind("<Button-3>", B.rightClick)
		B.core.grid(row = y, column = x)

timeLabel.grid(row = y+1, column = 0, columnspan = m+100)
root.mainloop()