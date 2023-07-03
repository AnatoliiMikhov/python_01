# list sorting
cars = ["bmw", "audi", "toyota", "subaru"]

# Change the list
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# --------------------------------------------------------------------------- #
cars = ["bmw", "audi", "toyota", "subaru"]
sorted_cars_list = sorted(cars)
sorted_cars_list_reversed = sorted(cars, reverse=True)

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted_cars_list)

print()
print(sorted_cars_list_reversed)

print("\nHere is the original list again:")
print(cars)
