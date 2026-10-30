"""Crypt-Arithmetic Puzzle"""

from itertools import permutations
letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
def solve_cryptarithm():
    for digits in permutations(range(10), 8):
        values = dict(zip(letters, digits))
        if values['S'] == 0 or values['M'] == 0:
            continue
        SEND = (
            values['S'] * 1000 +
            values['E'] * 100 +
            values['N'] * 10 +
            values['D']
        )
        MORE = (
            values['M'] * 1000 +
            values['O'] * 100 +
            values['R'] * 10 +
            values['E']
        )
        MONEY = (
            values['M'] * 10000 +
            values['O'] * 1000 +
            values['N'] * 100 +
            values['E'] * 10 +
            values['Y']
        )
        if SEND + MORE == MONEY:
            return values, SEND, MORE, MONEY
    return None
result = solve_cryptarithm()
if result:
    values, SEND, MORE, MONEY = result
    print("Solution:")
    for letter, digit in values.items():
        print(letter, "=", digit)
    print()
    print(SEND)
    print("+", MORE)
    print("=", MONEY)
else:
    print("No solution")
