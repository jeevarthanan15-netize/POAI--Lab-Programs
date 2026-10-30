"""Industrial Manufacturing"""

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
add_fact("machine_vibration")
add_fact("high_temperature")
add_fact("low_oil")
add_rule(
    ["machine_vibration", "high_temperature"],
    "machine_fault"
)
add_rule(
    ["low_oil"],
    "lubrication_required"
)
add_rule(
    ["machine_fault"],
    "maintenance_required"
)
add_rule(
    ["lubrication_required"],
    "maintenance_required"
)
add_rule(
    ["maintenance_required"],
    "inspection_required"
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
goal = "maintenance_required"
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Maintenance is REQUIRED.")
else:
    print("Result: Maintenance is NOT required.")
goal = "inspection_required"
print()
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Inspection is REQUIRED.")
else:
    print("Result: Inspection is NOT required.")
