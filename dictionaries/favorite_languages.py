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
