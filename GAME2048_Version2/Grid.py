from copy import deepcopy

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1)) #Possible moves
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)

class Grid:
    def __init__(self, size=0):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)] #Initially the board is filled with all 0 value

    # Make a Deep Copy of This Object
    def clone(self):
        gridCopy = Grid()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size

        return gridCopy

    # For inserting a tile in an Empty Cell
    def insertTile(self, pos, value):
        self.setCellValue(pos, value)
    
    #Setting the value 
    def setCellValue(self, pos, value):
        self.map[pos[0]][pos[1]] = value

    # Returning all the empty cells in the board
    def getAvailableCells(self):
        cells = []

        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 0:
                    cells.append((x,y))

        return cells

    # Returning the Tile which has the Maximum Value in the board
    def getMaxTile(self):
        maxTile = 0

        for x in range(self.size):
            for y in range(self.size):
                maxTile = max(maxTile, self.map[x][y])

        return maxTile

    # Check if we can Insert a Tile in Position
    def canInsert(self, pos):
        return self.getCellValue(pos) == 0

    # Movement of the Grid (UP, DOWN, LEFT, RIGHT)
    def move(self, dir):
        dir = int(dir)
        if dir == UP:
            return self.moveUD(False)
        if dir == DOWN:
            return self.moveUD(True)
        if dir == LEFT:
            return self.moveLR(False)
        if dir == RIGHT:
            return self.moveLR(True)

    # For moving Up or Down
    def moveUD(self, down):
        r = range(self.size -1, -1, -1) if down else range(self.size) #Setting the range for UP and DOWN
        moved = False

        for j in range(self.size):
            cells = []

            for i in r:
                cell = self.map[i][j]

                if cell != 0: #For non zero tiles
                    cells.append(cell)

            self.merge(cells) #merge the non zero cells

            for i in r:
                value = cells.pop(0) if cells else 0

                if self.map[i][j] != value:
                    moved = True

                self.map[i][j] = value

        return moved

    # For moving left or right
    def moveLR(self, right):
        r = range(self.size - 1, -1, -1) if right else range(self.size) #Setting range for left or right

        moved = False

        for i in range(self.size):
            cells = []

            for j in r:
                cell = self.map[i][j]

                if cell != 0: #For non zero tiles
                    cells.append(cell)

            self.merge(cells) #merge the non zero cells

            for j in r:
                value = cells.pop(0) if cells else 0

                if self.map[i][j] != value:
                    moved = True

                self.map[i][j] = value

        return moved

    # Function to merge Tiles with same value 
    def merge(self, cells):
        if len(cells) <= 1:
            return cells

        i = 0

        while i < len(cells) - 1:
            if cells[i] == cells[i+1]: # Checking two tiles if they are equal
                cells[i] *= 2 # Double the value if equal
                del cells[i+1] # Set one tile as 0
            i += 1

    #For checking if movement is possible
    def canMove(self, dirs = vecIndex):

        # Init Moves to be Checked
        checkingMoves = set(dirs)

        for x in range(self.size):
            for y in range(self.size):

                # If Current Cell is Filled
                if self.map[x][y]:

                    # Look Ajacent Cell Value
                    for i in checkingMoves:
                        move = directionVectors[i]

                        adjCellValue = self.getCellValue((x + move[0], y + move[1]))

                        # If Value is the Same or Adjacent Cell is Empty
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True

                # Else if Current Cell is Empty
                elif self.map[x][y] == 0:
                    return True

        return False

    # For returning all available moves
    def getAvailableMoves(self, dirs = vecIndex):
        availableMoves = []

        for x in dirs:
            gridCopy = self.clone()

            if gridCopy.move(x):
                availableMoves.append(x)

        return availableMoves
    
    #Checking the boundary limits
    def crossBound(self, pos):
        return pos[0] < 0 or pos[0] >= self.size or pos[1] < 0 or pos[1] >= self.size

    #Fetch the cell value
    def getCellValue(self, pos):
        if not self.crossBound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None
#Driver code
if __name__ == '__main__':
    g = Grid()
    g.map[0][0] = 2
    g.map[1][0] = 2
    g.map[3][0] = 4

    while True:
        for i in g.map:
            print(i)

        print(g.getAvailableMoves())

        v = input()

        g.move(v)