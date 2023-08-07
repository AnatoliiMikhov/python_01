cities = {
    "London": {
        "country": "United Kingdom",
        "population": "8.9 million",
        "fact": "Is the most populous city in the United Kingdom",
    },
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Is the most visited city in the world",
    },
    "Tokyo": {
        "country": "Japan",
        "population": "37.4 million",
        "fact": "Is the most populous city in the world by metropolitan area",
    },
    "New York City": {
        "country": "United States",
        "population": "8.8 million",
        "fact": "Is the most populous city in the United States",
    },
    "Los Angeles": {
        "country": "United States",
        "population": "3.9 million",
        "fact": "Is the second most populous city in the United States",
    },
}

# print(cities)

for city, data in cities.items():
    print(f"\nI want to tell you about {city.title()}:")

    print(
        f"\n\tThe city is in {data['country']}"
        f"\n\tPopulation is: {data['population']}"
        f"\n\tThe fact: {data['fact']}"
    )

    # --------------------------------------------------------------------------- #
    print("\n...\n")
    # --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
