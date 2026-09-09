hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    salary = hours * rate
else:
    overtime_hours = hours - 40
    salary = (40 * rate) + (overtime_hours * rate * 1.5)

print("Salary =", salary)
