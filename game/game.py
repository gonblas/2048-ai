import multiprocessing as mp
from icecream import ic
import numpy as np
import pygame
import random
import sys

from game.ui.pregame import Pregame
from game.ui.board import Board
from game.ui.menu import Menu
from game.settings import *
from ai.mcts_ai import MCTS_AI
from ai.expectiminimax.expectiminimax import *




class Game:
    def __init__(self):
        pygame.init()
        # Init data
        self.high_score = 0 
        
        # Pygame config
        pygame.display.set_caption("2048")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(pygame.Color(BACKGROUND_COLOR))
        
        # Pregame view
        self.reset()




    def reset(self):
        self.pregame = Pregame(self.screen, self.clock)
        self.user_mode, self.size = self.pregame.run()
        
        #Title
        self._add_title()
        
        # UI and pygame
        pygame.init()
        self.menu_ui = Menu(self.screen)
        self.board_ui = Board(size = self.size, screen = self.screen)
        
        # Init board and _run
        self._init_game()



    def _add_title(self):
        font = pygame.font.Font(FONT_BOLD, 80)  
        title_text = font.render("2048", True, TITLE_COLOR)  
        title_rect = title_text.get_rect(topleft=(45, 28))
        self.screen.blit(title_text, title_rect)
        return title_rect



    def _init_game(self):
        self.game_over = False
        self.win = False
        self.first_time_won = False
        self.matrix = np.zeros((self.size, self.size), dtype=int)
        self.old_matrix = np.zeros((self.size, self.size), dtype=int)
        self._add_new_tile(2)
        self._add_new_tile(256*2)
        self._add_new_tile(1024)
        self._add_new_tile(16384)
        self.score = 0
        self._update()
        if(self.user_mode):
            self._run_in_user_mode()
        else:
            # self.mcts = MCTS_AI(self.size)
            self.ai = Expectiminimax(self.size)
            self.pool = mp.Pool(processes=2)
            self.paused = False
            self._run_in_ai_mode()



    def _add_new_tile(self, number = None):
        if (number is None):
            number = np.random.choice([2, 4], p=[SPAWN_TWO_PROBABILITY, 1 - SPAWN_TWO_PROBABILITY])
        empty_cells = list(zip(*np.where(self.matrix == 0)))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row, col] = number

    def _stack(self):
        new_matrix = np.zeros((self.size, self.size), dtype=int)
        for x in range(self.size):
            fill_pos = 0
            for y in range(self.size):
                if(self.matrix[x, y] != 0):
                    new_matrix[x, fill_pos] = self.matrix[x, y]
                    fill_pos += 1
        self.matrix = new_matrix

    def _combine(self):
        for x in range(self.size):
            for y in range(self.size-1):
                if((self.matrix[x][y] != 0) and (self.matrix[x][y] == self.matrix[x][y+1])):
                    self.matrix[x][y] *= 2
                    self.matrix[x][y+1] = 0
                    self.score += self.matrix[x][y]

    def _handle_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            
            if self.win:
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    continue_rect, play_again_rect = self.board_ui.win()
                    if (continue_rect.collidepoint(event.pos) or not self.user_mode):
                        self.win = False
                    elif (play_again_rect.collidepoint(event.pos)):
                        self._init_game()
            
            elif self.game_over:
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    play_again_rect = self.play_again_button
                    if (play_again_rect.collidepoint(event.pos) or not self.user_mode):
                        self._init_game()
            
            elif self.user_mode and event.type == pygame.KEYDOWN:
                if event.key in move_functions:
                    self._move(move_functions[event.key])
            
            elif not self.user_mode and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.paused = not self.paused
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                title_rect = self._add_title()
                if title_rect.collidepoint(event.pos):
                    self.reset()
                repeat_rect = self.menu_ui._draw_menu()
                if repeat_rect.collidepoint(event.pos):
                    self._init_game()

    def _move(self, direction: str = None):
        if direction is None:
            return
        try:
            getattr(self, f"{direction}")()
        except KeyError:
            raise ValueError("Dirección de movimiento invalida.")

        if not np.array_equal(self.matrix, self.old_matrix):
            self._add_new_tile()
        else:
            return False
        return not self._check_game_over()

    def _move_up(self):
        self.matrix = np.rot90(self.matrix, k=1) 
        self._stack()
        self._combine()
        self._stack()  
        self.matrix = np.rot90(self.matrix, k=-1)
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self._add_new_tile()
            self.old_matrix = self.matrix
        else:
            return False
        return not self._check_game_over()

    def _move_right(self):
        self.matrix = np.rot90(self.matrix, k=2)
        self._stack()
        self._combine()
        self._stack()
        self.matrix = np.rot90(self.matrix, k=2)
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self._add_new_tile()
            self.old_matrix = self.matrix
        else:
            return False
        return not self._check_game_over()

    def _move_down(self):
        self.matrix = np.rot90(self.matrix, k=-1)  
        self._stack()
        self._combine()
        self._stack()  
        self.matrix = np.rot90(self.matrix, k=1)   
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self._add_new_tile()
            self.old_matrix = self.matrix
        else:
            return False
        return not self._check_game_over()

    def _move_left(self):
        self._stack()
        self._combine()
        self._stack()
        if(not np.array_equal(self.matrix, self.old_matrix)):
            self._add_new_tile()
            self.old_matrix = self.matrix
        else:
            return False
        return not self._check_game_over()

    def _moves_exists(self):
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

    def _check_game_over(self):
        if(not self.first_time_won and any(2048 in row for row in self.matrix)):
            self.board_ui.update(matrix = self.matrix)
            self.continue_button, self.play_again_button = self.board_ui.win(paint_background = True)
            self.win = True
            self.first_time_won = True
            return False
        elif(not self._moves_exists()):
            self.game_over = True
            self.board_ui.update(matrix = self.matrix)
            self.play_again_button = self.board_ui.game_over()
            return True

    def _run_in_user_mode(self):
        while True:
            self._handle_events()
            self._update()
    
    #MCTS
    # def _run_in_ai_mode(self):
    #     move_number = 0
    #     # wins = 0
    #     # game_overs = 0
    #     # win = False
    #     valid_game = True
    #     while True:
    #         if(self.paused):
    #             self._handle_events()
    #             continue
    #         move_number += 1
    #         number_of_simulations, search_length = self.mcts.get_search_params(move_number)
    #         self.matrix, valid_game, new_score = self.mcts.ai_move(self.matrix, number_of_simulations, search_length)
    #         if valid_game:
    #             self.score += new_score
    #             # if(2048 in self.matrix):
    #             #     win = True
    #             self._add_new_tile()
    #         else:
    #             # if(win):
    #             #     wins += 1
    #             # else:
    #             #     game_overs += 1
    #             # ic(wins)
    #             # ic(game_overs)
    #             win = False
    #             self._init_game()
    #         self._update()
    #         pygame.time.delay(100)
    #         self._handle_events()



    def _run_in_ai_mode(self):
        while True:
            if(self.paused):
                self._handle_events()
                continue
            
            bestNextMove = "_" + self.ai.getNextBestMoveExpectiminimax(self.matrix, self.pool, depth = 2)
            
            self._move(bestNextMove)
            self._update()
            if(self.game_over):
                self._init_game()
            self._handle_events()



    def _update(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            self.high_score = self.score
        self.menu_ui.update(self.score, self.high_score)
        if(not self.game_over and not self.win):
            self.board_ui.update(matrix = self.matrix)
        pygame.display.flip()
        self.clock.tick(FPS)