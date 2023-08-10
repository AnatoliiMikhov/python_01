# how to remove all element from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

print("\n", pets)


# --------------------------------------------------------------------------- #
print("\n...\n")
# --------------------------------------------------------------------------- #


while "cat" in pets:
    pets.remove("cat")

print(pets)
