import platform
import os

#Setting the colours for tiles/cells in our game board
colorMap = {
    0 	  : 97 ,
    2     : 40 ,
    4     : 100,
    8     : 47 ,
    16    : 41,
    32    : 46 ,
    64    : 105,
    128   : 44 ,
    256   : 104,
    512   : 42 ,
    1024  : 102,
    2048  : 43 ,
    4096  : 103,
    8192  : 45 ,
    16384 : 105,
    32768 : 41 ,
    65536 : 101,
    131072: 101,
}

cTemp = "\x1b[%dm%7s\x1b[0m "
def display(self, grid):
        pass
#For displaying the game board on terminal
class Displayer():
   
    def __init__(self):
        if "Windows" == platform.system(): # For knowing the OS
            self.display = self.winDisplay
        else:
            self.display = self.unixDisplay

    #For windows system the function for displaying the board on terminal
    def winDisplay(self, grid):
        for i in range(grid.size):
            for j in range(grid.size):
                print("%6d  " % grid.map[i][j], end="")
            print("")
        print("")
    
    #For unix like system the function for displaying the board 
    def unixDisplay(self, grid):
        for i in range(3 * grid.size):
            for j in range(grid.size):
                v = grid.map[int(i / 3)][j]

                if i % 3 == 1:
                    string = str(v).center(7, " ")
                else:
                    string = " "

                print(cTemp %  (colorMap[v], string), end="")
            print("")

            if i % 3 == 2:
                print("")   