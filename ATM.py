n = input("Enter the PIN: ")

balance = 10000

while True:

    if n == "1234":
        print("Login Successful")
        while True:
            print("----- ATM -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Exit")

            choice = input("Enter the feature: ")

            if choice == "1":
                print("Current Balance:", balance)

            elif choice == "2":
                amount = int(input("Enter deposit amount: "))
                if amount > 0:
                    balance = balance + amount
                    print("Deposit Successful")
                    print("Updated Balance:", balance)
                else:
                    print("Invalid Amount")

            elif choice == "3":
                amount = int(input("Enter withdrawal amount: "))
                if amount > 0 and amount <= balance:
                    balance = balance - amount
                    print("Withdrawal Successful")
                    print("Remaining Balance:", balance)
                else:
                    print("Invalid Amount")

            elif choice == "4":
                print("Thank you for using ATM")
                break

            else:
                print("Invalid Choice")
        break

    else:
        print("Wrong PIN. Try Again.")
        n = input("please Enter correct PIN: ")