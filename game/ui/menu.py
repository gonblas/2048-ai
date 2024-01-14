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
        border_radius = 10  # Ajusta según sea necesario
        padding = 15  # Espacio entre los rectángulos
    
        
        score_rect = pygame.Rect(POS_X_MENU - (MENU_WIDTH + padding), POS_Y_MENU, MENU_WIDTH, MENU_HEIGHT)

        
        high_score_rect = pygame.Rect(POS_X_MENU , POS_Y_MENU, MENU_WIDTH, MENU_HEIGHT)

        
        additional_rect = pygame.Rect(POS_X_MENU  + (MENU_WIDTH + padding), POS_Y_MENU, MENU_HEIGHT, MENU_HEIGHT)

        
        pygame.draw.rect(self.screen, BUTTON_COLOR, score_rect, border_radius=border_radius)
        pygame.draw.rect(self.screen, BUTTON_COLOR, high_score_rect, border_radius=border_radius)
        pygame.draw.rect(self.screen, BUTTON_COLOR, additional_rect, border_radius=border_radius)


        font = pygame.font.Font(None, 20) #CAMBIAR LUEGO POR ALGO DE SETTINGS

        score_text = font.render(f"Score:", True, TEXT_COLOR)
        high_score_text = font.render(f"High Score:", True, TEXT_COLOR)
        additional_text = font.render("LOGO", True, TEXT_COLOR)

        score_text_rect = score_text.get_rect(center=(score_rect.centerx, score_rect.centery - 10))  
        high_score_text_rect = high_score_text.get_rect(center=(high_score_rect.centerx, high_score_rect.centery - 10))  
        additional_text_rect = additional_text.get_rect(center=(additional_rect.centerx, additional_rect.centery))

        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(high_score_text, high_score_text_rect)
        self.screen.blit(additional_text, additional_text_rect)

        # Dibujar valores debajo de los textos
        score_value_text = font.render(str(self.score), True, TEXT_COLOR)
        high_score_value_text = font.render(str(self.high_score), True, TEXT_COLOR)

        score_value_text_rect = score_value_text.get_rect(center=(score_rect.centerx, score_rect.centery + 10))  
        high_score_value_text_rect = high_score_value_text.get_rect(center=(high_score_rect.centerx, high_score_rect.centery + 10))  

        self.screen.blit(score_value_text, score_value_text_rect)
        self.screen.blit(high_score_value_text, high_score_value_text_rect)



    def update(self, new_score, new_high_score):
        self.score = new_score
        self.high_score = new_high_score
        self.draw_menu()
        pygame.display.flip()
