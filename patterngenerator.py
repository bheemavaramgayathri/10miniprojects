
print("Pattern Generator")
print("1. Square")
print("2. Triangle")
print("3. Hollow Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter size: "))

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

elif choice == 2:
    n = int(input("Enter: "))

    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

elif choice == 3:
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))

    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

else:
    print("Invalid choice")