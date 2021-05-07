from Grid       import Grid
from Min_Player import Min_turn
from Max_Player   import Max_turn
from Display  import Displayer
from random       import randint
import time

defaultInitialTiles = 2
defaultProbability = 0.9

actionDic = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}

(Max, Min) = (0, 1) # Computer turn generates random number while player turn moves according to the action

# Time Limit Before Losing
timeLimit = 0.2
allowance = 0.05

class Main_Game:
    def __init__(self, size = 4): #4*4 grid
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4] # Random tiles can be of value either 2 or 4 
        self.probability = defaultProbability # Probability for generating random number
        self.initTiles  = defaultInitialTiles #Initial random tiles
        self.min_turn = None
        self.max_turn   = None
        self.displayer  = None
        self.over       = False

    def setMin_turn(self, min_turn): 
        self.min_turn = min_turn

    def setMax_turn(self, max_turn):
        self.max_turn = max_turn

    def setDisplayer(self, displayer):
        self.displayer = displayer

    #Updating and setting the time bounds 
    def updateAlarm(self, currTime): 
        if currTime - self.prevTime > timeLimit + allowance:
            self.over = True
        else:
            while time.process_time() - self.prevTime < timeLimit + allowance:
                pass

            self.prevTime = time.process_time()
    
    #Starting the game
    def start(self):
        for i in range(self.initTiles):
            self.insertRandomTile() #Insert random values

        self.displayer.display(self.grid) # Display the grid

        # Player AI Goes First to move either left, right, up or down
        turn = Max
        maxTile = 0 #Initially max value is zero, later updated

        self.prevTime = time.process_time() #setting time 

        while not self.isGameOver() and not self.over: # Checking the conditions if empty tile is available or not
            
            gridCopy = self.grid.clone() # Copy to make sure that AI Cannot Change the Real Grid to Cheat
            move = None

            if turn == Max:
                print("Max player moves ", end="")
                move = self.max_turn.getMove(gridCopy) # Max Player's turn to move either up, down, left or right
                print(actionDic[move])

                # Checking the validate Move
                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        # Update maxTile
                        maxTile = self.grid.getMaxTile()
                    else:
                        print("Invalid Move made by max player")
                        self.over = True
                else:
                    print("Invalid Max Player Move - 1")
                    self.over = True
            else:
                print("Min Player places number at position ", end ="")
                move = self.min_turn.getMove(gridCopy) #Min Player's turn to generate random number
                print(move)
                #Checking the validate Move
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer AI Move")
                    self.over = True

            if not self.over:
                self.displayer.display(self.grid)

            # Exceeding the Time Allotted for Any Turn Terminates the Game
            self.updateAlarm(time.process_time())

            turn = 1 - turn
        print(maxTile)
        print("Game Over with maximum value as", maxTile)

    #To check if any move is possible
    def isGameOver(self):
        return not self.grid.canMove()

    #To select 2 or 4 as the random tile
    def getNewTileValue(self):
        if randint(0,99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1]

    #Inserting the random tile
    def insertRandomTile(self):
        tileValue = self.getNewTileValue()
        cells = self.grid.getAvailableCells()
        cell = cells[randint(0, len(cells) - 1)]
        self.grid.setCellValue(cell, tileValue)

#Main function
def main():
    maingame = Main_Game()
    max_turn  	= Max_turn()
    min_turn  = Min_turn()
    displayer 	= Displayer()

    maingame.setDisplayer(displayer)
    maingame.setMax_turn(max_turn)
    maingame.setMin_turn(min_turn)
    maingame.start()

if __name__ == '__main__':
    main()