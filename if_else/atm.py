"""✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"""

db_pin=2121
db_balance=5000
pin=int(input("Enter atm pin:"))
if db_pin==pin:
    amount=int(input("Enter withdrawl amount:"))
    if amount<=db_balance:
        print("Withdrawl successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect pin")