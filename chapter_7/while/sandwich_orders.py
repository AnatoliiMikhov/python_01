# sandwich_orders.py

sandwiches = [
    "pastrami",
    "ham and cheese",
    "club",
    "pastrami",
    "BLT",
    "grilled cheese",
    "Monte Cristo",
    "pastrami",
]

finished_sandwiches = []

# --------------------------------------------------------------------------- #
print("\n--- Sorry, but we don't have pastrami right now. ---\n")

# --------------------------------------------------------------------------- #
while "pastrami" in sandwiches:
    sandwiches.remove("pastrami")

# --------------------------------------------------------------------------- #
while sandwiches:
    current_sandwich = sandwiches.pop()
    print(f'I made your "{current_sandwich}" sandwich')
    finished_sandwiches.append(current_sandwich)

# --------------------------------------------------------------------------- #
print("\nThere are your sandwiches:")

# --------------------------------------------------------------------------- #
for sandwich in finished_sandwiches:
    print("\t", sandwich)
