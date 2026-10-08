n = input("Enter Password: ")

lower = False
upper = False
digit = False
special = False

for i in n:
    if i.isupper():
        upper = True

    if i.islower():
        lower = True

    if i.isdigit():
        digit = True

    if i in "@#$%&*":
        special = True

if upper and lower and digit and special and len(n) > 8:
    print("Valid Password")
else:
    print("Invalid Password")