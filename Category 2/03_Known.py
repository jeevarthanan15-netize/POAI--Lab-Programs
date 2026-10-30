"""
SMART TRAFFIC SIGNAL CONTROLLER
Environment: Known

The agent knows all traffic rules and signal timings.
It makes decisions using predefined rules.
"""

print("========== SMART TRAFFIC SIGNAL CONTROLLER ==========")

vehicle_count = int(input("Enter Number of Vehicles: "))

print("\nTraffic Decision")
print("----------------------------")

if vehicle_count > 20:
    print("Signal : GREEN")
    print("Green Time : 60 Seconds")

elif vehicle_count > 10:
    print("Signal : GREEN")
    print("Green Time : 40 Seconds")

else:
    print("Signal : GREEN")
    print("Green Time : 20 Seconds")

print("\nReason:")
print("The traffic rules and timings are already known.")
print("This is a Known Environment.")