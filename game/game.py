import tkinter as tk
from settings import *
import random
import numpy as np


class Game(tk.Frame):
    def __init__(self, size):
        tk.Frame.__init__(self)
        self.grid()
        self.size = size
        self.master.title("2048")
        # self.master.iconbitmap("@../assets/icon.ico")
        
        self.main_grid = tk.Frame(
            self, bg=GRID_COLOR, bd=3, width=GRID_SIZE, height=GRID_SIZE
        )
        self.main_grid.grid(
            pady=(100,0)
        )
        self.make_UI()
        self.init_game()
        
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
    
    
    def make_UI(self):
        #Number grid
        self.cells = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                cell_frame =tk.Frame(
                    self.main_grid,
                    bg=EMPTY_COLOR,
                    width = GRID_SIZE / self.size,
                    height = GRID_SIZE / self.size
                )
                cell_frame.grid(row=x, column=y, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=EMPTY_COLOR)
                cell_number.grid(row=x, column=y)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
        

        self.make_scores()
        self.make_title()
        

    def make_scores(self):
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.8, y=45, anchor="center")
        # Score Label
        tk.Label(
            score_frame,
            text="Score",
            font=SCORE_LABEL_FONT
        ).grid(row=0, column=0)

        self.score_label = tk.Label(score_frame, text="0", font=SCORE_FONT)
        self.score_label.grid(row=1, column=0)

        # High Score Label
        tk.Label(
            score_frame,
            text="High Score",
            font=SCORE_LABEL_FONT
        ).grid(row=0, column=1)

        self.high_score_label = tk.Label(score_frame, text="0", font=SCORE_FONT)
        self.high_score_label.grid(row=1, column=1)
        
    def make_title(self):
        title_frame = tk.Frame(self)
        title_frame.place(x=20, y=20)

        title_label = tk.Label(title_frame, text="2048", font=("Arial", 24, "bold"))
        title_label.pack()
    
    def init_game(self):
        self.matrix = np.zeros((self.size, self.size), dtype=int)
        self.add_new_tile(2)
        self.add_new_tile(2)
        self.score = 0
        self.update_ui()
    
    def update_ui(self):
        for x in range(self.size):
            for y in range(self.size):
                cell_value = self.matrix[x][y]
                if cell_value == 0:
                    self.cells[x][y]["frame"].configure(bg=EMPTY_COLOR)
                    self.cells[x][y]["number"].configure(
                        bg=EMPTY_COLOR, text="")
                else:
                    self.cells[x][y]["frame"].configure(
                        bg=CARD_COLORS[cell_value]["tile_color"]) #??? 
                    self.cells[x][y]["number"].configure(
                        bg=CARD_COLORS[cell_value]["tile_color"],
                        fg=CARD_COLORS[cell_value]["label_color"],
                        font=CARD_COLORS[cell_value]["font"],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    # def add_new_tile(self, number: int = 2): # random.choice([2, 4])
    #     row = random.randint(0, self.size-1)
    #     col = random.randint(0, self.size-1)
        
    #     while(self.matrix[row][col] != 0):
    #         row = random.randint(0, self.size-1)
    #         col = random.randint(0, self.size-1)
        
    #     self.matrix[row, col] = number
    
    def add_new_tile(self, number = None):
        if (number is None):
            number = np.random.choice([2, 4], p=[0.6, 0.4])
        empty_cells = list(zip(*np.where(self.matrix == 0)))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row, col] = number
    
    def stack(self):
        new_matrix = np.zeros((self.size, self.size), dtype=int)
        for x in range(self.size):
            fill_pos = 0
            for y in range(self.size):
                if(self.matrix[x, y] != 0):
                    new_matrix[x, fill_pos] = self.matrix[x, y]
                    fill_pos += 1
        self.matrix = new_matrix
    
    def combine(self):
        for x in range(self.size):
            for y in range(self.size-1):
                if((self.matrix[x][y] != 0) and (self.matrix[x][y] == self.matrix[x][y+1])):
                    self.matrix[x][y] *= 2
                    self.matrix[x][y+1] = 0
                    self.score += self.matrix[x][y]
    
    
    def move_left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_ui()
        self.check_game_over()
    
    def move_right(self, event):
        self.matrix = np.rot90(self.matrix, k=2)
        self.stack()
        self.combine()
        self.stack()
        self.matrix = np.rot90(self.matrix, k=2)
        self.add_new_tile()
        self.update_ui()
        self.check_game_over()

    # def move_up(self, event):
    #     self.matrix = np.transpose(self.matrix)
    #     self.stack()
    #     self.combine()
    #     self.matrix = np.transpose(self.matrix)
    #     self.add_new_tile()
    #     self.update_ui()
    
    def move_up(self, event):
        self.matrix = np.rot90(self.matrix, k=1)   # Rotar 90 grados en sentido horario
        self.stack()
        self.combine()
        self.stack()  # Necesitas apilar nuevamente después de combinar
        self.matrix = np.rot90(self.matrix, k=-1)  # Rotar 90 grados en sentido antihorario
        self.add_new_tile()
        self.update_ui()
        self.check_game_over()
    
    # def move_down(self, event): #puedo hacer un 90grados antihorario
    #     self.matrix = np.transpose(self.matrix)
    #     self.matrix = np.rot90(self.matrix, k=2)
    #     self.stack()
    #     self.combine()
    #     self.matrix = np.rot90(self.matrix, k=2)
    #     self.matrix = np.transpose(self.matrix)
    #     self.add_new_tile()
    #     self.update_ui()
        
    def move_down(self, event):
        self.matrix = np.rot90(self.matrix, k=-1)  
        self.stack()
        self.combine()
        self.stack()  # Necesitas apilar nuevamente después de combinar
        self.matrix = np.rot90(self.matrix, k=1)   
        self.add_new_tile()
        self.update_ui()
        self.check_game_over()
    
    def moves_exists(self): # Check possible moves in all directions
        for row in range(self.size):
            for col in range(self.size):
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < self.size and 0 <= new_col < self.size and self.matrix[row, col] == self.matrix[new_row, new_col]:
                        return False 
        return True
    
    def check_game_over(self):
        if(any(2048 in row for row in self.matrix)):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="You Win!",
                bg=WINNER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT
            ).pack()
        elif(not any(0 in row for row in self.matrix) and (not self.moves_exists())):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game Over!",
                bg=LOSER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT
            ).pack()
            
    
    
if __name__ == "__main__":
    app = Game(2)
    app.mainloop()
