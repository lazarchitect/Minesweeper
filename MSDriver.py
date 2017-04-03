import MSGrid
import time

def printgrid(arr):
	print("  ",end="")
	index = len(arr[0])
	for x in range(index):
		print(str(x)+" ", end="")
	print()
	index = 0
	for i in arr:
		print(index,end="")
		index+=1
		for j in i:
			print("|"+str(j), end="")
		print("|\n")

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

mask = MSGrid.maskInitialize(n, m)

def sweep(y, x):
	if( y < 0 or x < 0 or y >= n or x >= m):
		return 0
	if mask[y][x] != ' ':
		return 0
	if(grid[y][x] == 9):
		print("BOOM! YOU DIED")
		printgrid(grid)
		input("exit >>")
		exit(0)
	mask[y][x] = grid[y][x]
	if(grid[y][x] > 0):
		return 1
	retval = 1	
	for horz1 in [-1, 0, 1]:
		retval += sweep(y-1, x+horz1)
	for horz2 in [-1, 1]:
		retval += sweep(y, x+horz2)
	for horz3 in [-1, 0, 1]:
		retval += sweep(y+1, x+horz3)
	return retval	
	
print("top left corner is 0,0. Enter coordinates to check for mines.")
start = time.time()
while(1):
	print("time taken so far:", time.time()-start)
	try:
		printgrid(mask)
		x = int(input("Enter an x coordinate >> "))
		y = int(input("\nEnter a y coordinate >> "))
		if x >= m or y >= n: raise IndexError
		flagFlag = input("type F to toggle a flag or anything else to sweep the block: >>")
		if(flagFlag == "F" or flagFlag == "f"):
			if type(mask[y][x]) is not int:
				if mask[y][x] == 'F': 
					mask[y][x] = ' '
					print("flag toggled off.")
				else: 
					mask[y][x] = 'F'
					print("flag toggled on.")
			continue		
				
	except IndexError: 
		print("Input index too large. Try again.\n")
		continue
	except ValueError:
		print("Input must be a valid integer. Try again.\n")
		continue
	remainingBlocks -= sweep(y, x)
	if(remainingBlocks == numMines):
		print("all mines found!")
		end = time.time()
		timeTaken = int(end - start)
		print("total time taken:", timeTaken,"seconds")
		
		name = input("Enter your name to be entered into the scoreboard. >>")
		f = open("scores.txt", "a")
		f.write(name + ","+str(x)+"x"+str(y)+": "+str(timeTaken)+" seconds\n")

		f = open("scores.txt", "r")
		print("scores:")
		for line in f: print(line, end="")
		exit(0)