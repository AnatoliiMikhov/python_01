# how to change, how to add, how to delete
# european_cars = [
#     "bugatti",
#     "citroen",
#     "peugeot",
#     "renault",
#     "volkswagen",
#     "porsche",
#     "mercedes",
#     "aston martin",
#     "mclaren",
#     "jaguar",
#     "rolls royce",
#     "bentley",
#     "alpha romeo",
#     "ferrari",
# ]

european_cars = ["bugatti", "citroen", "peugeot", "jaguar", "renault", "volkswagen"]
print(european_cars)

european_cars[0] = "audi"
print(european_cars)


# --------------------------------------------------------------------------- #
#                                  how to add                                 #
# --------------------------------------------------------------------------- #

european_cars.append("alpha romeo")
print(european_cars)


# --------------------------------------------------------------------------- #
#                      how to insert an element to a list                     #
# --------------------------------------------------------------------------- #

european_cars.insert(0, "bentley")
print(european_cars)

# --------------------------------------------------------------------------- #
#                                how to delete                                #
# --------------------------------------------------------------------------- #
del european_cars[0]
print(european_cars)

# --------------------------------------------------------------------------- #
#                               del last element                              #
# --------------------------------------------------------------------------- #

del european_cars[-1]
print(european_cars)

# --------------------------------------------------------------------------- #
#                          deleting use method pop()                          #
# --------------------------------------------------------------------------- #
european_cars.append("ford")

last_bought_car = european_cars.pop()


print(european_cars)

print(last_bought_car)
print(f"The last car I bought is {last_bought_car.title()}")

first_bought_car = european_cars.pop(0)
print(f"First car that I bought was {first_bought_car.title()}")

# --------------------------------------------------------------------------- #
#                          Removing elements by value                         #
# --------------------------------------------------------------------------- #
too_expensive = "jaguar"
european_cars.remove(too_expensive)

print(european_cars)

print(f"\nA {too_expensive.title()} is too expensive for me.")
