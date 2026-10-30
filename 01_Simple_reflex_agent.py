# =====================================================
# SMART LIBRARY SILENCE MONITOR
# Simple Reflex Agent
# =====================================================
# Function to apply condition-action rules
def apply_rules(current_noise):

    if current_noise > 60:
        matched_rule = "IF Noise > 60 dB"
        action = "Display 'Please Keep Silent'"
        result = "Library is Noisy."
    else:
        matched_rule = "IF Noise <= 60 dB"
        action = "No Warning"
        result = "Library Environment is Quiet."

    return matched_rule, action, result


# Function to simulate the alarm
def activate_alarm():
    print(">>> ALARM: Please Keep Silent! <<<")


# Main Function
def run_monitor():

    print("==============================================")
    print(" SMART LIBRARY SILENCE MONITOR")
    print(" Simple Reflex Agent")
    print("==============================================")

    try:
        # Current percept
        current_noise = float(input("Enter Current Noise Level (dB): "))

        if current_noise < 0:
            print("Noise level cannot be negative.")
            return

        # Apply the rules
        matched_rule, action, result = apply_rules(current_noise)

        print("\n----------- OUTPUT -----------")
        print("Current Noise Level :", current_noise, "dB")
        print("Matched Rule        :", matched_rule)
        print("Action              :", action)

        if current_noise > 60:
            activate_alarm()

        print("Result              :", result)

    except ValueError:
        print("Invalid Input! Please enter a number.")


# Program Starts Here
if __name__ == "__main__":
    run_monitor()
