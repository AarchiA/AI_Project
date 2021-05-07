#Functions defined here are useful for getting the best possible next move
#This is used to get the Child of a node in a particular direction

def getChild(grid, dir):
	temp = grid.clone()
	temp.move(dir)
	return temp

#For getting all the children of a node
def children(grid):
	children = []
	for move in grid.getAvailableMoves():
		children.append(getChild(grid, move))
	return children

#Returns true if the node is terminal
def terminal(grid):
	return not grid.canMove()

#The HEURISTIC function
#Evaluates the heuristic. The heuristic used here is a gradient function
def Eval(grid):
	import math 
	import numpy as np

	if terminal(grid):
		return -np.inf

	gradients = [
				[[ 3,  2,  1,  0],[ 2,  1,  0, -1],[ 1,  0, -1, -2],[ 0, -1, -2, -3]],
				[[ 0,  1,  2,  3],[-1,  0,  1,  2],[-2, -1,  0,  1],[-3, -2, -1, -0]], 
				[[ 0, -1, -2, -3],[ 1,  0, -1, -2],[ 2,  1,  0, -1],[ 3,  2,  1,  0]], 
				[[-3, -2, -1,  0],[-2, -1,  0,  1],[-1,  0,  1,  2],[ 0,  1,  2,  3]]
				]

	values = [0,0,0,0]

	for i in range(4):
		for x in range(4):
			for y in range(4):
				values[i] += gradients[i][x][y]*grid.map[x][y]

	return max(values)