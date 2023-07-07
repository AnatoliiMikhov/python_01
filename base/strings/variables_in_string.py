first_name = "anatolii"
last_name = "mikhov"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


# old syntax
full_name = "{} {}".format(first_name, last_name)
message = f"Hello, {full_name.upper()}!"
print(f"\t{message}")
