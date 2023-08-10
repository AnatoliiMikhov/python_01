# Filling the dictionary with data introduced by the user

responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name: ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == "no":
        poll_active = False

# The survey is completed, derive the results.

print("\n--- Poll Results ---")

for user, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")
