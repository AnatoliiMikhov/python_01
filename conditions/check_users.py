import sys

sys.path.append("library")
import to_lowercase

# --------------------------------------------------------------------------- #


# from to_lowercase import translate_to_lower

# --------------------------------------------------------------------------- #

current_users = [
    "AdmiN",
    "Alice",
    "bob",
    "carol",
    "dave",
    "ethan",
    "frank",
    "george",
    "harry",
    "ian",
]

new_users = [
    "jessica",
    "michael",
    "sarah",
    "aliCe",
    "john",
    "mary",
    "aDMin",
    "patricia",
    "robert",
    "steven",
]

# ------------------------ current user to lowercase ------------------------ #

current_users_lowercase = to_lowercase.translate_to_lower(current_users)

# print(current_users_lowercase)


# Hi, you must choose a new name
# Hi, this nickname is available
# --------------------------------------------------------------------------- #

for user in new_users:
    if user.lower() in current_users_lowercase:
        print(
            f"\nHello, {user.title()}! This name already exists.\n\tYou must choose a different name"
        )
    else:
        print(f"\nHi, {user.title()}! You have chosen a unique name")
