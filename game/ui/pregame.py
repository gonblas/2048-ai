import pygame
from settings import *

class Pregame:
    def __init__(self, screen, clock):
        self.size = 3
        self.screen = screen
        self.clock = clock
        self.waiting_for_start = True


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.waiting_for_start = False


    def _draw_elements(self):
        pygame.draw.rect(self.screen, pygame.Color(BACKGROUND_COLOR), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        self._add_title()
        



    def _add_title(self):
        font = pygame.font.Font(FONT_BOLD, 90)  
        title_text = font.render("2048", True, TITLE_COLOR)  
        title_rect = title_text.get_rect(topleft=(WINDOW_WIDTH/2 - 100, 50))
        self.screen.blit(title_text, title_rect)
        
        #Start Game
        font = pygame.font.Font(FONT_MEDIUM, 20) 
        repeat_rect = pygame.Rect(WINDOW_WIDTH/2-155, WINDOW_HEIGHT/2 + 160, MENU_WIDTH*2 + 140, MENU_HEIGHT)
        pygame.draw.rect(self.screen, START_BUTTON_COLOR, repeat_rect, border_radius=3)
        repeat_text = font.render("Start Game", True, NEW_GAME_TEXT)
        repeat_text_rect = repeat_text.get_rect(center=(repeat_rect.centerx, repeat_rect.centery))
        self.screen.blit(repeat_text, repeat_text_rect)
        
        


    def run(self) -> int:
        while self.waiting_for_start:
            self._handle_events()
            self._draw_elements()
            pygame.display.flip()
            self.clock.tick(30)  