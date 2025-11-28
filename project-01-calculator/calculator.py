while True:
    try:
        n1 = int(input("Enter 1st number: "))
        n2 = int(input("Enter 2nd number: "))

        print("""
        1. Multiplication
        2. Addition
        3. Subtraction
        4. Division
        5. Exit
        """)

        a = input("Enter your choice (1,2,3,4,5): ")

        if a == "1":
            print("Answer:", n1 * n2)
        elif a == "2":
            print("Answer:", n1 + n2)
        elif a == "3":
            print("Answer:", n1 - n2)
        elif a == "4":
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Answer:", n1 / n2)
        elif a == "5":
            print("Exiting calculator...")
            break
        else:
            print("Invalid choice. Enter only (1,2,3,4,5).")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    print()
