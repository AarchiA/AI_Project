# Computer trying to play 2048 like a human, also taking the best possible move according to min max algorithm 

from Helper import *
from Minimaxa import *
from Grid import *
import numpy as np

class Max_turn():
	def getMove(self, grid):
		moves = grid.getAvailableMoves()
		maxUtility = -np.inf
		nextDir = -1

		for move in moves:
			child = getChild(grid, move)

			utility = Decision(grid=child, max=False) 

			if utility >= maxUtility:
				maxUtility = utility
				nextDir = move

		return nextDir