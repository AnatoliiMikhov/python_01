# ticket price

while True:
    age = input("\nEnter your age: \nor enter quit for exit: ")

    if age == "quit":
        break
    elif age.isnumeric():
        age = int(age)

        if age <= 3:
            price = "free"
        elif age > 3 and age <= 12:
            price = 10
        else:
            price = 15
    else:
        print(
            f'\nYou may have entered incorrect information. Check it, please. You have˜ entered "{age}". It is not a integer.'
        )
        continue

    print(f"\nYour ticket is {price}.")
