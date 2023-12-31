# a simple function - format name


def get_formatted_name(first_name="john", last_name="smith", middle_name=""):
    """Returns formatted full name"""
    if not middle_name:
        full_name = f"{first_name} {last_name}"
    else:
        full_name = full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


# --------------------------------------------------------------------------- #
my_name = get_formatted_name(
    first_name="anatolii", middle_name="wonderful", last_name="mikhov"
)
print("\n", my_name)

wife_name = get_formatted_name("liudmyla", "mikhova")
print("\n", wife_name)

default_name = get_formatted_name()
print("\n", default_name)
