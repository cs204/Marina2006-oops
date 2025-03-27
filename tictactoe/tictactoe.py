"""
Tic Tac Toe Player
"""
from random import choice
import copy
X = "X"
O = "O"
EMPTY = "None"
infinity = float("inf")

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count = sum(row.count(X) + row.count(O) for row in board)
    return X if count % 2 == 0 else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    nboard = copy.deepcopy(board)
    board[action[0]][action[1]] = player(board)
    return board

def winner(board):
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
        if all(board[i][j] == O for i in range(3)):
            return O

    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    if all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None

def terminal(board):
    return winner(board) is not None or not any(EMPTY in row for row in board)

def utility(board):
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0

def AI_Turn(board, length, pl):
    if pl == X:
        best = (-1, -1, -infinity)
    else:
        best = (-1, -1, +infinity)

    if length == 0 or terminal(board):
        score = utility(board)
        return (-1, -1, score)

    for x, y in actions(board):
        new_board = copy.deepcopy(board)  # Создаем копию перед изменением
        new_board[x][y] = pl
        score = AI_Turn(new_board, length - 1, player(new_board))
        score = (x, y, score[2])

        if pl == X:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def minimax(board):
    pl = player(board)
    length = len(actions(board))

    if length == 0 or terminal(board):
        return None

    if length == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = AI_Turn(board, length, pl)
        x, y = move[0], move[1]

    return (x, y)

