import heapq

def heuristic(board):
    score = 0

    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in lines:
        line = [board[a], board[b], board[c]]

        if line.count('X') == 2 and line.count('-') == 1:
            score -= 10

        elif line.count('O') == 2 and line.count('-') == 1:
            score += 10

        elif line.count('X') == 1 and line.count('-') == 2:
            score -= 1

        elif line.count('O') == 1 and line.count('-') == 2:
            score += 1

    return score

def greedy(board):
    queue = []

    for i in range(9):
        if board[i] == '-':
            new_board = list(board)
            new_board[i] = 'O'
            new_board = tuple(new_board)

            heapq.heappush(queue, (heuristic(new_board), new_board))

    if queue:
        return heapq.heappop(queue)[1]

    return board

board = (
    'X', 'O', 'X',
    '-', 'O', '-',
    '-', '-', '-'
)

result = greedy(board)

print(result[0:3])
print(result[3:6])
print(result[6:9])
