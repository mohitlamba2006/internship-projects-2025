print("UNIT CONVERTER")
print("1. Kilograms to Pounds")
print("2. Hours to Minutes")

try:
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        kg = float(input("Enter weight in kg: "))
        print(f"Weight in pounds: {kg * 2.20462:.2f}")
    elif choice == 2:
        hours = float(input("Enter hours: "))
        print(f"Time in minutes: {hours * 60}")
    else:
        print("Invalid option.")
except ValueError:
    print("Enter numeric values only.")
