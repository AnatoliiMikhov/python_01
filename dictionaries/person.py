human = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",
}

first_name = human["first_name"]
last_name = human["last_name"]
age = human["age"]
city = human["city"]

print(first_name)
print(last_name)
print(age)

# --------------------------------------------------------------------------- #
print()
# --------------------------------------------------------------------------- #

for value in human.values():
    print(value)

# --------------------------------------------------------------------------- #
print()
# --------------------------------------------------------------------------- #

for key, value in human.items():
    print(f"{key}: {value}")
