import numpy as np
from game.settings import *
import random
from icecream import ic

def stack(matrix):
    size = matrix.shape[0]
    new_matrix = np.zeros((size, size), dtype=int)
    done = False
    
    for x in range(size):
        fill_pos = 0
        for y in range(size):
            if matrix[x, y] != 0:
                new_matrix[x, fill_pos] = matrix[x, y]
                fill_pos += 1
    
    done = not np.array_equal(matrix, new_matrix)
    return new_matrix, done


def combine(matrix):
    size = matrix.shape[0]
    done = False
    score = 0
    
    for x in range(size):
        for y in range(size-1):
            if matrix[x][y] != 0 and matrix[x][y] == matrix[x][y+1]:
                matrix[x][y] *= 2
                matrix[x][y+1] = 0
                score += matrix[x][y]
                done = True
    return matrix, done, score



def move_up(matrix):
    matrix = np.rot90(matrix, k=1) 
    matrix, has_stacked = stack(matrix)
    matrix, has_combined, score = combine(matrix)
    matrix, _ = stack(matrix)  
    matrix = np.rot90(matrix, k=-1)
    move_made = has_stacked or has_combined
    return matrix, move_made, score



def move_right(matrix):
    matrix = np.rot90(matrix, k=2)
    matrix, has_stacked = stack(matrix)
    matrix, has_combined, score = combine(matrix)
    matrix, _ = stack(matrix)
    matrix = np.rot90(matrix, k=2)
    move_made = has_stacked or has_combined
    return matrix, move_made, score



def move_down(matrix):
    matrix = np.rot90(matrix, k=-1)
    matrix, has_stacked = stack(matrix)
    matrix, has_combined, score = combine(matrix)
    matrix, _ = stack(matrix)
    matrix = np.rot90(matrix, k=1)   
    move_made = has_stacked or has_combined
    return matrix, move_made, score



def move_left(matrix):
    matrix, has_stacked = stack(matrix)
    matrix, has_combined, score = combine(matrix)
    matrix, _ = stack(matrix)
    move_made = has_stacked or has_combined
    return matrix, move_made, score



def check_game_over(matrix):
    size = matrix.shape[0]
    for row in range(size):
        for col in range(size):
            if matrix[row, col] == 0:
                return False 
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (
                    0 <= new_row < size
                    and 0 <= new_col < size
                    and matrix[row, col] == matrix[new_row, new_col]
                ):
                    return False
    return True



def random_move(board):
    move_made = False
    move_order = [move_right, move_up, move_down, move_left]
    while not move_made and len(move_order) > 0:
        move_index = np.random.randint(0, len(move_order))
        move = move_order[move_index]
        board, move_made, score  = move(board)
        if move_made:
            return board, True, score
        move_order.pop(move_index)
    return board, False, score


def check_game_over(self, matrix):
    size = matrix.shape[0]
    for row in range(size):
        for col in range(size):
            if matrix[row, col] == 0:
                return False
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (
                    0 <= new_row < size
                    and 0 <= new_col < size
                    and matrix[row, col] == matrix[new_row, new_col]
                ):
                    return False  
    return True



def getOpenTiles(matrix):
    size = matrix.shape[0]
    openTiles = []
    for i in range(size):
        for j in range(size):
            if(matrix[i][j] == 0):
                openTiles.append((i,j))
    return openTiles



def add_new_tile(matrix, pos = None, number = None):
    if (number is None):
        number = np.random.choice([2, 4], p=[SPAWN_TWO_PROBABILITY, 1 - SPAWN_TWO_PROBABILITY])
    if(pos is None):
        empty_cells = list(zip(*np.where(matrix == 0)))
        if empty_cells:
            row, col = random.choice(empty_cells)
            matrix[row, col] = number
        return matrix
    else:
        matrix[pos[0]][pos[1]] = number
    return matrix