# how to copy a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# --------------------------------------------------------------------------- #
my_foods.append("borsh")
my_foods.append("fish")
my_foods.append("egg")
friend_foods.append("bread")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# --------------------------------------------------------------------------- #
my_foods.append("soup")
friend_foods.append("apples")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print(len(my_foods))

# --------------------------------------------------------------------------- #
#                                      HW                                     #
# --------------------------------------------------------------------------- #

first_tree_items = my_foods[0:3]
middle_items = my_foods[2:5]
last_tree_items = my_foods[-3:]

print("\nThe first three items in the list are:»")
print(first_tree_items)

print("\nThree items from the middle of the list are:")
print(middle_items)

print("\nThe last three items in the list are:")
print(last_tree_items)
