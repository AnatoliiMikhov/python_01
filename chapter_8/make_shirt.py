def make_shirt(size="l", text="I love Python"):
    print(
        f'\nThis shirt\'s size is "{size.title()}"'
        f'\nAnd it has a print "{text.title()}"'
    )


make_shirt()
make_shirt(size="s", text="I love javascript")
