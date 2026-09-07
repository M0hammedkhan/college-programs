temp = float(input("Enter temperature: "))
choice = input("Convert to (C/F): ").upper()

if choice == "F":
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif choice == "C":
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid choice")