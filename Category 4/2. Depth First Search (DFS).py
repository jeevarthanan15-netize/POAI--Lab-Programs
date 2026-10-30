def dfs(graph, node, goal, visited=None):
    if visited is None:
        visited = set()

    if node == goal:
        return [node]

    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, goal, visited)

            if path:
                return [node] + path

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'

path = dfs(graph, start, goal)

print("DFS Path:", path)