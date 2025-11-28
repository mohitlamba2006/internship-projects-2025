print("=== Movie Ticket Booking System ===\n")

movies = {
    1: ("The Lion King", 0),
    2: ("Avengers: Endgame", 13),
    3: ("John Wick", 18),
    4: ("50 Shades of Grey", 18)
}

print("Available Movies:")
for num, (name, age_req) in movies.items():
    print(f"{num}. {name} (Age {age_req}+)")

try:
    choice = int(input("\nEnter movie number: "))
    if choice not in movies:
        print("Invalid selection.")
        exit()

    movie_name, min_age = movies[choice]
    age = int(input("Enter your age: "))

    if age < min_age:
        print(f"Minimum age required: {min_age}")
        exit()

    tickets = int(input("How many tickets? "))
    if tickets <= 0:
        print("Invalid ticket count.")
    else:
        print(f"Booked {tickets} ticket(s) for {movie_name}. Enjoy!")

except ValueError:
    print("Please enter numbers only.")
