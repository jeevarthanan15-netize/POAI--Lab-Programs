
"""Min-Max Search algorithm for chess game"""

def minimax(board, depth, maximizing):
    if depth == 0:
        return evaluate(board)

    if maximizing:
        best = -9999

        for move in get_moves(board, 'W'):
            new_board = make_move(board, move)
            value = minimax(new_board, depth - 1, False)
            best = max(best, value)

        return best

    else:
        best = 9999

        for move in get_moves(board, 'B'):
            new_board = make_move(board, move)
            value = minimax(new_board, depth - 1, True)
            best = min(best, value)

        return best


def evaluate(board):
    values = {
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 100
    }

    score = 0

    for row in board:
        for piece in row:
            if piece.isupper():
                score += values.get(piece.upper(), 0)
            elif piece.islower():
                score -= values.get(piece.upper(), 0)

    return score


def get_moves(board, player):
    moves = []

    for i in range(8):
        for j in range(8):
            if player == 'W' and board[i][j].isupper():
                if i > 0:
                    moves.append((i, j, i - 1, j))

            elif player == 'B' and board[i][j].islower():
                if i < 7:
                    moves.append((i, j, i + 1, j))

    return moves


def make_move(board, move):
    new_board = [row[:] for row in board]

    x1, y1, x2, y2 = move
    new_board[x2][y2] = new_board[x1][y1]
    new_board[x1][y1] = '.'

    return new_board


board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print("Min-Max value:", minimax(board, 2, True))
