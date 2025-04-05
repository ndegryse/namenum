def name_to_lower(usr_name):
    lower_name = usr_name.lower()
    print("Made it to name_to_lower function")
    return lower_name

def characters_to_numbers(usr_name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    number_name = []
    characters = list(usr_name)
    for character in characters:
        number = alphabet.index(character) + 1
        number_name.append(number)
    return number_name