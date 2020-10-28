import numpy as np
pieces = {'X':-1, 'O':1, 'B':0}
states = {'X':-1, 'O':1, 'Draw':0, 'Middle':2}

def print_board(board):
    nice_display = ''
    for i in board:
        for ii in i:
            if ii == -1:
                nice_display = nice_display + '[X]'
            elif ii == 0:
                nice_display = nice_display + '[ ]'
            elif ii == 1:
                nice_display = nice_display + '[O]'

        nice_display = nice_display + '\n'

    print(nice_display)


def is_won(board, val):
    if board[0, 0] == board[1, 1] == board[2, 2] == val:
        # Check 1st diagonal
        return True
    elif board[0, 2] == board[1, 1] == board[2,0] == val:
        # Check 2nd diagonal
        return True
    else:
        for i in range(len(board)):
            # Check rows
            if board[i, 0] == board[i, 1] == board[i, 2] == val:
                return True

        for i in range(len(board)):
            # Check columns
            if board[0, i] == board[1, i] == board[2, i] == val:
                return True


    return False


def check_state(board):
    if is_won(board, -1):
        return states['X']
    elif is_won(board, 1):
        return states['O']
    elif 0 not in board:
        return states['Draw']

def get_available_cells(board):
    res = np.where(board==0)
    return list(zip(res[0], res[1]))
