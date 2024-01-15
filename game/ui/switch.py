import pygame
import sys
from settings import *

class Switch:
    def __init__(self):
        self.selected_option = 0
        self.border_radius = 10

    def switch_state(self):
        self.selected_option = 1 - self.selected_option

    def is_left_selected(self):
        return self.selected_option == 0

    def draw(self, surface, rect_position, rect_size, padding, options, text_color):
        # Dibuja el interruptor (switch)
        switch_rect = pygame.Rect(rect_position, rect_size)
        pygame.draw.rect(surface, pygame.Color(SWITCH_COLOR), switch_rect, border_radius=self.border_radius)

        # Limita el ancho total del rectángulo a la mitad del ancho disponible
        max_rect_width = rect_size[0] // 2
        rect_width = min(max_rect_width, switch_rect.width)

        # Ajusta la escala del tamaño del texto en relación con el ancho del rectángulo
        text_scale = rect_width / max_rect_width

        # Dibuja la mitad izquierda o derecha del rectángulo de fondo
        background_rect = switch_rect.copy()
        background_rect.width = rect_width  # Mitad izquierda o derecha
        if self.selected_option == 1:
            background_rect.left += switch_rect.width - rect_width  # Mover la mitad derecha al lugar correcto
        self.draw_rect(surface, pygame.Color(SELECTED_COLOR), background_rect)

        # Dibuja el texto de las opciones centrado en su respectiva área
        font_size = int(22 * text_scale)
        font = pygame.font.Font(FONT_MEDIUM, font_size)

        total_width = sum([font.size(option)[0] for option in options]) + (len(options) - 1) 
        x = switch_rect.centerx - total_width / 2 
        y = switch_rect.centery - font.size(options[0])[1] / 2

        for option in options:
            text = font.render(option, True, text_color)
            text_rect = text.get_rect()

            # Alinea el centro del texto con el centro del rectángulo pequeño correspondiente
            text_rect.center = (background_rect.centerx, switch_rect.centery)

            surface.blit(text, text_rect)

            # Actualiza la posición para la siguiente opción
            background_rect.left += text_rect.width + padding

    def draw_rect(self, surface, color, rect):
        """
        Dibuja un rectángulo con bordes redondeados.
        """
        pygame.draw.rect(surface, color, rect, border_radius=self.border_radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Interruptor (Switch)")

    switch = Switch()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    switch.switch_state()

        switch.draw(screen, (300, 250), (400, 100), 80, ["Opción A", "Opción B"], TEXT_COLOR)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
