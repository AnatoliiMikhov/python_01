# Using int () to get a numeric input
# int() - interprets the string as a numeric value
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("You can drink wine.")
else:
    print("You can not drink wine.")
