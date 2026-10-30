"""
ATM CASH DISPENSING AGENT
Environment: Deterministic

The same input always produces the same output.
If the account has sufficient balance, cash is dispensed.
Otherwise, the transaction is rejected.
"""

print("========== ATM CASH DISPENSING AGENT ==========")

balance = float(input("Enter Account Balance: "))
withdraw = float(input("Enter Withdrawal Amount: "))

print("\nTransaction Result")
print("----------------------------")

if withdraw <= balance:
    balance = balance - withdraw
    print("Transaction Successful")
    print("Cash Dispensed :", withdraw)
    print("Remaining Balance :", balance)
else:
    print("Insufficient Balance")
    print("Transaction Cancelled")

print("\nReason:")
print("The same input always gives the same result.")
print("This is a Deterministic Environment.")