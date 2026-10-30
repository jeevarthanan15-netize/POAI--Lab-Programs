"""Local Search for CSP"""

import random
N = 8
def conflicts(board):
    total = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                total += 1
            if abs(board[i] - board[j]) == abs(i - j):
                total += 1
    return total
def get_neighbors(board):
    neighbors = []
    for row in range(N):
        for col in range(N):
            if col != board[row]:
                new_board = board[:]
                new_board[row] = col
                neighbors.append(new_board)
    return neighbors
def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]
    while True:
        current_conflicts = conflicts(board)
        if current_conflicts == 0:
            return board
        neighbors = get_neighbors(board)
        best_board = min(neighbors, key=conflicts)
        best_conflicts = conflicts(best_board)
        if best_conflicts >= current_conflicts:
            board = [random.randint(0, N - 1) for _ in range(N)]
        else:
            board = best_board
solution = hill_climbing()
print("8-Queens Solution:")
print(solution)
print("Conflicts:", conflicts(solution))
