favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "anatolii": "javascript",
}

# --------------------------------------------------------------------------- #
# favorite_languages = {}
# --------------------------------------------------------------------------- #
# print(favorite_languages)


# --------------------------------------------------------------------------- #
# Show Phil's favorite language
# ------------------------- get_favorite_lang starts ------------------------ #
def get_favorite_lang(name):
    if (favorite_languages and name) in favorite_languages:
        language = favorite_languages[name]
        message = f"\n{name.title()} favorite languages is {language.title()}"
        return message
    else:
        return f"\nWe aren't familiar with {name.title()}, so we do not know his favorite language"


# -------------------------- get_favorite_lang ends ------------------------- #

# ------------------------- print favorite language ------------------------- #
print(get_favorite_lang("anatolii"))
print(get_favorite_lang("phil"))
print(get_favorite_lang("rabbit"))

# --------------------------------------------------------------------------- #

# ----------------------------- Use method get() ---------------------------- #
phil_lang = favorite_languages.get("phil", "\nWe are not familiar with this user")
setur_lang = favorite_languages.get("setur", "\nWe are not familiar with this user")

print(f"\nPhil favorite lang is: {phil_lang.title()}")
print(f"\nSetur favorite lang is: {setur_lang.title()}")

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
for name, lang in favorite_languages.items():
    print(f'{name.title()}\'s favorite languages is "{lang.title()}"')

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
# ------------------------- How to stdout only keys ------------------------- #
count = 1

for name in favorite_languages.keys():
    print(f"Name_{count}: {name.title()}")
    count += 1

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #

boss_name = "stivan"

if boss_name not in favorite_languages:
    favorite_languages[boss_name] = "PHP"

# --------------------------------------------------------------------------- #

count = 1

for name in favorite_languages.keys():
    print(f"Name_{count}: {name.title()}")
    count += 1

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


for name, lang in favorite_languages.items():
    if lang == "PHP":
        print(f'{name.title()}\'s favorite languages is "{lang.upper()}"')
    else:
        print(f'{name.title()}\'s favorite languages is "{lang.title()}"')


# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# ------------------------------ show keys list ----------------------------- #
keys_list = favorite_languages.keys()
print(keys_list)

# ----------------------------- show list values ---------------------------- #
list_values = favorite_languages.values()
print(list_values)

# ------------------------------ show key:value ----------------------------- #
items = favorite_languages.items()
print(items)

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# -------------------------- sorted dictionary keys ------------------------- #
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


# ---------------------- We can get only unique values ---------------------- #
print("\nThe following languages have been mentioned:\n")

for langguage in set(favorite_languages.values()):
    print(langguage.title())


# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


print(favorite_languages)

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #


programmers = {
    "john": "python",
    "jen": "java",
    "mary": "c++",
    "peter": "javascript",
    "sarah": "ruby",
}


for name in programmers.keys():
    if name in favorite_languages:
        print(f"Hi, {name.title()}! Thank you for taking part in this survey.")
    else:
        print(f"Hi, {name.title()}! Please, take part in our survey")

# --------------------------------------------------------------------------- #
print("\n------------------------ * * * * * * * * * -----------------------\n")
# --------------------------------------------------------------------------- #
