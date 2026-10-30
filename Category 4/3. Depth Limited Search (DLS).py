def depth_limited_search(graph, node, goal, limit, path=None):
    if path is None:
        path = [node]

    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbour in graph[node]:
        if neighbour not in path:
            result = depth_limited_search(
                graph,
                neighbour,
                goal,
                limit - 1,
                path + [neighbour]
            )

            if result:
                return result

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'
limit = 3

path = depth_limited_search(graph, start, goal, limit)

if path:
    print("DLS Path:", path)
else:
    print("Goal not found within depth limit")