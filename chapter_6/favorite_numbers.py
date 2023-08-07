favorite_numbers = {
    "bard": [1, 2, 3],
    "ada": [4, 5, 6],
    "grace": [7, 8, 9],
    "alan": [10, 11, 12],
    "charles": [13, 14, 15],
    "david": [16, 17, 18],
}


# print(favorite_numbers)

for user, numbers in favorite_numbers.items():
    print(f"\n{user.title()}'s favorite numbers are:")

    for number in numbers:
        print("\t", number)
