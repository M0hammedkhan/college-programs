rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        # Rectangle border
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        # Hollow diamond
        elif abs(i - rows // 2) + abs(j - cols // 2) == rows // 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()