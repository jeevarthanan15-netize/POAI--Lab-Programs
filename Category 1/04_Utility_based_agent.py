# WILDLIFE SAFARI GUIDE AGENT
# Utility-Based Agent

weather_scores = {"Good": 100, "Moderate": 70, "Bad": 30}
road_scores = {"Excellent": 100, "Good": 80, "Average": 60, "Poor": 30}
crowd_scores = {"Low": 20, "Medium": 50, "High": 90}


def calculate_utility(route):
    weather = weather_scores[route["weather"]]
    road = road_scores[route["road"]]
    crowd = crowd_scores[route["crowd"]]

    utility = (route["animals"] * 0.4) + (weather * 0.2) + (road * 0.2) \
              - (crowd * 0.1) - (route["fuel"] * 0.1)

    return round(utility, 1)


print("======================================")
print(" Wildlife Safari Guide Agent")
print(" Utility-Based Agent")
print("======================================")

route = {}

route["name"] = input("Enter Route Name: ")
route["animals"] = int(input("Animal Sighting Chance (0-100): "))
route["weather"] = input("Weather (Good/Moderate/Bad): ")
route["crowd"] = input("Crowd (Low/Medium/High): ")
route["road"] = input("Road Condition (Excellent/Good/Average/Poor): ")
route["fuel"] = int(input("Fuel Cost: "))

score = calculate_utility(route)

print("\n----------- RESULT -----------")
print("Route Name     :", route["name"])
print("Utility Score  :", score)

if score >= 70:
    print("Recommendation : Excellent Route")
elif score >= 50:
    print("Recommendation : Good Route")
else:
    print("Recommendation : Choose Another Route")
