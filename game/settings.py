import pygame
from os.path import join
import os


# Display Size
PADDING = 20
GRID_SIZE = 500 #WIDTH = HEIGHT
WINDOW_WIDTH = GRID_SIZE + 2*PADDING + 40
WINDOW_HEIGHT = GRID_SIZE + 3*PADDING + 130
MENU_WIDTH = 110
MENU_HEIGHT = 50

POS_X_BOARD = 43
POS_Y_BOARD = 155

POS_X_MENU = WINDOW_WIDTH - (1.3*MENU_WIDTH)
POS_Y_MENU = 35

# Time config
FPS = 60

# Fonts
FONT_LIGHT = join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Light.ttf')
FONT_MEDIUM = join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Medium.ttf')
FONT_REGULAR = join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Regular.ttf')
FONT_BOLD = join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Bold.ttf')



# Colors
BACKGROUND_COLOR = "#fbf8ef"
GRID_COLOR = "#BBADA0"
EMPTY_COLOR = "#D6CDC4"
BUTTON_COLOR = "#8f7a66"
SCORE_BOX_COLOR = "#bbada0"
TEXT_COLOR = "#eee4da" 
NEW_GAME_TEXT = "#f9f6f2"
TITLE_COLOR = "#776e65"
WHITE = "#FFFFFF"
START_BUTTON_COLOR = "#ff775c"
CHOSEN_OPTION_COLOR = "#ff775c"  
UNCHOSEN_OPTION_COLOR = "#776e65"  




# Card Settings
FONT_STYLE = "bold"
CARD_BASE_FONT_SIZE = 80

CARD = {
    0: {"tile_color": EMPTY_COLOR, "label_color": EMPTY_COLOR, "font": (FONT_REGULAR, "bold")},
    2: {"tile_color": "#eee4da", "label_color": "#776e65", "font": (FONT_REGULAR,"bold")},
    4: {"tile_color": "#eee1c9", "label_color": "#695c57", "font": (FONT_REGULAR, "bold")},
    8: {"tile_color": "#f3b27a", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    16: {"tile_color": "#f69664", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    32: {"tile_color": "#f77c5f", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    64: {"tile_color": "#f75f3b", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    128: {"tile_color": "#edd073", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    256: {"tile_color": "#edcc62", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    512: {"tile_color": "#edc950", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    1024: {"tile_color": "#edc53f", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    2048: {"tile_color": "#edc22e", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
    4096: {"tile_color": "#3c3a33", "label_color": "#f9f6f2", "font": (FONT_REGULAR, "bold")},
}

SPAWN_TWO_PROBABILITY = 0.9


# Board size options
BOARD = {
    0: 3,
    1: 4,
    2: 5,
    3: 6,
    4: 8
}

# User input settings
move_functions = {
        pygame.K_UP: "_move_up",
        pygame.K_RIGHT: "_move_right",
        pygame.K_DOWN: "_move_down",
        pygame.K_LEFT: "_move_left",
}