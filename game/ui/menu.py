import pygame
from pygame.locals import *
from settings import *


class Menu:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.score = 0
        self.high_score = 0

        # Cargar imágenes si es necesario
        # self.img = pygame.image.load("ruta_de_la_imagen.png")


    def draw_menu(self):
        border_radius = 3  # Ajusta según sea necesario
        padding = 8  # Espacio entre los rectángulos
        
        score_rect = pygame.Rect(POS_X_MENU - (MENU_WIDTH + padding), POS_Y_MENU*2+padding, MENU_WIDTH, MENU_HEIGHT)
        
        high_score_rect = pygame.Rect(POS_X_MENU , POS_Y_MENU*2+padding , MENU_WIDTH, MENU_HEIGHT)
        
        repeat_rect = pygame.Rect(POS_X_MENU - (MENU_WIDTH + padding), POS_Y_MENU - padding/2, MENU_WIDTH*2 + padding, MENU_HEIGHT-padding/2)

        pygame.draw.rect(self.screen, SCORE_BOX_COLOR, score_rect, border_radius=border_radius)
        pygame.draw.rect(self.screen, SCORE_BOX_COLOR, high_score_rect, border_radius=border_radius)
        pygame.draw.rect(self.screen, BUTTON_COLOR, repeat_rect, border_radius=border_radius)

        font1 = pygame.font.Font(FONT_MEDIUM, 14) 
        font2 = pygame.font.Font(FONT_MEDIUM, 20) 

        score_text = font1.render(f"SCORE", True, TEXT_COLOR)
        high_score_text = font1.render(f"HIGH SCORE", True, TEXT_COLOR)
        repeat_text = font2.render("New Game", True, NEW_GAME_TEXT)

        score_text_rect = score_text.get_rect(center=(score_rect.centerx, score_rect.centery - 10))  
        high_score_text_rect = high_score_text.get_rect(center=(high_score_rect.centerx, high_score_rect.centery - 10))  
        repeat_text_rect = repeat_text.get_rect(center=(repeat_rect.centerx, repeat_rect.centery))

        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(high_score_text, high_score_text_rect)
        self.screen.blit(repeat_text, repeat_text_rect)

        # Dibujar valores debajo de los textos
        score_value_text = font2.render(str(self.score), True, WHITE)
        high_score_value_text = font2.render(str(self.high_score), True, WHITE)

        score_value_text_rect = score_value_text.get_rect(center=(score_rect.centerx, score_rect.centery + 10))  
        high_score_value_text_rect = high_score_value_text.get_rect(center=(high_score_rect.centerx, high_score_rect.centery + 10))  

        self.screen.blit(score_value_text, score_value_text_rect)
        self.screen.blit(high_score_value_text, high_score_value_text_rect)
        
        return repeat_rect


    def update(self, new_score, new_high_score):
        repeat_button = self.score = new_score
        self.high_score = new_high_score
        self.draw_menu()
        pygame.display.flip()
        return repeat_button
