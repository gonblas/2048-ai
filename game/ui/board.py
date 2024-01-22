import pygame

from game.settings import *


blur_surface_win = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
blur_surface_win.fill((255, 255, 0, 50))  # Ajusta el color y la opacidad según sea necesario
blur_surface_win = pygame.transform.smoothscale(blur_surface_win, (GRID_SIZE+4, GRID_SIZE+4))


class Board:
    def __init__(self, screen, size: int = 4):
        self.size = size
        self.spacing = max(2, 12 - self.size)
        self.block_size = (GRID_SIZE - (self.size + 1) * self.spacing) / self.size
        self.screen = screen
        self.rect_outer = pygame.Rect(POS_X_BOARD, POS_Y_BOARD, GRID_SIZE + 4, GRID_SIZE + 4)  # Ajustado rectángulo exterior
        self.border_radius = 3  # Ajusta el radio según sea necesario
        self.rect_outer_color = pygame.Color(GRID_COLOR)


    def _draw_grid(self, matrix):
        # Dibujar el fondo del for con esquinas redondeadas
        pygame.draw.rect(self.screen, GRID_COLOR, self.rect_outer, border_radius=6)

        # Dibujar cuadrados con colores y números por fila con separación
        for row in range(self.size):
            y = (POS_Y_BOARD + 2) + self.spacing + row * (self.block_size + self.spacing)
            for col in range(self.size):
                x = 45 + self.spacing + col * (self.block_size + self.spacing)
                square_rect = pygame.Rect(x, y, self.block_size, self.block_size)
                value = matrix[row][col]
                
                #Set colors
                if value >= 4096:
                    tile_color = CARD[4096]["tile_color"]
                    label_color = CARD[4096]["label_color"]
                else:
                    tile_color = CARD[value]["tile_color"]
                    label_color = CARD[value]["label_color"]
                
                #Set font size
                digit_count = len(str(value))
                font_size = CARD_BASE_FONT_SIZE - 8 * (digit_count - 1)
                font_size = int(font_size - (font_size * 0.14 * (self.size - 4)))
                font = pygame.font.SysFont(FONT_BOLD, font_size, FONT_STYLE)
                
                
                pygame.draw.rect(self.screen, tile_color, square_rect, border_radius=self.border_radius)
                
                if value != 0:  # Si el valor es 0, no se muestra ningún número
                    label = font.render(str(value), True, label_color)
                    label_rect = label.get_rect(center=square_rect.center)
                    self.screen.blit(label, label_rect)



    def game_over(self):
        blur_surface = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
        blur_surface.fill((238, 228, 218, 73))  # Ajusta el color y la opacidad según sea necesario
        blur_surface = pygame.transform.smoothscale(blur_surface, (GRID_SIZE+4, GRID_SIZE+4))

        # Dibuja la superficie difuminada sobre el área del tablero
        self.screen.blit(blur_surface, (POS_X_BOARD,POS_Y_BOARD))
        
        #Game Over Title
        font = pygame.font.Font(FONT_BOLD, 60)
        title_text = font.render("Game Over!", True, TITLE_COLOR)
        title_rect = title_text.get_rect(topleft=(WINDOW_WIDTH/2-155, WINDOW_HEIGHT/2))
        self.screen.blit(title_text, title_rect)

        # Dibuja el botón de repetir
        font = pygame.font.Font(FONT_MEDIUM, 20) 
        repeat_rect = pygame.Rect(WINDOW_WIDTH/2-85, WINDOW_HEIGHT/2 + 140 , MENU_WIDTH*2, MENU_HEIGHT)
        pygame.draw.rect(self.screen, BUTTON_COLOR, repeat_rect, border_radius=3)
        repeat_text = font.render("Try Again", True, NEW_GAME_TEXT)
        repeat_text_rect = repeat_text.get_rect(center=(repeat_rect.centerx, repeat_rect.centery))
        self.screen.blit(repeat_text, repeat_text_rect)

        return repeat_rect
    
    
    def win(self, paint_background: bool = False):
        if(paint_background):
            self.screen.blit(blur_surface_win, (POS_X_BOARD,POS_Y_BOARD))
        
        #Game Over Title
        font = pygame.font.Font(FONT_BOLD, 60)
        title_text = font.render("You Won!", True, WHITE)
        title_rect = title_text.get_rect(topleft=(WINDOW_WIDTH/2-125, WINDOW_HEIGHT/2))
        self.screen.blit(title_text, title_rect)

        # Dibuja el botón de repetir
        font = pygame.font.Font(FONT_MEDIUM, 20) 
        continue_rect = pygame.Rect(WINDOW_WIDTH/2+25, WINDOW_HEIGHT/2 + 140 , MENU_WIDTH + 50, MENU_HEIGHT)
        pygame.draw.rect(self.screen, BUTTON_COLOR, continue_rect, border_radius=3)
        continue_text = font.render("Keep Going", True, NEW_GAME_TEXT)
        continue_text_rect = continue_text.get_rect(center=(continue_rect.centerx, continue_rect.centery))
        self.screen.blit(continue_text, continue_text_rect)
        
        repeat_rect = pygame.Rect(WINDOW_WIDTH/2-155, WINDOW_HEIGHT/2 + 140 , MENU_WIDTH + 50, MENU_HEIGHT)
        pygame.draw.rect(self.screen, BUTTON_COLOR, repeat_rect, border_radius=3)
        repeat_text = font.render("Try Again", True, NEW_GAME_TEXT)
        repeat_text_rect = repeat_text.get_rect(center=(repeat_rect.centerx, repeat_rect.centery))
        self.screen.blit(repeat_text, repeat_text_rect)

        return continue_rect, repeat_rect



    def update(self, matrix):
        self._draw_grid(matrix=matrix)
