toppings = []

while True:
    topping = input("Enter a topping here:\nIf you need to end enter quit: ")

    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"\nThe {topping} was added to your order\n")

print("\nYou have ordered a pizza with the next toppings:")

for topping in toppings:
    print(f"\t{topping}")
