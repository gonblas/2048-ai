import numpy as np

from ai.ai_settings import *
from ai.mcts.functions import *


class MCTS_AI:
    def __init__(self, size):
        self.size = size



    def get_search_params(self, move_number):
        searches_per_move = SPM_SCALE_PARAM * (1+(move_number // SEARCH_PARAM))
        search_length = SL_SCALE_PARAM * (1+(move_number // SEARCH_PARAM))
        return searches_per_move, search_length




    def ai_move(self, board, searches_per_move, search_length):
        possible_moves = [move_left, move_up, move_down, move_right]
        values = np.zeros(NUMBER_OF_MOVES)
        for move_index in range(NUMBER_OF_MOVES):
            move_function =  possible_moves[move_index]
            board_with_first_move, move_made, move_score = move_function(board)
            if not move_made:
                continue
            values[move_index] += move_score
            board_with_first_move = add_new_tile(board_with_first_move)
            for _ in range(searches_per_move):
                move_number = 1
                search_board = np.copy(board_with_first_move)
                game_valid = True
                while game_valid and move_number < search_length:
                    search_board, game_valid, score = random_move(search_board)
                    if game_valid:
                        search_board = add_new_tile(search_board)
                        values[move_index] += score
                        move_number += 1
        best_move = possible_moves[np.argmax(values)]
        search_board, game_valid, score = best_move(board)
        return search_board, game_valid, score



