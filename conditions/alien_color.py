alien_color = "green"

# -------------------------------- Function --------------------------------- #


def alien_points(alien_color):
    """
    This function determines the number of points a player earns for shooting an alien.

    Args:
      alien_color: The color of the alien.

    Returns:
      The number of points the player earns.
    """

    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        points = 0

    return print(f"\nThe player has just earned {points} points.")


# --------------------------------------------------------------------------- #
alien_points("yellow")
alien_points("green")
alien_points("blue")
alien_points("red")
