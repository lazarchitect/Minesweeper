# Minesweeper
Minesweeper clone in Python 3 using the built-in Tkinter GUI module. 

The main mechanic of the game involves an overlay of a logical 2D array of integers forming the backbone, 
and a visual grid of block objects forming the front end. 

Each square has a number associated with it; the number's meaning changes depending on its value. 
0-8 describes the number of mines in adjacent blocks, which is the core gameplay mechanic. 
A 9 represents a mine (9 adjacent mines is impossible). 
Clicking on a square reveals its number, or, if its a 9, the game ends. 
If the number revealed is a 0, the game then runs the reveal function on any nearby blocks, 
and if any of them are zeroes, this repeats again, in a recursive fashion, until all zeroes in a contiguous block are revealed. 

A blue square is unclicked. Red is a mine. Purple is an unknown (question mark) block. 
