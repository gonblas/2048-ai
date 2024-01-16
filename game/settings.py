#SIN USO POR EL MOMENTO
from turtle import window_height
from os.path import join
import os


# Display Size
PADDING = 20
GRID_SIZE = 500 #WIDTH = HEIGHT
WINDOW_WIDTH = GRID_SIZE + 2*PADDING + 40
WINDOW_HEIGHT = GRID_SIZE + 3*PADDING + 100
MENU_WIDTH = 90
MENU_HEIGHT = 45

POS_X_MENU = WINDOW_WIDTH - (1.4*MENU_WIDTH)
POS_Y_MENU = 35

# Time config
FPS = 60

# Fonts
FONT_LIGHT = os.path.join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Light.ttf')
FONT_MEDIUM = os.path.join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Medium.ttf')
FONT_REGULAR = os.path.join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Regular.ttf')
FONT_BOLD = os.path.join(os.getcwd(),'assets', 'fonts', 'Ubuntu-Bold.ttf')



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
CHOSEN_OPTION_COLOR = "#ff775c"  # Blue
UNCHOSEN_OPTION_COLOR = "#776e65"  # Black

# Card Settings

CARD = {
    0: {"tile_color": EMPTY_COLOR, "label_color": EMPTY_COLOR, "font": (FONT_REGULAR, 80, "bold")},
    2: {"tile_color": "#eee4da", "label_color": "#776e65", "font": (FONT_REGULAR, 80, "bold")},
    4: {"tile_color": "#f2e8cb", "label_color": "#695c57", "font": (FONT_REGULAR, 80, "bold")},
    8: {"tile_color": "#f5b682", "label_color": "#ffffff", "font": (FONT_REGULAR, 80, "bold")},
    16: {"tile_color": "#f29446", "label_color": "#ffffff", "font": (FONT_REGULAR, 75, "bold")},
    32: {"tile_color": "#ff775c", "label_color": "#ffffff", "font": (FONT_REGULAR, 75, "bold")},
    64: {"tile_color": "#e64c2e", "label_color": "#ffffff", "font": (FONT_REGULAR, 75, "bold")},
    128: {"tile_color": "#ede291", "label_color": "#ffffff", "font": (FONT_REGULAR, 70, "bold")},
    256: {"tile_color": "#fce130", "label_color": "#ffffff", "font": (FONT_REGULAR, 70, "bold")},
    512: {"tile_color": "#ffdb4a", "label_color": "#ffffff", "font": (FONT_REGULAR, 70, "bold")},
    1024: {"tile_color": "#f0b922", "label_color": "#ffffff", "font": (FONT_REGULAR, 65, "bold")},
    2048: {"tile_color": "#fad74d", "label_color": "#ffffff", "font": (FONT_REGULAR, 65, "bold")},
    4096: {"tile_color": "#000000", "label_color": "#ffffff", "font": (FONT_REGULAR, 65, "bold")},
    8192: {"tile_color": "#000000", "label_color": "#ffffff", "font": (FONT_REGULAR, 65, "bold")},
}


# Board size options

BOARD = {
    0: 3,
    1: 4,
    2: 5,
    3: 6,
    4: 8
}