import numpy as np
from TicTacToe import *
from copy import deepcopy

from keras.models import load_model
smort = load_model('smort')

board = np.zeros((3, 3), dtype=int)
print_board(board)
print('>>Human turn<<')
human = input('Type position, <row col>, "0 0": ')
board[int(human[0]), int(human[2])] = pieces['O']

while True:
    print_board(board)
    print('>>Smort turn<<')
    available_cells = get_available_cells(board)
    max_val = 0.0
    best_cell = available_cells[0]

    for cell in available_cells:
        temp_board = deepcopy(board)
        temp_board[cell[0], cell[1]] = pieces['X']

        val = smort.predict(temp_board.reshape(-1,3*3))[0][0] # [0][0] for X wins, [0][1] for Draw, [0][1] for O wins 
        if val > max_val:
            max_val = val
            best_cell = cell


    board[best_cell[0], best_cell[1]] = pieces['X']

    if check_state(board) == states['X'] or check_state(board) == states['O'] or check_state(board) == states['Draw']:
        print(check_state(board))
        print(states)
        break

    print_board(board)
    print('>>Human turn<<')
    human = input('Type position, <row col>, "0 0": ')
    board[int(human[0]), int(human[2])] = pieces['O']

    if check_state(board) == states['X'] or check_state(board) == states['O'] or check_state(board) == states['Draw']:
        print(check_state(board))
        print(states)
        break
