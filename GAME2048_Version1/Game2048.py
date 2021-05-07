import tkinter as tk
import random
import colors as c

class Game(tk.Frame):
    def __init__(self): #Constructing game as frame widget
        tk.Frame.__init__(self) 
        self.grid() #For creating game grid
        self.master.title("** The 2048 Game **") #Set the title
        print("Enter the board size : ") 
        self.n=int(input()) #Take the input from user about the board size that the user wants to play for
        self.main_grid = tk.Frame(
        self, bg=c.GRID_COLOR, bd=5, width=400, height= 400)
        self.main_grid.grid(pady=(90, 0)) #Outline of GUI
        self.make_GUI()
        self.start_game() # For starting the game
        self.master.bind("<Left>", self.left) # left arrow key and corresponding function 
        self.master.bind("<Right>", self.right) #right arrow key and corresponding function
        self.master.bind("<Up>", self.up) #up arrow key and corresponding funcion
        self.master.bind("<Down>", self.down) # down arrow key and corresponding function
        self.mainloop() # GUI is continuously running

    def make_GUI(self):

        self.cells =[] # Holding the information contained in each cell of the grid
        for i in range(self.n): #Appending cells row by row
            row = []
            for j in range(self.n):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width = 600//self.n,
                    height =600//self.n)
                cell_frame.grid (row=i, column=j, padx=5,pady=5) #grid lines between cell
                cell_number= tk.Label(self.main_grid, bg =c.EMPTY_CELL_COLOR) #number value of the cell
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}#dictionary to store the cell data
                row.append(cell_data) # appending cell data to row
            self.cells.append(row) #appending each row to cell
        
        #For displaying score
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=40, anchor ="center") #position
        tk.Label(score_frame, text = "Score", font =c.SCORE_LABEL_FONT).grid(row=0) #label 
        self.score_label = tk.Label(score_frame, text ="0", font = c.SCORE_FONT) #actual score, initially zero
        self.score_label.grid(row=1)# place score undder score label

    def start_game(self):
        #Initilaise the matrix with zeros
        self.matrix = [[0]*self.n for _ in range(self.n)]

        #For filling the random value
        row = random.randint(0,self.n-1) #randomly select row
        col = random.randint(0,self.n-1) #randomly select column
        self.matrix[row][col]=2 # placing the first value=2 randomly
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text = "2"
        )
        #repeating the same process for placing the second value=2 randomly
        while (self.matrix[row][col]!=0):
            row =random.randint(0,self.n-1)
            col = random.randint(0,self.n-1)
        self.matrix[row][col]=2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
                bg=c.CELL_COLORS[2],
                fg=c.CELL_NUMBER_COLORS[2],
                font=c.CELL_NUMBER_FONTS[2],
                text = "2"
            )

        self.score = 0 # To keep track of the score

    #Matrix functions called during the game

    def stack (self): #Used to compress all the non-zeroes numbers to one side of the board removing the gap in between
        new_matrix = [[0]*self.n for _ in range (self.n)] # initialise zero matrix
        for i in range(self.n):
            fill_position = 0 # keep track of non zero number 
            for j in range(self.n):
                if self.matrix[i][j]!=0:
                    new_matrix[i][fill_position]=self.matrix[i][j] 
                    fill_position +=1
        self.matrix = new_matrix

    def combine(self): #Used to add all horizontally adjacent non zero numbers of the same value and merges to left
        for i in range(self.n):
            for j in range (self.n-1):
                if (self.matrix[i][j]!=0 and self.matrix[i][j]==self.matrix[i][j+1]):
                    self.matrix[i][j] *=2 # double the value
                    self.matrix[i][j+1]=0 # make one cell zero
                    self.score +=self.matrix[i][j] #updating the score

    def reverse(self): #Used to reverse the order of each row of the matrix
        new_matrix =[]
        for i in range (self.n):
            new_matrix.append([])
            for j in range(self.n):
                new_matrix[i].append(self.matrix[i][self.n-1-j]) #order the values that are reversed
        self.matrix = new_matrix

    def transpose(self): #Used to flip the matrix over the diagonal
        new_matrix = [[0]*self.n for _ in range (self.n)]
        for i in range (self.n):
            for j in range (self.n):
                new_matrix[i][j]= self.matrix[j][i]
        self.matrix = new_matrix

    #Randomly add a new tile(2/4) after each move to an empty cell 

    def add_new_tile(self):
        if any(0 in row for row in self.matrix):
            row = random.randint(0,self.n-1)
            col = random.randint(0,self.n-1)
            while (self.matrix[row][col]!=0):
                row =random.randint(0,self.n-1)
                col = random.randint(0,self.n-1)
            self.matrix[row][col]=random.choice([2,4])

    #Updating the GUI according to newly created board

    def update_GUI(self):
        for i in range (self.n):
            for j in range (self.n):
                cell_value = self.matrix[i][j]
                if cell_value ==0: # For Empty cells
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR, text = "")
                else: #For non zero value cells
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font= c.CELL_NUMBER_FONTS[cell_value],
                        text = str(cell_value)
                        )
                        
        self.score_label.configure(text=self.score) # update score 
        self.update_idletasks() # To immediately update the widget display
                            
    #The lef, right, up, down arrow functions

    def left(self, event):
        self.stack() # compress non zero number to left side of board
        self.combine() # combine horizontally adjacent numbers
        self.stack() # to eliminate newly created zero cells from the combine function
        self.add_new_tile() # add a random tile
        self.update_GUI() # update the GUI
        self.game_over()

    def right(self, event):
        self.reverse() #first reverse right move to left and then do the same as left move
        self.stack() # compress non zero number to left side of board
        self.combine() # combine horizontally adjacent numbers
        self.stack() # to eliminate newly created zero cells from the combine function
        self.reverse() # back to original orientation
        self.add_new_tile() # add a random tile
        self.update_GUI()  # update the GUI
        self.game_over()

    def up (self, event):
        self.transpose() # transpose the matrix to make it work like left move
        self.stack() # compress non zero number to left side of board
        self.combine() # combine horizontally adjacent numbers
        self.stack() # to eliminate newly created zero cells from the combine function
        self.transpose() # to original 
        self.add_new_tile() # add a random tile
        self.update_GUI() # update the GUI
        self.game_over()

    def down(self, event):
        self.transpose() # for left move to have downward effect
        self.reverse()
        self.stack() # compress non zero number to left side of board
        self.combine() # combine horizontally adjacent numbers
        self.stack() # to eliminate newly created zero cells from the combine function
        self.reverse() # works like right
        self.transpose() # for working like left
        self.add_new_tile()  # add a random tile
        self.update_GUI() # update the GUI
        self.game_over()

    # For checking if any horizontal move is possible
    def horizontal_move_exists(self):
        for i in range (self.n):
            for j in range (self.n-1):
                if self.matrix[i][j]== self.matrix[i][j+1]:
                    return True
        return False
    # For checking if any vertical move is possible
    def vertical_move_exists(self):
        for i in range (self.n-1):
            for j in range (self.n):
                if self.matrix[i][j] == self. matrix[i+1][j]:
                    return True
        return False


#To check if game is over

    def game_over(self):
        if any (2048 in row for row in self.matrix): # If 2048 is present in the board
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor ="center")
            tk.Label(
                game_over_frame,
                text="You Win :)",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font= c.GAME_OVER_FONT).pack()
        elif not any (0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists(): # If no empty cell and no horizontal or vertical move is possible
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor ="center")
            tk.Label(
                game_over_frame,
                text="You Lose :(",
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font= c.GAME_OVER_FONT
            ).pack()

def main(): #instance of game
    Game()

if __name__ == "__main__":
    main()