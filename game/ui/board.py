import pygame
from settings import *


class Board:
    def __init__(self, screen, size: int = 4):
        self.size = size
        self.spacing = max(2, 12 - self.size)
        self.block_size = (GRID_SIZE - (self.size + 1) * self.spacing) / self.size
        self.display_surface = screen
        self.rect_outer = pygame.Rect(43, 98, GRID_SIZE + 4, GRID_SIZE + 4)  # Ajustado rectángulo exterior
        self.border_radius = 8  # Ajusta el radio según sea necesario
        self.rect_outer_color = pygame.Color(GRID_COLOR)

    def _draw_grid(self, matrix):
        # Dibujar el fondo del for con esquinas redondeadas
        pygame.draw.rect(self.display_surface, GRID_COLOR, self.rect_outer, border_radius=self.border_radius)

        # Dibujar cuadrados con colores y números por fila con separación
        for row in range(self.size):
            y = 100 + self.spacing + row * (self.block_size + self.spacing)

            for col in range(self.size):
                x = 45 + self.spacing + col * (self.block_size + self.spacing)
                square_rect = pygame.Rect(x, y, self.block_size, self.block_size)
                
                value = matrix[row][col]
                tile_color = CARD[value]["tile_color"]
                label_color = CARD[value]["label_color"]

                # Calcular el tamaño de la fuente basado en self.size
                base_font_size = CARD[value]["font"][1]
                font_size = int(base_font_size - (base_font_size * 0.15 * (self.size - 4)))  
                font = pygame.font.SysFont(CARD[value]["font"][0], font_size, CARD[value]["font"][2])

                pygame.draw.rect(self.display_surface, tile_color, square_rect, border_radius=self.border_radius)

                if value != 0:  # Si el valor es 0, no se muestra ningún número
                    label = font.render(str(value), True, label_color)
                    label_rect = label.get_rect(center=square_rect.center)
                    self.display_surface.blit(label, label_rect)

    def update(self, matrix):
        self._draw_grid(matrix=matrix)
