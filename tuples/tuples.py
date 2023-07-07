# кортеж - immutable list
numbers = (3, 4, 5)

volume = 1

for num in numbers:
    volume *= num

print(f"Volume = {volume}")

# --------------------------------------------------------------------------- #
# create a tuple
dimensions = (200, 50)

print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

# change the tuple
dimensions = (400, 100)
print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)
# --------------------------------------------------------------------------- #

# ------------------------------------ HW ----------------------------------- #
# --------------------------------------------------------------------------- #
#                                    Buffet                                   #
# --------------------------------------------------------------------------- #
meals = ("pizza", "pasta", "burger", "salad", "sushi")

for meal in meals:
    print(f"You may order some {meal}")

# next line is wrong
# meals[-1] = "fish"

print(meals)

meals = ("pizza", "rice", "fish", "salad", "sushi")

for meal in meals:
    print(meal)
