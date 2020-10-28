from TicTacToe import *
import numpy as np
from random import choice
from copy import deepcopy
import pickle

# To generate random games as dataset
if __name__ == '__main__':
    training_history = []
    number_of_games = 100

    for gameth in range(number_of_games):
        board = np.zeros((3, 3), dtype=int)
        board_history = []
        board_result = None
        player_to_move = pieces['X']
        while True:
            available_cells = get_available_cells(board)
            selected_cell = choice(available_cells)
            board[selected_cell[0], selected_cell[1]] = player_to_move

            if player_to_move == pieces['X']:
                player_to_move = pieces['O']
            else:
                player_to_move = pieces['X']

            if check_state(board) == states['X'] or check_state(board) == states['O'] or check_state(board) == states['Draw']:
                board_history.append(deepcopy(board))
                board_result = check_state(board)
                break
            else:
                board_history.append(deepcopy(board))

        for move_history in board_history:
            training_history.append((move_history, board_result))

    with open('TEST_training_history.pkl', 'wb') as f:
        pickle.dump(training_history, f)
