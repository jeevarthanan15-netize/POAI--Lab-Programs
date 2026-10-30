
"""Min-Max Search Algorithm for Tic-Tac-Toe"""

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def minimax(board, maximizing):
    winner = check_winner(board)

    if winner == 'O':
        return 1

    if winner == 'X':
        return -1

    if is_full(board):
        return 0

    if maximizing:
        best = -999

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = minimax(board, False)
                    board[i][j] = ' '
                    best = max(best, value)

        return best

    else:
        best = 999

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, True)
                    board[i][j] = ' '
                    best = min(best, value)

        return best


def best_move(board):
    best_value = -999
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                value = minimax(board, False)
                board[i][j] = ' '

                if value > best_value:
                    best_value = value
                    move = (i, j)

    return move


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

while True:
    print_board(board)

    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    if board[row][col] != ' ':
        print("Invalid move")
        continue

    board[row][col] = 'X'

    if check_winner(board) == 'X':
        print_board(board)
        print("You win!")
        break

    if is_full(board):
        print_board(board)
        print("Draw!")
        break

    move = best_move(board)
    board[move[0]][move[1]] = 'O'

    print("Computer played:", move[0] + 1, move[1] + 1)

    if check_winner(board) == 'O':
        print_board(board)
        print("Computer wins!")
        break

    if is_full(board):
        print_board(board)
        print("Draw!")
        break
