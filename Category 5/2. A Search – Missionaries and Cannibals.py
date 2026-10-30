"""A* Search – Missionaries and Cannibals"""

import heapq

def valid(m, c):
    mr = 3 - m
    cr = 3 - c

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    if mr > 0 and mr < cr:
        return False

    return True

def moves(state):
    m, c, boat = state
    result = []

    possible = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for x, y in possible:
        if boat == 0:
            new = (m - x, c - y, 1)
        else:
            new = (m + x, c + y, 0)

        if valid(new[0], new[1]):
            result.append(new)

    return result

def heuristic(state):
    return state[0] + state[1]

def a_star(start, goal):
    queue = []
    heapq.heappush(queue, (heuristic(start), 0, start))

    cost = {start: 0}
    parent = {start: None}

    while queue:
        f, g, current = heapq.heappop(queue)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for next_state in moves(current):
            new_cost = g + 1

            if next_state not in cost or new_cost < cost[next_state]:
                cost[next_state] = new_cost
                parent[next_state] = current

                f = new_cost + heuristic(next_state)
                heapq.heappush(queue, (f, new_cost, next_state))

    return None

start = (3, 3, 0)
goal = (0, 0, 1)

path = a_star(start, goal)

for state in path:
    print(state)
