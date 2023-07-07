# how to get a slice of a list
cars = [
    "toyota",
    "honda",
    "ford",
    "chevrolet",
    "bmw",
    "mercedes-benz",
    "audi",
    "tesla",
    "nissan",
    "hyundai",
]

first_tree = cars[0:3]
print(first_tree)

first_tree = cars[:3]
print(first_tree)

start_third = cars[3:]
print(start_third)

last_tree = cars[-3:]
print(last_tree)


# --------------------------------------------------------------------------- #
print("\nHere are the first three cars on my park:\n")

for car in cars[0:3]:
    print(car.title())

# --------------------------------------------------------------------------- #
print("\nHere are the last three cars on my park:\n")

for car in cars[-3:]:
    print(car.title())

# --------------------------------------------------------------------------- #
numbers = [11, 2, 17, 8, 5, 19, 14, 20, 1, 10, 7, 16, 4, 13, 6, 3, 12, 9, 18, 15]

sorted_numbers = sorted(numbers)

tree_bigger_num = sorted_numbers[-3:]

print("\nHere are 3 bigger integer of the list:\n")
print(tree_bigger_num)

# --------------------------------------------------------------------------- #
