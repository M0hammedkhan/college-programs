import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b * b - 4 * a * c

if d > 0:
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)
    print("Real and distinct roots")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)
    print("Real and equal roots")
    print("Root =", root)

else:
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    print("Imaginary roots")
    print("Root 1 =", root1)
    print("Root 2 =", root2)