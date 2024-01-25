from ai.ai_settings import *
import numpy as np
from icecream import ic
import copy
import multiprocessing as mp
from ai.expectiminimax.functions import *
from ai.mcts.functions import check_game_over
import cma


class Expectiminimax:
    def __init__(self, size):
        self.size = size
        
        self.position_multipliers = [
            [pow(2, size * i + j) if i % 2 == 0 else pow(2, size * (i + 1) - 1 - j) for j in range(size)]
            for i in range(size)
        ]



    def count_open_squares(self, board):
        return np.count_nonzero(board == 0)

    def large_values_on_edge_bonus(self, board):
        bonus = 0
        for i in range(self.size):
            for j in range(self.size):
                bonus += board[i][j] * self.position_multipliers[i][j]
        return bonus

    def non_monotonic_penalty(self, board):
        penalty = 0
        for row in board:
            penalty += np.sum(np.diff(row[row > 0]) < 0)
        for col in board.T:
            penalty += np.sum(np.diff(col[col > 0]) < 0)
        return penalty

    def potential_merges(self, board):
        merges = 0
        merges += np.sum(board[:, :-1] == board[:, 1:])
        merges += np.sum(board[:-1, :] == board[1:, :])
        return merges

    def calculate_heuristic_value(self, board):
        score = 0
        score += 2**8 * self.count_open_squares(board) 
        score += self.large_values_on_edge_bonus(board) 
        score -= 2**4 * self.non_monotonic_penalty(board) 
        score += 2**6 * self.potential_merges(board) 
        return score


        # def snakeHeuristic(self, board):
        #     h = 0
        #     for i in range(self.size):
        #         for j in range(self.size):
        #             h += board[i][j] * self.position_multipliers[i][j]
        #     return h


    def getNextBestMoveExpectiminimax(self, board, pool, depth=2):
        bestScore = -INF
        bestNextMove = "move_up"
        results = []

        for move_name, move_function in possible_moves.items():
            sim_board = copy.deepcopy(board)
            sim_board, move_made, score = move_function(sim_board)
            if not move_made:
                continue
            results.append(pool.apply_async(self.expectiminimax, (sim_board, depth, move_name)))

        results = [res.get() for res in results]

        for res in results:
            if res[0] >= bestScore:
                bestScore = res[0]
                bestNextMove = res[1]

        return bestNextMove


    def expectiminimax(self, board, depth, move_name=None):
        if check_game_over(board):
            return -INF, move_name
        elif depth < 0:
            return self.calculate_heuristic_value(board), move_name
        
        a = 0
        if depth != int(depth):
            # Player's turn, pick max
            a = -INF
            for next_move_name, next_move_function in possible_moves.items():
                sim_board = copy.deepcopy(board)
                sim_board, move_made, score = next_move_function(sim_board)
                if move_made:
                    res = self.expectiminimax(sim_board, depth - 0.5, next_move_function)[0]
                    if res > a:
                        a = res
        elif depth == int(depth):
            # Nature's turn, calc average
            a = 0
            openTiles = getOpenTiles(board)
            for addTileLoc in openTiles:
                board = add_new_tile(matrix=board, number=2, pos=addTileLoc)
                a += 1.0 / len(openTiles) * self.expectiminimax(board, depth - 0.5, move_name)[0]
                board = add_new_tile(matrix=board, pos=addTileLoc)
        return a, move_name


