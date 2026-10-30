"""AO* Search"""

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('E', 1)]],
    'C': [[('F', 1)]],
    'D': [[('G', 1), ('H', 1)]],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

h = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0
}

solution = {}

def ao_star(node):
    if len(graph[node]) == 0:
        return h[node]

    min_cost = 9999
    best = None

    for option in graph[node]:
        cost = 0

        for child, value in option:
            cost += value + ao_star(child)

        if cost < min_cost:
            min_cost = cost
            best = option

    h[node] = min_cost
    solution[node] = best

    return min_cost

cost = ao_star('A')

print("Cost =", cost)

for node in solution:
    print(node, "->", solution[node])
