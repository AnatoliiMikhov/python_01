rivers = [
    "amazon",
    "nile",
    "yangtze",
    "mississippi",
    "yukon",
    "murray",
    "ganges",
    "rhine",
    "seine",
    "thames",
]

print(rivers)
print(len(rivers))

print()

print(sorted(rivers))
print()

print(sorted(rivers, reverse=True))

last_river = rivers[-1]
print()

print(f"Last river is {last_river.title()}")
print()

poped_river = rivers.pop()
print(f"\nThere are poped river. It is the {poped_river.title()}\n")

print(rivers)
print(len(rivers))

rivers.append("dnipro")

print()
print(rivers)
print(len(rivers))

print()


print(rivers[-1].title())
