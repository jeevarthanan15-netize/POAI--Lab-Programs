"""
FOREST FIRE DETECTION DRONE
Environment: Partially Observable

The drone cannot see the whole forest.
It only observes the current nearby area.
"""

print("========== FOREST FIRE DETECTION DRONE ==========")

smoke = input("Smoke Detected? (Yes/No): ")
temperature = float(input("Temperature (°C): "))

print("\nDrone Observation")
print("----------------------------")

if smoke == "Yes" and temperature >= 45:
    print("High Possibility of Forest Fire!")
    print("Action : Send Emergency Alert")

elif smoke == "Yes":
    print("Smoke Detected")
    print("Action : Continue Monitoring")

else:
    print("No Fire Signs Nearby")
    print("Action : Patrol Next Area")

print("\nReason:")
print("The drone only observes its nearby surroundings.")
print("It cannot view the entire forest.")