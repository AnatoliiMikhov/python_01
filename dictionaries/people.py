people = [
    {
        "firstname": "John",
        "lastname": "Doe",
        "age": 35,
        "address": "123 Main St",
        "hair_color": "brown",
    },
    {
        "firstname": "Jane",
        "lastname": "Doe",
        "age": 32,
        "address": "456 Park Ave",
        "hair_color": "black",
    },
    {
        "firstname": "Bob",
        "lastname": "Smith",
        "age": 41,
        "address": "789 Oak St",
        "hair_color": "blonde",
    },
    {
        "firstname": "Mary",
        "lastname": "Jones",
        "age": 29,
        "address": "321 Elm St",
        "hair_color": "red",
    },
    {
        "firstname": "David",
        "lastname": "Lee",
        "age": 27,
        "address": "987 Pine St",
        "hair_color": "brown",
    },
]

# --------------------------------------------------------------------------- #
for person in people:
    print(
        f"\nHello, I am {person['firstname'].title()} {person['lastname'].title()}."
        f"\n\tI am {person['age']} old."
        f"\n\tI live on {person['address']}."
        f"\n\tMy hair color is {person['hair_color']}."
    )
# --------------------------------------------------------------------------- #
