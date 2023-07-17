def check_age(age):
    """
    Эта функция определяет возраст человека.

    Аргументы:
      age: Возраст человека в годах.

    Возврат:
      Возраст человека в виде строки.
    """

    if age < 2:
        return "baby"
    elif age >= 2 and age < 4:
        return "baby"
    elif age >= 4 and age < 13:
        return "child"
    elif age >= 13 and age < 20:
        return "teenager"
    elif age >= 20 and age < 65:
        return "adult"
    else:
        return "elderly Human"


# --------------------------------------------------------------------------- #
message = ""
answer = check_age(49)
message = f"\nYou are {answer}"

print(message)
