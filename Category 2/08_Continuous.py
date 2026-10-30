"""
SMART GREENHOUSE CLIMATE CONTROLLER
Environment: Continuous

Temperature changes continuously.
The agent adjusts the cooling or heating system.
"""

print("========== SMART GREENHOUSE CLIMATE CONTROLLER ==========")

temperature = float(input("Enter Current Temperature (°C): "))

print("\nClimate Decision")
print("----------------------------")

if temperature > 35:
    print("Cooling System : ON")

elif temperature < 20:
    print("Heater : ON")

else:
    print("Temperature is Normal")
    print("No Action Required")

print("\nReason:")
print("Temperature changes continuously.")
print("This is a Continuous Environment.")