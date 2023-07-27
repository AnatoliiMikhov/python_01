def translate_to_lower(list):
    """
    This function translates a list of strings to lower register.

    Args:
      list: The list of strings to be translated.

    Returns:
      The list of strings in lower register.
    """

    translated_list = []
    for name in list:
        translated_name = name.lower()
        translated_list.append(translated_name)

    return translated_list
