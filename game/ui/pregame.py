import pygame
from icecream import ic
from game.ui.dropdown import Dropdown
from game.ui.switch import Switch
from game.settings import *


class Pregame:
    def __init__(self, screen, clock):
        self.size = 4
        self.screen = screen
        self.clock = clock
        self.switch = Switch(self.screen, (WINDOW_WIDTH/2-80, WINDOW_HEIGHT/2 + 255), (150, 40), ["User", "AI"])
        self.waiting_for_start = True
        self.user_mode = True
        self.dropdown = Dropdown(self.screen)


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if (self.start_rect.collidepoint(event.pos)):
                    self.waiting_for_start = False
                elif self.switch.collidepoint(event.pos):
                    self.user_mode = (self.switch.selected_option == 0)
                elif self.dropdown.position[0] <= event.pos[0] <= self.dropdown.position[0] + self.dropdown.size[0] and \
                    self.dropdown.position[1] <= event.pos[1] <= self.dropdown.position[1] + self.dropdown.size[1]:
                    self.dropdown.toggle()
                elif self.dropdown.select_option(event.pos):
                    self.size = BOARD[self.dropdown.selected_index]



    def _draw_elements(self):
        pygame.draw.rect(self.screen, pygame.Color(BACKGROUND_COLOR), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        
        font = pygame.font.Font(FONT_BOLD, 90)  
        self.title_text = font.render("2048", True, TITLE_COLOR)  
        title_rect = self.title_text.get_rect(topleft=(WINDOW_WIDTH/2 - 100, 50))
        self.screen.blit(self.title_text, title_rect)
        
        
        #Start Game
        font = pygame.font.Font(FONT_MEDIUM, 20)
        self.start_rect = pygame.Rect(WINDOW_WIDTH/2-143, WINDOW_HEIGHT/2 + 190, MENU_WIDTH*2 + 100, MENU_HEIGHT)
        pygame.draw.rect(self.screen, START_BUTTON_COLOR, self.start_rect, border_radius=3)
        start_text = font.render("Start Game", True, NEW_GAME_TEXT)
        start_text_rect = start_text.get_rect(center=(self.start_rect.centerx, self.start_rect.centery))
        self.screen.blit(start_text, start_text_rect)
        
        # Size 
        font = pygame.font.Font(FONT_MEDIUM, 30)  
        board_text = font.render("Board Size", True, BUTTON_COLOR)  
        board_rect = board_text.get_rect(topleft=(WINDOW_WIDTH/2 - 78, 220))
        self.screen.blit(board_text, board_rect)
        
        self.dropdown.draw()
        
        # User mode vs AI mode
        self.switch.draw()




    def run(self) -> int:
        while self.waiting_for_start:
            self._handle_events()
            self._draw_elements()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.draw.rect(self.screen, pygame.Color(BACKGROUND_COLOR), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        return self.user_mode, self.size



