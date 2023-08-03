margarita_pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese", "olives"],
}

# order description
print(
    f"\nYou ordered a {margarita_pizza['crust']}-crust pizza "
    "with the following toppings:"
)

for topping in margarita_pizza["toppings"]:
    print(f"\t{topping}")
