# Start with two lists: users for verification
# and an empty list for storing trusted users.

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []


# --------------------------------------------------------------------------- #
print("\n...\n")
# --------------------------------------------------------------------------- #

print(unconfirmed_users)


# --------------------------------------------------------------------------- #
print("\n...\n")
# --------------------------------------------------------------------------- #


while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")

    confirmed_users.append(current_user)


# --------------------------------------------------------------------------- #
print("\n...\n")
# --------------------------------------------------------------------------- #

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
