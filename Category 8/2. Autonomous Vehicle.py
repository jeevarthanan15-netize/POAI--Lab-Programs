"""Autonomous Vehicle"""

facts = set()
rules = []
def add_fact(fact):
    facts.add(fact)
def add_rule(conditions, conclusion):
    rules.append((conditions, conclusion))
def forward_chaining():
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    changed = True
def backward_chaining(goal, visited=None):
    if visited is None:
        visited = set()
    if goal in facts:
        return True
    if goal in visited:
        return False
    visited.add(goal)
    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(condition, visited)
                   for condition in conditions):
                return True
    return False
add_fact("traffic_light_red")
add_fact("road_clear")
add_fact("vehicle_moving")
add_rule(
    ["traffic_light_red"],
    "stop"
)
add_rule(
    ["obstacle_ahead"],
    "slow_down"
)
add_rule(
    ["pedestrian_detected"],
    "stop"
)
add_rule(
    ["traffic_light_green", "road_clear"],
    "move"
)
add_rule(
    ["stop"],
    "vehicle_stopped"
)
add_rule(
    ["slow_down"],
    "vehicle_slow"
)
print("===================================")
print("FORWARD CHAINING")
print("===================================")
forward_chaining()
print("Known facts and conclusions:")
for fact in facts:
    print("-", fact)
print()
print("===================================")
print("BACKWARD CHAINING")
print("===================================")
goal = "vehicle_stopped"
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Vehicle should STOP.")
else:
    print("Result: Cannot determine whether vehicle should stop.")
goal = "vehicle_slow"
print()
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Vehicle should SLOW DOWN.")
else:
    print("Result: Vehicle does not need to slow down.")
