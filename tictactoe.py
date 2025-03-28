from random import choice

X = "X"
O = "O"
EMPTY = "None"

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count = 0
    for row in board:
        count += row.count(X)
        count += row.count(O)
    if count % 2 == 0:
        return X
    else:
        return O

def actions(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.append((i, j))
    return available_moves

def result(board, action):
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board):
    best_move = None
    moves = actions(board)
    if len(moves) == 0:
        return None
    if len(moves) == 9:
        return choice(moves)
    for move in moves:
        new_board = result(board, move)
        if winner(new_board) == X:
            return move
    return moves[0]


if __name__ == "__main__":
    board = initial_state()

    # X делает первый ход
    board = result(board, (0, 0))  # X ставит в верхний левый угол

    # O отвечает
    board = result(board, (1, 1))  # O ставит в центр

    # X продолжает
    board = result(board, (0, 1))  # X ставит в верхний ряд, середина

    # O отвечает
    board = result(board, (2, 2))  # O ставит в нижний правый угол

    # X делает победный ход
    board = result(board, (0, 2))  # X ставит в верхний ряд, правый угол

    print("Игра окончена!")
    for row in board:
        print(row)
    print()

    if winner(board) == X:
        print("X выиграли!")
    elif winner(board) == O:
        print("O выиграли!")
    else:
        print("Ничья!")
