#minesweeper.py



"""CREATE THE ARRAY
Step 1: create a grid (2D array) of integers. 
9 means this spot is a mine. Otherwise, the number in any given cell is the number of  mines in surrounding cells.
Initialize the array to all zeroes.

Step 2: place mines randomly.
Select arbitrary cells to be mines. Change their number to be 9.

Step 3: Fill up the array with the other numbers.
Iterate through the array, and do a count of surrounding mines. Change this number to that result.
"""

#generates and returns a working minesweeper
def gridInitialize(n, m, numMines):
	
	grid = []

	def populate():
		for i in range(n):
			sublist = []
			for j in range(m):
				sublist.append(0)
			grid.append(sublist)
		
	def mineInsert():
		from random import randint
		for i in range(numMines):	
			x, y = randint(0, n-1), randint(0, m-1)
			# print("x:",x,"y:",y)
			while(grid[x][y] == 9): 
				x, y = randint(0, n-1), randint(0, m-1)
			grid[x][y] = 9

	def numberInsert():
		for i in range(n):
			for j in range(m):
				numberfill(i, j)

	def topRow(i, j):
		if i == 0: return
		if grid[i-1][j] == 9: grid[i][j]+=1
		if m == 1: return
		if j == 0: 
			if grid[i-1][j+1] == 9: grid[i][j]+=1 #just check above-right
			return
		elif j == m-1: 
			if grid[i-1][j-1] == 9: grid[i][j]+=1 #just check above-left
			return
		else: 
			if grid[i-1][j-1] == 9: grid[i][j]+=1
			if grid[i-1][j+1] == 9: grid[i][j]+=1
		
	def bottomRow(i, j):
		if i == n-1: return
		if grid[i+1][j] == 9: grid[i][j]+=1
		if m == 1: return
		if j == 0:
			if grid[i+1][j+1] == 9: grid[i][j]+=1 #just check below-right
			return
		elif j == m-1: 
			if grid[i+1][j-1] == 9: grid[i][j]+=1 #just check below-left
			return
		else: 
			if grid[i+1][j-1] == 9: grid[i][j]+=1
			if grid[i+1][j+1] == 9: grid[i][j]+=1
		
	def sides(i ,j):
		if m == 1: return #dumb edge case if the grid is 1 cell wide
		if j == 0:
			if grid[i][j+1] == 9: grid[i][j]+=1 #just check right
			return
		elif j == m-1: 
			if grid[i][j-1] == 9: grid[i][j]+=1 #just check left
			return
		else: 
			if grid[i][j-1] == 9: grid[i][j]+=1
			if grid[i][j+1] == 9: grid[i][j]+=1
		
	def numberfill(i, j):
		if grid[i][j] == 9: return
		topRow(i, j)
		sides(i, j)
		bottomRow(i, j)
		
	populate()
	mineInsert()
	numberInsert()
	
	return grid	


"""
purpose of this is to create a dummy array that the user sees initially. 
As they clear spots, the mask is cleared away and each cell reveals (switches to) its coordinated counterpart in the real grid.
"""

def maskInitialize(n, m):
	mask = []
	for i in range(n):
		sublist = []
		for j in range(m):
			sublist.append(' ')
		mask.append(sublist)
	return mask