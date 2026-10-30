
"""Map -Coloring"""

colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
assignment = {}
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def map_coloring():
    if len(assignment) == len(neighbors):
        return True
    for region in neighbors:
        if region not in assignment:
            break
    for color in colors:
        if is_valid(region, color):
            assignment[region] = color
            if map_coloring():
                return True
            del assignment[region]
    return False
if map_coloring():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("No solution")
