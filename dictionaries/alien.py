# simple dictionary
alien_1 = {}
alien_1["color"] = "green"
alien_1["points"] = 5
alien_1["smell"] = "smelly"
alien_1["speed"] = "medium"

# --------------------------------------------------------------------------- #
print(f"alien_1 color is: {alien_1['color']}")
print(f"alien_1 points: {alien_1['points']}")

# ------------------------------- add elements ------------------------------ #
alien_1["x_position"] = 0
alien_1["y_position"] = 25

print(alien_1)

# --------------------------- how to change values -------------------------- #
print(f"The alien_1 is {alien_1['color']}")

alien_1["color"] = "yellow"

print(f"The alien_1 color is {alien_1['color']} now")
# --------------------------------------------------------------------------- #
print(f"\nOriginal position X: {alien_1['x_position']}")

# The alien moves to the right
# We calculate the magnitude of the displacement on the basis of the current speed.
# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости.


def set_speed(speed):
    if speed == "slow":
        x_increment = 1
    elif speed == "medium":
        x_increment = 2
    elif speed == "fast":
        x_increment = 3
    else:
        x_increment = 0

    return x_increment


# --------------------------------------------------------------------------- #
# The new position is equal to the sum of the old position and increment
# Новая позиция равна сумме старой позиции и приращения
x_increment = set_speed("medium")

alien_1["x_position"] = alien_1["x_position"] + x_increment

print(f"\nNew X position: {alien_1['x_position']}\n")

# --------------------------------------------------------------------------- #
# how to delete an entry?
# just use: del
del alien_1["smell"]
print(alien_1)

# --------------------------------------------------------------------------- #
