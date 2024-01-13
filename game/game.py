from tkinter import *
from tkinter.font import Font
from settings import *
import random
import numpy as np
from PIL import Image, ImageFont, ImageTk


class Game(Frame):
    def __init__(self, size, user_mode: bool = True):
        Frame.__init__(self)
        self.grid()
        self.size = size
        self.high_score = 0
        
        self.img = PhotoImage(file="assets/change.png")
        
        # Window Config.
        self.master.title("2048")
        self.icon = PhotoImage(file="assets/icon.png")
        self.master.iconphoto(True, self.icon)
        self.master.config(background=GAME_COLOR)
        
        # Grid config
        self.background = Frame(
            self, 
            bg=GAME_COLOR,
            width=GRID_SIZE + 200, 
            height=GRID_SIZE + 400
        )
        self.background.grid(row=0, column=0)
        self.main_grid = Frame(
            self.background, 
            bg=GRID_COLOR,
            bd=2, 
            width=GRID_SIZE, 
            height=GRID_SIZE
        )
        
        self.main_grid.grid(
            padx=12,
            pady=(70, 0)
        )
        
        # Initialize GUI
        self.make_UI()
        self.init_game()
        
        
        #Initialize Directions
        if(user_mode):
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
                cell_frame =Frame(
                    self.main_grid,
                    bg=EMPTY_COLOR,
                    width = GRID_SIZE / self.size,
                    height = GRID_SIZE / self.size
                )
                cell_frame.grid(row=x, column=y, padx=5, pady=5)
                cell_number = Label(self.main_grid, bg=EMPTY_COLOR)
                cell_number.grid(row=x, column=y)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
        
        self.make_menu()

        self.make_title()

    def make_menu(self):
        # Crear un Frame contenedor para el menu
        menu_frame = Frame(self.background, bg=GAME_COLOR)

        # Frame para Score
        self.score_frame = Frame(menu_frame, bg=BUTTON_COLOR)
        self.score_frame.grid(row=0, column=0, padx=10, pady=0)
        

        Label(
            self.score_frame,
            text="Score",
            font=("Helvetica", 16),
            bg=BUTTON_COLOR,
            padx=15,
            pady=5,
        ).grid(row=0, column=0)

        self.score_label = Label(self.score_frame, text="0", font=("Helvetica", 14), bg=BUTTON_COLOR, pady=5)
        self.score_label.grid(row=1, column=0)

        # Frame para High Score
        self.high_score_frame = Frame(menu_frame, bg=BUTTON_COLOR)
        self.high_score_frame.grid(row=0, column=1, padx=10, pady=10)

        Label(
            self.high_score_frame,
            text="High Score",
            font=("Helvetica", 16),
            bg=BUTTON_COLOR,
            padx=15,
            pady=5,
        ).grid(row=0, column=0)

        self.high_score_label = Label(self.high_score_frame, text="0", font=("Helvetica", 14), bg=BUTTON_COLOR, pady=5)
        self.high_score_label.grid(row=1, column=0)
        
        # Restart game
        button = Button(menu_frame, image=self.img, command=self.init_game, bg=BUTTON_COLOR)
        button.grid(row=0, column=2, columnspan=2, pady=10)

        menu_frame.place(relx=0.8, y=30, anchor="center")

    def make_title(self):
        title_frame = Frame(self.background, bg=GAME_COLOR)
        title_frame.place(x=20, y=30)
        
        custom_font = Font(family="Helvetica", size=50)
        
        title_label = Label(title_frame, text="2048", bg=GAME_COLOR, font=custom_font)
        title_label.pack(padx=20)

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
        if(self.score > self.high_score):
            self.high_score = self.score
            self.high_score_label.configure(text=self.high_score)
        self.update_idletasks()
    
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
        return self.check_game_over()
    
    def move_right(self, event):
        self.matrix = np.rot90(self.matrix, k=2)
        self.stack()
        self.combine()
        self.stack()
        self.matrix = np.rot90(self.matrix, k=2)
        self.add_new_tile()
        self.update_ui()
        return self.check_game_over()
    
    def move_up(self, event):
        self.matrix = np.rot90(self.matrix, k=1)   # Rotar 90 grados en sentido horario
        self.stack()
        self.combine()
        self.stack()  # Necesitas apilar nuevamente después de combinar
        self.matrix = np.rot90(self.matrix, k=-1)  # Rotar 90 grados en sentido antihorario
        self.add_new_tile()
        self.update_ui()
        return self.check_game_over()
    
    def move_down(self, event):
        self.matrix = np.rot90(self.matrix, k=-1)  
        self.stack()
        self.combine()
        self.stack()  # Necesitas apilar nuevamente después de combinar
        self.matrix = np.rot90(self.matrix, k=1)   
        self.add_new_tile()
        self.update_ui()
        return self.check_game_over()
    
    def moves_exists(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.matrix[row, col] == 0:
                    return True 
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if (
                        0 <= new_row < self.size
                        and 0 <= new_col < self.size
                        and self.matrix[row, col] == self.matrix[new_row, new_col]
                    ):
                        return True  
        return False 
    
    def check_game_over(self):
        if(any(2048 in row for row in self.matrix)):
            game_over_frame = Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
                game_over_frame,
                text="You Win!",
                bg=WINNER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT
            ).pack()
            return False
        elif(not self.moves_exists()):
            game_over_frame = Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
                game_over_frame,
                text="Game Over!",
                bg=LOSER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT
            ).pack()
            return True
    
    def play_step(self, action):
        actions_mapping = {
            (1, 0, 0, 0): self.move_up,
            (0, 1, 0, 0): self.move_right,
            (0, 0, 1, 0): self.move_down,
            (0, 0, 0, 1): self.move_left
        }

        last_score = self.score
        action_function = actions_mapping[tuple(action)]
        done = action_function()
        reward = self.score - last_score
        return reward, done, self.score

if __name__ == "__main__":
    app = Game(4)
    app.mainloop()


#TODO: TENGO QUE AGREGAR LAS FONTS, MEJORAR LA PRESENTACION DEL SCORE Y DEL TITULO, DAR LA OPCION DE ELEGIR POR LA VENTANA EL TAMAÑO DEL TABLERO 3X3, 4X4, 5X5, 6X6, 8X8, Y TAMBIEN SI SE JUEGA EN MODO USUARIO O IA, Y SI LA IA ESTA ENTRENADA O QUE EMPIECE A ENTRENAR DESDE 0. METER TODO LO DE LA IA.
