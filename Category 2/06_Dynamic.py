"""
AMBULANCE ROUTE ASSISTANT
Environment: Dynamic

Traffic conditions change continuously.
The agent must react to the current traffic situation.
"""

print("========== AMBULANCE ROUTE ASSISTANT ==========")

traffic = input("Traffic Condition (Low/Medium/High): ")

print("\nRoute Decision")
print("----------------------------")

if traffic == "Low":
    print("Recommended Route : Main Road")
    print("Estimated Time : 10 Minutes")

elif traffic == "Medium":
    print("Recommended Route : Ring Road")
    print("Estimated Time : 15 Minutes")

elif traffic == "High":
    print("Recommended Route : Emergency Lane")
    print("Estimated Time : 8 Minutes")

else:
    print("Invalid Traffic Condition")

print("\nReason:")
print("Traffic changes continuously while the ambulance travels.")
print("This is a Dynamic Environment.")