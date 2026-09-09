n = int(input("Enter number of rows: "))

# Upper half
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# Lower half
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)