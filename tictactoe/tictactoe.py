"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Checks how many Os and Xs are  in the board
    X_inBoard = 0
    O_inBoard = 0
    for row in board:
        for block in row:
            if block == X:
                X_inBoard += 1
            if block == O:
                O_inBoard += 1
    
    # return O only if more Xs in the board(that means X in first turn)s
    if X_inBoard > O_inBoard:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initializes the set of moves possible
    moves = set()

    # Checks every square in board if its empty it can be a possible move
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY:
                moves.add((y, x))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    j, i = action

    # checks for error in action
    # if not(j <= 2 and i <= 2 and j >= 0 and i >= 0 and board[j][i] == EMPTY) :
    #     raise Exception('Move Invalid')
    
    # initializes the board copy and does the action
    boardCopy = copy.deepcopy(board)
    boardCopy[j][i] = player(boardCopy)

    return boardCopy

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks for a row
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][2] == board[i][0]:
            return board[i][0]
    
    # Checks for column
    for i in range(3):
        if board[0][i] != EMPTY and board[0][i] == board[1][i] and board[2][i] == board[0][i]:
            return board[0][i]

    # Checks for diagonals
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[2][2] == board[0][0]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[2][0] == board[0][2]:
        return board[0][2]

    # If none of above 
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def MAX_VALUE(board):
    # to stop recursion when we are at a terminal state
    if terminal(board):
        return utility(board)
    
    # initialise v to -infty
    v = -1000

    # loop for all dark witchcraft
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
        if v == 1: return v
    return v


def MIN_VALUE(board):
    # to stop recursion when we are at a terminal state
    if terminal(board):
        return utility(board)

    # initialize v to infinty
    v = 1000
    
    # loop for all the dark witchcraft
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))
        if v == -1: return v
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        best_value = -100
        for action in actions(board):
            value = MIN_VALUE(result(board, action))
            if value == 1:
                return action
            if value > best_value:
                best_move = action
                best_value = value
        
    else:
        best_value = 100
        for action in actions(board):
            value = MAX_VALUE(result(board, action))
            if value == -1:
                return action
            if value < best_value:
                best_move = action
                best_value = value

    return best_move



