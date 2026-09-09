balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
min_balance = float(input("Enter minimum balance: "))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Withdrawal rejected: Insufficient balance")
elif balance - amount < min_balance:
    print("Withdrawal rejected: Minimum balance rule violated")
else:
    balance -= amount
    print("Withdrawal approved")
    print("Remaining balance:", balance)