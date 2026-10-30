"""
LIBRARY BOOK ORGANIZER
Environment: Static

The books do not move while the agent is making a decision.
The environment remains unchanged.
"""

print("========== LIBRARY BOOK ORGANIZER ==========")

book = input("Enter Book Category (Science/Math/History): ")

print("\nLibrary Decision")
print("----------------------------")

if book == "Science":
    print("Place the book in Science Shelf.")

elif book == "Math":
    print("Place the book in Mathematics Shelf.")

elif book == "History":
    print("Place the book in History Shelf.")

else:
    print("Category not found.")
    print("Place the book in General Shelf.")

print("\nReason:")
print("Books remain stationary while organizing.")
print("This is a Static Environment.")