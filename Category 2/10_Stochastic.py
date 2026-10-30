"""
WEATHER-BASED TRAVEL ADVISOR
Environment: Stochastic

Weather is uncertain and can change unexpectedly.
The agent makes decisions based on the predicted weather.
"""

import random

print("========== WEATHER-BASED TRAVEL ADVISOR ==========")

weather = random.choice(["Sunny", "Rainy", "Cloudy"])

print("Today's Weather :", weather)

print("\nTravel Decision")
print("----------------------------")

if weather == "Sunny":
    print("Enjoy your trip!")
    print("Carry sunglasses.")

elif weather == "Cloudy":
    print("Trip is possible.")
    print("Carry a light jacket.")

else:
    print("Travel with caution.")
    print("Carry an umbrella.")

print("\nReason:")
print("Weather changes randomly and cannot be predicted with certainty.")
print("This is a Stochastic Environment.")