"""Medical Diagnosis
"""

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
add_fact("fever")
add_fact("cough")
add_fact("body_pain")
add_rule(
    ["fever", "cough", "body_pain"],
    "flu"
)
add_rule(
    ["fever", "rash"],
    "measles"
)
add_rule(
    ["cough", "breathing_problem"],
    "bronchitis"
)
add_rule(
    ["flu"],
    "viral_infection"
)
add_rule(
    ["viral_infection"],
    "infection"
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
goal = "flu"
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Goal can be proved.")
else:
    print("Result: Goal cannot be proved.")
goal = "measles"
print()
print("Goal:", goal)
if backward_chaining(goal):
    print("Result: Goal can be proved.")
else:
    print("Result: Goal cannot be proved.")
