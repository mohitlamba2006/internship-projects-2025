try:
    a = int(input("Enter a number: "))
    if a > 0:
        print("Positive")
    elif a < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Enter a valid integer.")
