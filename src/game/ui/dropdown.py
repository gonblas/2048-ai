import pygame

from game.settings import *

class Dropdown:
    def __init__(self, screen):
        self.options = ["Tiny (3x3)", "Classic (4x4)", "Big (5x5)", "Bigger (6x6)", "Huge (8x8)"]
        self.position = (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT- 400)
        self.screen = screen
        self.size = (240, 40)
        self.font = pygame.font.Font(FONT_MEDIUM, 20)
        self.selected_index = 1
        self.expanded = False

        # Configuración interna
        self.arrow_color = WHITE
    
    
    def draw(self):
        pygame.draw.rect(self.screen, BUTTON_COLOR, (self.position, self.size))
        pygame.draw.polygon(self.screen, self.arrow_color, [
            (self.position[0] + self.size[0] - 20, self.position[1] + self.size[1] // 2 - 5),
            (self.position[0] + self.size[0] - 10, self.position[1] + self.size[1] // 2 - 5),
            (self.position[0] + self.size[0] - 15, self.position[1] + self.size[1] // 2 + 5)
        ])

        selected_option_text = self.font.render(self.options[self.selected_index], True, TEXT_COLOR)
        selected_option_rect = selected_option_text.get_rect(center=(
            self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))

        self.screen.blit(selected_option_text, selected_option_rect)

        if self.expanded:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(
                    self.position[0], self.position[1] + (i + 1) * self.size[1], self.size[0], self.size[1])
                option_text = self.font.render(option, True, TEXT_COLOR)
                option_text_rect = option_text.get_rect(center=(
                    option_rect[0] + option_rect[2] // 2, option_rect[1] + option_rect[3] // 2))
                pygame.draw.rect(self.screen, BUTTON_COLOR, option_rect)
                self.screen.blit(option_text, option_text_rect)



    def toggle(self):
        self.expanded = not self.expanded


    def select_option(self, mouse_pos):
        if not self.expanded:
            return False


        for i, option in enumerate(self.options):
            option_rect = pygame.Rect(
                self.position[0], self.position[1] + (i + 1) * self.size[1], self.size[0], self.size[1])
            if option_rect.collidepoint(mouse_pos):
                self.selected_index = i
                self.expanded = False
                return True
        return False
