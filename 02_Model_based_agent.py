# =====================================================
# SMART MUSEUM ARTIFACT PROTECTION SYSTEM
# Model-Based Reflex Agent
# =====================================================
# Internal State (Memory)
internal_state = {
    "warning_given": False
}
SAFE_DISTANCE = 50

# Function to apply model-based rules
def apply_model_based_rules(distance):

    warning_before = internal_state["warning_given"]
    if distance < SAFE_DISTANCE and not warning_before:
        matched_rule = "Visitor too close and no previous warning."
        action = "Display Warning Message"
        result = "Please stay away from the artifact."
        internal_state["warning_given"] = True
        alarm = False
    elif distance < SAFE_DISTANCE and warning_before:
        matched_rule = "Visitor ignored previous warning."
        action = "Activate Security Alarm"
        result = "Security Alert!"
        alarm = True
    else:
        matched_rule = "Visitor is at a safe distance."
        action = "Continue Monitoring"
        result = "Safe Distance. Monitoring..."
        internal_state["warning_given"] = False
        alarm = False
    return matched_rule, action, result, warning_before, internal_state["warning_given"], alarm

# Alarm Function
def activate_alarm():
    print("🚨 SECURITY ALARM ACTIVATED! 🚨")

# Main Function
def run_monitor():
    print("==============================================")
    print(" SMART MUSEUM ARTIFACT PROTECTION SYSTEM")
    print(" Model-Based Reflex Agent")
    print("==============================================")
    try:
        distance = float(input("Enter Visitor Distance (cm): "))

        if distance < 0:
            print("Distance cannot be negative.")
            return

        matched_rule, action, result, before, after, alarm = apply_model_based_rules(distance)

        print("\n----------- OUTPUT -----------")
        print("Current Distance      :", distance, "cm")
        print("Memory Before         :", before)
        print("Matched Rule          :", matched_rule)
        print("Action                :", action)
        print("Memory After          :", after)

        if alarm:
            activate_alarm()

        print("Result                :", result)

    except ValueError:
        print("Invalid input! Please enter a number.")

# Program Starts Here
if __name__ == "__main__":
    run_monitor()
