#Deep Learning

BLOCK_SIZE = 20
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

INITIAL_EPSILON = 40
INITIAL_GAMMA = 1




#Monte Carlo Tree Search

NUMBER_OF_MOVES = 4
SAMPLE_COUNT = 50

SPM_SCALE_PARAM = 10
SL_SCALE_PARAM = 4
SEARCH_PARAM = 200





#Expectiminimax
from ai.expectiminimax.functions import *

possible_moves = {
    "move_up": move_up,
    "move_right": move_right,
    "move_down": move_down,
    "move_left": move_left,
}

INF = 2**64