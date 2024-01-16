import pygame

class Dropdown:
    def __init__(self, screen):
        self.options = ["Option 1", "Option 2", "Option 3"]
        self.position = (50, 50)
        self.screen = screen
        self.size = (200, 40)
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)
        self.selected_index = 0
        self.expanded = False

        # Configuración interna
        self.background_color = (200, 200, 200)
        self.text_color = (0, 0, 0)
        self.arrow_color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, (self.position, self.size))
        pygame.draw.polygon(screen, self.arrow_color, [
            (self.position[0] + self.size[0] - 20, self.position[1] + self.size[1] // 2 - 5),
            (self.position[0] + self.size[0] - 10, self.position[1] + self.size[1] // 2 - 5),
            (self.position[0] + self.size[0] - 15, self.position[1] + self.size[1] // 2 + 5)
        ])

        selected_option_text = self.font.render(self.options[self.selected_index], True, self.text_color)
        selected_option_rect = selected_option_text.get_rect(center=(
            self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))

        screen.blit(selected_option_text, selected_option_rect)

        if self.expanded:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(
                    self.position[0], self.position[1] + (i + 1) * self.size[1], self.size[0], self.size[1])
                option_text = self.font.render(option, True, self.text_color)
                option_text_rect = option_text.get_rect(center=(
                    option_rect[0] + option_rect[2] // 2, option_rect[1] + option_rect[3] // 2))
                pygame.draw.rect(screen, self.background_color, option_rect)
                screen.blit(option_text, option_text_rect)

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


# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((400, 300))
#     clock = pygame.time.Clock()
    
#     dropdown = Dropdown(screen)

#     running = True
#     while running:
#         screen.fill((255, 255, 255))

#         dropdown.draw(screen)

#         pygame.display.flip()
#         clock.tick(60)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if dropdown.position[0] <= event.pos[0] <= dropdown.position[0] + dropdown.size[0] and \
#                     dropdown.position[1] <= event.pos[1] <= dropdown.position[1] + dropdown.size[1]:
#                     dropdown.toggle()
#                 elif dropdown.select_option(event.pos):
#                     print(f"Selected Option: {dropdown.options[dropdown.selected_index]}")
