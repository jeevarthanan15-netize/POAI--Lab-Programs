"""
WAREHOUSE DELIVERY ROBOT
Environment: Sequential

Every movement affects the next movement.
The robot must follow the correct sequence
to reach the destination.
"""

print("========== WAREHOUSE DELIVERY ROBOT ==========")

steps = int(input("Enter Number of Steps to Destination: "))

print("\nRobot Movement")
print("----------------------------")

for i in range(1, steps + 1):
    print("Step", i, "-> Moving Forward")

print("\nDestination Reached Successfully")

print("\nReason:")
print("Each movement depends on the previous movement.")
print("This is a Sequential Environment.")