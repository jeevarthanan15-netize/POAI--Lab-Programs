import random

N = 8


# Calculate number of attacking queen pairs
def conflicts(board):
    count = 0

    for i in range(N):
        for j in range(i + 1, N):

            # Same column
            if board[i] == board[j]:
                count += 1

            # Same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


# Generate a neighboring state
def get_neighbors(board):
    neighbors = []

    for row in range(N):
        for col in range(N):

            if col != board[row]:
                new_board = board.copy()
                new_board[row] = col
                neighbors.append(new_board)

    return neighbors


# Hill Climbing algorithm
def hill_climbing():

    # Random initial state
    current = [random.randint(0, N - 1) for _ in range(N)]

    while True:

        current_conflicts = conflicts(current)

        # Solution found
        if current_conflicts == 0:
            return current

        neighbors = get_neighbors(current)

        # Select the best neighbor
        best = min(neighbors, key=conflicts)
        best_conflicts = conflicts(best)

        # Local optimum reached
        if best_conflicts >= current_conflicts:
            print("Hill Climbing got stuck at local optimum.")
            return current

        current = best


# Run the algorithm
solution = hill_climbing()

print("Board:", solution)
print("Number of conflicts:", conflicts(solution))

print("\nChess Board:")

for row in range(N):
    for col in range(N):

        if solution[row] == col:
            print("Q", end=" ")
        else:
            print(".", end=" ")

    print()