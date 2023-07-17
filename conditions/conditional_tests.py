# conditional test
car = "subaru"

print("\nIs car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# --------------------------------------------------------------------------- #
month = "March"

print("\nIs monts == 'March'? I predict True")
print(month == "March")

print("\nIs monts == 'April'? I predict False")
print(month == "April")

string_1 = "Some texT here"
string_2 = "Some second text here"
string_3 = "some Text Here"

if string_1 != string_2:
    print("\nThe strings are not equal")

if (string_1.lower()) != (string_3.lower()):
    print("\nThe strings are not equal")
else:
    print("\nThe strings are equal")

# --------------------------------------------------------------------------- #
number_1 = 42
number_2 = 69

if number_1 <= 50 and number_2 <= 50:
    print("\nBoth the numbers <= 50")
else:
    print("\nOne is not <= 50")

if number_1 == 42 or number_2 == 42:
    print("\nThere is number: 42")
else:
    print("\nThere isn't number: 42")

# --------------------------------------------------------------------------- #
pets = ["dog", "cat", "bird", "fish", "rabbit"]

if "cat" in pets:
    print("\nThere is a cat.")
else:
    print("\nThere isn't a cat")

# --------------------------------------------------------------------------- #
print("-------------------------- * * * * * * * * * -------------------------")

if "rabbit" not in pets:
    pets.append("rabbit")

for pet in pets:
    print(f"\tThere is a {pet}")
