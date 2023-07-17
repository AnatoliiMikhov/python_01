# amusement_park.py
# check age

# age = 66
age = 42

price_before_4 = "free"
price_between_4_18 = 25
price_after_18 = 40
price_after_65 = price_after_18 / 2

if age < 4:
    price = price_before_4 = "free"
elif age < 18:
    price = price_between_4_18
elif age < 65:
    price = price_after_18
elif age >= 65:
    price = price_after_65

print(f"\nYour ticket costs ${price}")
