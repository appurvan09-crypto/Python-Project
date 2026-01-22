print(Welcome to The Great Bank of India)
ac = {}

while True:
    print("Menu:")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Update Account")
    print("4. Display Accounts")
    print("5. Deposit")
    print("6. Withdraw")
    print("7. Exit")
    
    ch = input("Enter your choice (1/2/3/4/5/6/7): ")

    if ch == "1":
        an = input("Enter account number: ")
        name = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        ac[an] = {'name': name, 'balance': balance}
        print("Account created successfully!")

    elif ch == "2":
        an = input("Enter account number to delete: ")
        if an in ac:
            del ac[an]
            print("Account deleted successfully!")
        else:
            print("Account not found.")

    elif ch == "3":
        an = input("Enter account number to update: ")
        if an in ac:
            name = input("Enter new account holder's name: ")
            ac[an]['name'] = name
            print("Account updated successfully!")
        else:
            print("Account not found.")

    elif ch == "4":
        print("Accounts:")
        for an, ai in ac.items():
            print("Account Number:" ,an, "Name:", ai['name'], "Balance:", ai['balance'])

    elif ch == "5":
        an = input("Enter account number: ")
        if an in ac:
            amount = float(input("Enter amount to deposit: "))
            ac[an]['balance'] += amount
            print("Amount deposited successfully!")
            print("Your current balance is",ac[an]['balance'])
        else:
            print("Account not found.")

    elif ch == "6":
        an = input("Enter account number: ")
        if an in ac:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= ac[an]['balance']:
                ac[an]['balance'] -= amount
                print("Amount withdrawn successfully!")
                print("Your current balance is",ac[an]['balance'])
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    elif ch == "7":
        print("Thank you for using our bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

    


