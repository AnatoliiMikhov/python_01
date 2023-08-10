# while, polling, input

places = {}

# active = True
# while active:
while True:
    user_name = input("\nWhat is your name? ")
    place = input("Where would you like to spend your vacation? ")

    places[user_name] = place

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        # active = False
        break

print("\n--- Poll Results ---\n")

for user, place in places.items():
    print(f"{user.title()} would like to spend vacation in {place.title()}")
