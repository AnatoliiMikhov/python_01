# --------------------------------------------------------------------------- #
for value in range(1, 21):
    print(value)

# --------------------------------------------------------------------------- #
million_numbers = list(range(1, 1_000_001))

# it takes approximately 16 seconds on my macbook
# --------------------------------------------------------------------------- #
# for num in million_numbers:
#     print(num)
# --------------------------------------------------------------------------- #
print()
# --------------------------------------------------------------------------- #
print(min(million_numbers))
print(max(million_numbers))

print()

print(sum(million_numbers))

# --------------------------------------------------------------------------- #
odd_numbers = list(range(1, 20, 2))

for num in odd_numbers:
    print(num)
# --------------------------------------------------------------------------- #
# Trees
print("\nThere are only trees below:\n")

trees = list(range(3, 31, 3))

for tree in trees:
    print(tree)

# --------------------------------------------------------------------------- #
# var 2
# trees = list(range(3, 31, 3))

# for tree in list(range(3, 31, 3)):
#     print(tree)
# --------------------------------------------------------------------------- #

# Cubes
cubes = []

for num in range(1, 11):
    cubes.append(num**3)

for cube in cubes:
    print(cube)

# --------------------------------------------------------------------------- #
print("\nI used cube generator style below:\n")

# Cube generator

cubes_list = [value**3 for value in range(1, 11)]
for cube in cubes_list:
    print(cube)
