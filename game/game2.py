import pygame
from settings import *
from ui.board import *
from ui.menu import *
import numpy as np


class Game:
    def __init__(self, size: int = 4):
        pygame.init()

        # Init data
        self.size = size
        self.high_score = 0 
        
        self.matrix = np.zeros((self.size, self.size), dtype=int)

        # Pygame config
        pygame.display.set_caption("2048")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(pygame.Color(BACKGROUND_COLOR))
        
        #Title: Agregar titulo
        self.add_title()

        # UI and pygame
        pygame.init()
        self.menu_ui = Menu(self.screen)
        self.menu_ui.update(10, 100)
        self.board_ui = Board(size = self.size, screen = self.screen)
        self.board_ui.update(matrix = self.matrix)
        
        self.sprites = pygame.sprite.Group()



    def add_title(self):
        font = pygame.font.Font(None, 45)  
        title_text = font.render("2048", True, GRID_COLOR)  
        title_rect = title_text.get_rect(topleft=(45, 40))
        self.screen.blit(title_text, title_rect)



    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Aquí puedes agregar lógica para actualizar tu juego

            # Actualiza la pantalla
            pygame.display.flip()

            # Configura la velocidad de actualización
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()