sparky = {
    "kind": "dog",
    "age": 5,
    "favorite_food": "kibble",
    "eyes_color": "brown",
    "owner": "john doe",
    "name": "sparky",
}

smudge = {
    "kind": "cat",
    "age": 3,
    "favorite_food": "tuna",
    "eyes_color": "green",
    "owner": "jane doe",
    "name": "smudge",
}

jerry = {
    "kind": "mouse",
    "age": 1,
    "favorite_food": "cheese",
    "eyes_color": "black",
    "owner": "mary smith",
    "name": "jerry",
}

shelly = {
    "kind": "turtle",
    "age": 10,
    "favorite_food": "lettuce",
    "eyes_color": "black",
    "owner": "peter jones",
    "name": "shelly",
}

# --------------------------------------------------------------------------- #

pets = [sparky, smudge, jerry, shelly]

for pet in pets:
    name = pet.get("name")
    kind = pet.get("kind")
    age = pet.get("age")
    favorite_food = pet.get("favorite_food")
    eyes_color = pet.get("eyes_color")
    owner = pet.get("owner")

    print()

    print(
        f"Hello, I am {name.title()}"
        f"\n\tI am a {kind}"
        f"\n\tI'm {age} old"
        f"\n\tI really like {favorite_food}"
        f"\n\tI have {eyes_color} eyes"
        f"\n\tMy owner's name is {owner.title()}"
    )
