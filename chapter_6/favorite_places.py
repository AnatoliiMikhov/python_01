favorite_places = {
    "john doe": ["paris", "rome", "tokyo"],
    "jane doe": ["london", "new york city", "los angeles"],
    "mary smith": ["miami", "las vegas", "hawaii"],
    "peter jones": ["sydney", "melbourne", "canberra"],
    "sally green": ["toronto", "vancouver", "montreal"],
}

for user, places in favorite_places.items():
    print(f"\n{user.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")
