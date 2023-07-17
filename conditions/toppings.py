requested_toppings = ["mushrooms", "extra cheese"]

if requested_toppings != "anchovies":
    print("\nHold the anchovies!")

# ---------------- Checking the entry of values into the list --------------- #
# ------------------- Перевірка входження значень до списку ------------------ #
requested_toppings = ["mushrooms", "onions", "pineapple", "extra cheese"]

if "onions" in requested_toppings:
    print("\nIt's Ok. There is an onion")

# ------------- Checking for the absence of a value in the list ------------- #
# ----------------- Перевірка відсутності значення в списку ----------------- #
if "cheese" not in requested_toppings:
    print("\nYou should add some cheese.")

# ------------------------- Check a few conditionals ------------------------ #
print()

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# --------------------------------------------------------------------------- #
print("-------------------------- * * * * * * * * * -------------------------")

not_available = "pineapple"

for requested_topping in requested_toppings:
    if requested_topping == not_available:
        print(f"Sorry, we are out of {not_available} right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

# --------------------------------------------------------------------------- #
print("-------------------------- * * * * * * * * * -------------------------")

# requested_toppings = ["mushrooms", "onions", "pineapple", "extra cheese"]
requested_toppings = []

not_available = "extra cheese"

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == not_available:
            print(f"Sorry, we are out of {not_available} right now.")
        else:
            print(f"Adding {requested_topping}")

    print("\nFinished making your pizza!")

else:
    print("Are you sure you want a plain pizza?")
