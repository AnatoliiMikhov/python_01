# Guests list
names = ["alice", "bob", "charlie"]
# names = ["David", "Emma", "Frank"]

message = "\nWelcome"

print(f"{message} {names[0].title()}")
print(f"{message} {names[1].title()}")
print(f"{message} {names[2].title()}")

# --------------------------------------------------------------------------- #
will_not_come = "bob"

names.remove(will_not_come)

print(names)

# --------------------------------------------------------------------------- #
names.insert(1, "john")

print(names)

print(f"{message} {names[0].title()}")
print(f"{message} {names[1].title()}")
print(f"{message} {names[2].title()}")

print("\nHooray We are expanding the guest list!!!\n")

names.insert(0, "david")
names.insert(2, "emma")
names.append("frank")

print(names)

# --------------------------------------------------------------------------- #
print("\nUnfortunately, only two guests are invited to dinner\n")

poped_name = names.pop()
print(f"I am sorry {poped_name.title()}")

poped_name = names.pop()
print(f"I am sorry {poped_name.title()}")

poped_name = names.pop()
print(f"I am sorry {poped_name.title()}")

poped_name = names.pop()
print(f"I am sorry {poped_name.title()}")

print(names)

# --------------------------------------------------------------------------- #
print(f"Welcome {names[0].title()}")
print(f"Welcome {names[1].title()}")

# --------------------------------------------------------------------------- #
del names[0]
del names[0]

print(names)
