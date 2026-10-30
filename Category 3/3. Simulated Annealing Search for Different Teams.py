import random
import math

# Teams
teams = ["Team A", "Team B", "Team C", "Team D"]

# Tasks
tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]

# Cost matrix
# Rows = Teams
# Columns = Tasks
cost = [
    [9, 2, 7, 8],   # Team A
    [6, 4, 3, 7],   # Team B
    [5, 8, 1, 8],   # Team C
    [7, 6, 9, 4]    # Team D
]


# Calculate total cost
def total_cost(solution):
    total = 0

    for team in range(len(teams)):
        task = solution[team]
        total += cost[team][task]

    return total


# Generate neighboring solution
def get_neighbor(solution):
    new_solution = solution.copy()

    # Swap two teams' tasks
    i, j = random.sample(range(len(solution)), 2)

    new_solution[i], new_solution[j] = (
        new_solution[j],
        new_solution[i]
    )

    return new_solution


# Simulated Annealing
def simulated_annealing():

    # Initial random solution
    current = list(range(len(tasks)))
    random.shuffle(current)

    best = current.copy()

    temperature = 1000
    cooling_rate = 0.95
    minimum_temperature = 0.01

    while temperature > minimum_temperature:

        neighbor = get_neighbor(current)

        current_cost = total_cost(current)
        neighbor_cost = total_cost(neighbor)

        # Always accept better solution
        if neighbor_cost < current_cost:
            current = neighbor

        else:
            # Sometimes accept worse solution
            probability = math.exp(
                -(neighbor_cost - current_cost) / temperature
            )

            if random.random() < probability:
                current = neighbor

        # Update best solution
        if total_cost(current) < total_cost(best):
            best = current.copy()

        # Cool down
        temperature *= cooling_rate

    return best


# Run algorithm
solution = simulated_annealing()

print("Best Team Assignment:")
print()

for i in range(len(teams)):
    print(teams[i], "->", tasks[solution[i]])

print("\nMinimum Total Cost:", total_cost(solution))