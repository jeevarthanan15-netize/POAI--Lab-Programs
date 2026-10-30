"""
MARS EXPLORATION ROVER
Environment: Unknown

The rover explores unknown terrain.
It does not know what obstacle lies ahead until it senses it.
"""

print("========== MARS EXPLORATION ROVER ==========")

obstacle = input("Obstacle Detected? (Yes/No): ")

print("\nRover Decision")
print("----------------------------")

if obstacle == "Yes":
    print("Obstacle Found")
    print("Action : Turn Right and Explore New Path")

else:
    print("No Obstacle")
    print("Action : Move Forward")

print("\nReason:")
print("The rover has no prior knowledge of the environment.")
print("It discovers obstacles while exploring.")