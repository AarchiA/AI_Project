# Used to place a tile randomly at available positions on the board

from random import randint

class Min_turn():
    def getMove(self, grid):
        cells = grid.getAvailableCells()

        return cells[randint(0, len(cells) - 1)] if cells else None