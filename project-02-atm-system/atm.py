balance = 5000
userpin = 9999
attempt = 3

while attempt > 0:
    pin = int(input("Enter your PIN: "))

    if pin == userpin:
        print("Login successful!\n")
        break

    attempt -= 1
    print("Wrong PIN. Attempts left:", attempt)

if attempt == 0:
    print("Account blocked due to multiple failed attempts.")
else:
    while True:
        print("""
        1. Credit Money
        2. Debit Money
        3. Check Balance
        4. Exit
        """)
        ch = int(input("Enter your choice: "))

        if ch == 1:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Updated balance:", balance)
        elif ch == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Updated balance:", balance)
        elif ch == 3:
            print("Current balance:", balance)
        elif ch == 4:
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice.")
