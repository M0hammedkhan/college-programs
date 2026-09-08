import math

x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0

for i in range(n):
    power = 2 * i + 1
    term = (x ** power) / math.factorial(power)

    if i % 2 == 0:
        total += term
    else:
        total -= term

print("Sum =", total)