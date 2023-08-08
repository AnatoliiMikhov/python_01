# counting.py
current_number = 1
mantra = "Om Gan Ganapate Namaha Sharanam Ganesha"

while current_number <= 108:
    print(f"\n{current_number}: {mantra}")
    current_number += 1


# --------------------------------------------------------------------------- #
print("\n...\n")
# --------------------------------------------------------------------------- #

counter = 1
mantra = "Oṃ Āh Hūṃ Vajra Guru Padma Siddhi Hūṃ Oṃ Āh Hūṃ "

while counter <= 100:
    mantra += " Oṃ Āh Hūṃ Vajra Guru Padma Siddhi Hūṃ Oṃ Āh Hūṃ "
    counter += 1

print(mantra)

# --------------------------------------------------------------------------- #
counter = 1

while counter < 10_001:
    print(f"\n{counter}: {mantra.title()}")
    counter += 1
# --------------------------------------------------------------------------- #
