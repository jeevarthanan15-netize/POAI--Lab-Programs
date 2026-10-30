"""
AUTOMATIC FACE MASK CHECKER
Environment: Episodic

Each person is checked independently.
The decision for one person does not affect the next person.
"""

print("========== AUTOMATIC FACE MASK CHECKER ==========")

mask = input("Is the person wearing a mask? (Yes/No): ")

print("\nChecking Result")
print("----------------------------")

if mask == "Yes":
    print("Access Granted")
    print("Mask Detected")

else:
    print("Access Denied")
    print("Please Wear a Mask")

print("\nReason:")
print("Each person's inspection is independent.")
print("Previous checks do not affect the current decision.")
print("This is an Episodic Environment.")