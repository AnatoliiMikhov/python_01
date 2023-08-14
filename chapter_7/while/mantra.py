# mantra.py
import time


# --------------------------------------------------------------------------- #
#                                Ganesha mantra                               #
# --------------------------------------------------------------------------- #
def ganesh_mantra_create():
    counter = 1
    # mantra = "Om Gan Ganapataye Namah Sharanam Ganesha"
    mantra = "ॐ गं गणपतये नमः शरणं गणेश"

    while counter <= 108:
        # print(f"\n{mantra}")
        mantra += " | ॐ गं गणपतये नमः शरणं गणेश"
        counter += 1
    return mantra


ganesh_mantra = ganesh_mantra_create()

print(ganesh_mantra)

time.sleep(5)


# --------------------------------------------------------------------------- #
#                                 Guru mantra                                 #
# --------------------------------------------------------------------------- #
def guru_mantra():
    # --------------------------------------------------------------------------- #
    print("\n...\n")
    # --------------------------------------------------------------------------- #

    counter = 1
    # mantra = "Oṃ Āh Hūṃ Vajra Guru Padma Siddhi Hūṃ Oṃ Āh Hūṃ "
    mantra = "ॐ अह हुं वज्र गुरु पद्म सिद्धि हुं"

    while counter <= 108:
        # mantra += " Oṃ Āh Hūṃ Vajra Guru Padma Siddhi Hūṃ Oṃ Āh Hūṃ "
        mantra += " | ॐ अह हुं वज्र गुरु पद्म सिद्धि हुं"
        counter += 1

    # --------------------------------------------------------------------------- #
    return mantra


# --------------------------------------------------------------------------- #
guru_mantra = guru_mantra()
counter = 1

while counter < 1_001:
    print(f"\n{guru_mantra}")
    counter += 1
# --------------------------------------------------------------------------- #

# ---------------------------- Guru mantra finish --------------------------- #
