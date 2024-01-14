#SIN USO POR EL MOMENTO
from turtle import window_height
from os.path import join


SCORE_LABEL_FONT = ("Roboto Mono", 24)
SCORE_FONT = ("Roboto Mono", 36, "bold")
TITLE_FONT = ("Roboto Mono", 36, "bold")
GAME_OVER_FONT = ("Roboto Mono", 48, "bold")
GAME_OVER_FONT_COLOR = "#ffffff"
LABEL_FONT = ("Arimo", 40, "bold")

# Display Size
PADDING = 20
GRID_SIZE = 420 #WIDTH = HEIGHT
WINDOW_WIDTH = GRID_SIZE + 2*PADDING + 40
WINDOW_HEIGHT = GRID_SIZE + 3*PADDING + 55
MENU_WIDTH = 90
MENU_HEIGHT = 45


POS_X_MENU = WINDOW_WIDTH / 2 + MENU_WIDTH //2 + 10
POS_Y_MENU = 30


WHITE = (255, 255, 255)



# Colors
BACKGROUND_COLOR = "#fbf8ef"
GRID_COLOR = "#BBADA0"
EMPTY_COLOR = "#D6CDC4"
BUTTON_COLOR = "#bbada0"
WINNER_BG = "#ffcc00"
LOSER_BG = "#a39489"
TEXT_COLOR = "#fbf8ef"



# Card Settings

CARD = {
    0: {"tile_color": EMPTY_COLOR, "label_color": EMPTY_COLOR, "font": ("Roboto Mono", 45, "bold")},
    2: {"tile_color": "#eee4da", "label_color": "#695c57", "font": ("Roboto Mono", 45, "bold")},
    4: {"tile_color": "#f2e8cb", "label_color": "#695c57", "font": ("Roboto Mono", 45, "bold")},
    8: {"tile_color": "#f5b682", "label_color": "#ffffff", "font": ("Roboto Mono", 45, "bold")},
    16: {"tile_color": "#f29446", "label_color": "#ffffff", "font": ("Roboto Mono", 40, "bold")},
    32: {"tile_color": "#ff775c", "label_color": "#ffffff", "font": ("Roboto Mono", 40, "bold")},
    64: {"tile_color": "#e64c2e", "label_color": "#ffffff", "font": ("Roboto Mono", 40, "bold")},
    128: {"tile_color": "#ede291", "label_color": "#ffffff", "font": ("Roboto Mono", 30, "bold")},
    256: {"tile_color": "#fce130", "label_color": "#ffffff", "font": ("Roboto Mono", 35, "bold")},
    512: {"tile_color": "#ffdb4a", "label_color": "#ffffff", "font": ("Roboto Mono", 35, "bold")},
    1024: {"tile_color": "#f0b922", "label_color": "#ffffff", "font": ("Roboto Mono", 30, "bold")},
    2048: {"tile_color": "#fad74d", "label_color": "#ffffff", "font": ("Roboto Mono", 30, "bold")},
    4096: {"tile_color": "#000000", "label_color": "#ffffff", "font": ("Roboto Mono", 30, "bold")},
    8192: {"tile_color": "#000000", "label_color": "#ffffff", "font": ("Roboto Mono", 30, "bold")},
}