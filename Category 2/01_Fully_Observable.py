"""
SMART FACTORY MACHINE INSPECTOR
Environment: Fully Observable

The agent can observe the complete state of all machines
before making a decision.
"""

print("========== SMART FACTORY MACHINE INSPECTOR ==========")

machine1 = input("Machine 1 Status (Working/Faulty): ")
machine2 = input("Machine 2 Status (Working/Faulty): ")
machine3 = input("Machine 3 Status (Working/Faulty): ")

print("\nFactory Report")
print("----------------------------")

if machine1 == "Faulty":
    print("Machine 1 -> Repair Required")
else:
    print("Machine 1 -> Working Properly")

if machine2 == "Faulty":
    print("Machine 2 -> Repair Required")
else:
    print("Machine 2 -> Working Properly")

if machine3 == "Faulty":
    print("Machine 3 -> Repair Required")
else:
    print("Machine 3 -> Working Properly")

print("\nDecision Completed.")
print("Reason: Agent can observe every machine completely.")