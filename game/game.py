import pygame
from settings import *
from ui.pregame import Pregame
from ui.menu import Menu
from ui.board import Board
import numpy as np
import random
import sys

# LD_PRELOAD=/usr/lib/libstdc++.so.6 python -u "/home/papadedios/Documents/Repos/2048-ai/game/game.py"

class Game:
    def __init__(self, size: int = 4):
        pygame.init()
        # Init data
        self.size = size
        self.high_score = 0 
        
        # Pygame config
        pygame.display.set_caption("2048")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(pygame.Color(BACKGROUND_COLOR))
        
        # Pregame view
        self.pregame = Pregame(self.screen, self.clock)
        self.pregame.run()
        
        #Title
        self.add_title()

        # UI and pygame
        pygame.init()
        self.menu_ui = Menu(self.screen)
        self.board_ui = Board(size = self.size, screen = self.screen)

        # Init board and run
        self.init_game()
        self.run()



    def add_title(self):
        font = pygame.font.Font(FONT_BOLD, 80)  
        title_text = font.render("2048", True, TITLE_COLOR)  
        title_rect = title_text.get_rect(topleft=(45, 28))
        self.screen.blit(title_text, title_rect)


    def init_game(self):
        self.game_over = False
        self.win = False
        self.first_time_won = False
        self.matrix = np.zeros((self.size, self.size), dtype=int)
        self.old_matrix = np.zeros((self.size, self.size), dtype=int)
        self.add_new_tile(2)
        self.add_new_tile(2)
        self.score = 0
        self.update()



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



    def handle_events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif((not self.game_over and not self.win) and event.type == pygame.KEYDOWN):
                if event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_RIGHT:
                    self.move_right()
                elif event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_LEFT:
                    self.move_left()
            elif self.win:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    continue_rect, play_again_rect = self.board_ui.win()
                    if continue_rect.collidepoint(event.pos):
                        self.win = False
                    elif play_again_rect.collidepoint(event.pos):
                        self.init_game()
            elif(self.game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                play_again_rect = self.play_again_button
                if play_again_rect.collidepoint(event.pos):
                    self.init_game()
            elif(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                repeat_rect = self.menu_ui.draw_menu()
                if repeat_rect.collidepoint(event.pos):
                    self.init_game()



    def move_up(self):
        self.matrix = np.rot90(self.matrix, k=1) 
        self.stack()
        self.combine()
        self.stack()  
        self.matrix = np.rot90(self.matrix, k=-1)
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self.add_new_tile()
            self.old_matrix = self.matrix
        return self.check_game_over()


    def move_right(self):
        self.matrix = np.rot90(self.matrix, k=2)
        self.stack()
        self.combine()
        self.stack()
        self.matrix = np.rot90(self.matrix, k=2)
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self.add_new_tile()
            self.old_matrix = self.matrix
        return self.check_game_over()


    def move_down(self):
        self.matrix = np.rot90(self.matrix, k=-1)  
        self.stack()
        self.combine()
        self.stack()  
        self.matrix = np.rot90(self.matrix, k=1)   
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self.add_new_tile()
            self.old_matrix = self.matrix
        return self.check_game_over()


    def move_left(self):
        self.stack()
        self.combine()
        self.stack()
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self.add_new_tile()
            self.old_matrix = self.matrix
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
        if(not self.first_time_won and any(4 in row for row in self.matrix)):
            self.board_ui.update(matrix = self.matrix)
            self.continue_button, self.play_again_button = self.board_ui.win(paint_background = True)
            self.win = True
            self.first_time_won = True
            return False
        elif(not self.moves_exists()):
            self.game_over = True
            self.board_ui.update(matrix = self.matrix)
            self.play_again_button = self.board_ui.game_over()
            return True


    def run(self):
        while True:
            self.handle_events()
            if(self.score > self.high_score):
                self.high_score = self.score
            self.update()



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


    def update(self):
        self.menu_ui.update(self.score, self.high_score)
        if(not self.game_over and not self.win):
            self.board_ui.update(matrix = self.matrix)
        pygame.display.flip()
        self.clock.tick(FPS)



if __name__ == "__main__":
    game = Game(size=2)
    game.run()