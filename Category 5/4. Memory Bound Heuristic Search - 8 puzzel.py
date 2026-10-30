"""Memory Bound Heuristic Search - 8 puzzel"""

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] == 0:
            continue

        pos = goal.index(state[i])

        r1 = i // 3
        c1 = i % 3

        r2 = pos // 3
        c2 = pos % 3

        distance += abs(r1 - r2) + abs(c1 - c2)

    return distance

def moves(state):
    result = []

    pos = state.index(0)
    row = pos // 3
    col = pos % 3

    if row > 0:
        new = list(state)
        new[pos], new[pos - 3] = new[pos - 3], new[pos]
        result.append(tuple(new))

    if row < 2:
        new = list(state)
        new[pos], new[pos + 3] = new[pos + 3], new[pos]
        result.append(tuple(new))

    if col > 0:
        new = list(state)
        new[pos], new[pos - 1] = new[pos - 1], new[pos]
        result.append(tuple(new))

    if col < 2:
        new = list(state)
        new[pos], new[pos + 1] = new[pos + 1], new[pos]
        result.append(tuple(new))

    return result

def search(state, goal, g, limit, path):
    f = g + heuristic(state, goal)

    if f > limit:
        return f

    if state == goal:
        return path

    minimum = 9999

    for next_state in moves(state):
        if next_state not in path:
            path.append(next_state)

            result = search(
                next_state,
                goal,
                g + 1,
                limit,
                path
            )

            if isinstance(result, list):
                return result

            if result < minimum:
                minimum = result

            path.pop()

    return minimum

def ida_star(start, goal):
    limit = heuristic(start, goal)
    path = [start]

    while True:
        result = search(
            start,
            goal,
            0,
            limit,
            path
        )

        if isinstance(result, list):
            return result

        limit = result

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

path = ida_star(start, goal)

for state in path:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
