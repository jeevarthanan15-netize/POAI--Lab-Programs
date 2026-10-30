"""
SMART PARKING SLOT FINDER
Environment: Discrete

The parking area consists of fixed parking slots.
The agent selects an available slot.
"""

print("========== SMART PARKING SLOT FINDER ==========")

slot = input("Enter Available Slot (A1/A2/B1/B2): ")

print("\nParking Decision")
print("----------------------------")

if slot == "A1":
    print("Park your vehicle in Slot A1.")

elif slot == "A2":
    print("Park your vehicle in Slot A2.")

elif slot == "B1":
    print("Park your vehicle in Slot B1.")

elif slot == "B2":
    print("Park your vehicle in Slot B2.")

else:
    print("No Valid Parking Slot Available.")

print("\nReason:")
print("Parking slots are fixed and countable.")
print("This is a Discrete Environment.")