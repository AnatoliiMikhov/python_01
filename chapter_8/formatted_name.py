# a simple function - format name


def get_formatted_name(first_name, last_name):
    """Returns formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# --------------------------------------------------------------------------- #
my_name = get_formatted_name(first_name="anatolii", last_name="mikhov")
print("\n", my_name)
