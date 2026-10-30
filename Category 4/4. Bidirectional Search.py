from collections import deque

def bidirectional_search(graph, start, goal):

    if start == goal:
        return [start]

    front_queue = deque([[start]])
    back_queue = deque([[goal]])

    front_visited = {start: [start]}
    back_visited = {goal: [goal]}

    while front_queue and back_queue:

        # Search from start
        path = front_queue.popleft()
        node = path[-1]

        for neighbour in graph[node]:
            if neighbour not in front_visited:
                front_visited[neighbour] = path + [neighbour]
                front_queue.append(path + [neighbour])

                if neighbour in back_visited:
                    return (front_visited[neighbour] +
                            back_visited[neighbour][-2::-1])

        # Search from goal
        path = back_queue.popleft()
        node = path[-1]

        for neighbour in graph[node]:
            if neighbour not in back_visited:
                back_visited[neighbour] = path + [neighbour]
                back_queue.append(path + [neighbour])

                if neighbour in front_visited:
                    return (front_visited[neighbour] +
                            back_visited[neighbour][-2::-1])

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

start = 'A'
goal = 'F'

path = bidirectional_search(graph, start, goal)

print("Bidirectional Search Path:", path)