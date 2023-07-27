pizza_names = ["margherita", "pepperoni", "hawaiian"]
# --------------------------------------------------------------------------- #
# how to copy list? Just use slises [0:9]
friend_pizzas = pizza_names[:]
# --------------------------------------------------------------------------- #
# append elements to list
pizza_names.append("aarhus pizza")
friend_pizzas.append("odder pizza")

# --------------------------------------------------------------------------- #
# list iteration
print("\nMy favorite pizzas are:")
for pizza in pizza_names:
    print(f"\t{pizza.title()}")

print("\n...\n")
# --------------------------------------------------------------------------- #
# list iteration
print("\nMy friend’s favorite pizzas are:")

for pizza in friend_pizzas:
    print(f"\t{pizza.title()}")
