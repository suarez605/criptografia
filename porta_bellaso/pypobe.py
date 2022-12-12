""" Python program to user Porta/Bellaso cipher.
    Alvaro Suarez Lozano 2021
    - https://github.com/suarez605
    - https://www.linkedin.com/in/aesuarezlozano/
    
    Tip: Using as a script put TEXT and KEY inside quotation marks, also be sure that the key only contain letters.

    Usage:
    pypobe.py <TEXT> <KEY>
    pypobe.py -i | --interactive
    pypobe.py -h | --help
   

"""
import sys
from docopt import docopt
from dictionaries import get_dictionaries

ALPHABET = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def porta_bellaso(key: str, dictionary: dict, text: str) -> str:
    counter_position = 0
    text = text.upper()
    key = key.upper()
    result = ""
    for character in text:
        if character == " " or character not in ALPHABET:
            result+= character
            continue
        key_dictionary = key[counter_position % len(key)]
        char_to_append = dictionary[key_dictionary].get(character)
        if char_to_append == None: # Se puede optimizar mejorando la generacion de diccionarios
            for item in dictionary[key_dictionary].items():
                if item[1] == character:
                    char_to_append = item[0]
                    break
        result += char_to_append
        counter_position += 1
    return result


def interactive():
    print("""pypobe Interactive mode | By Alvaro Suarez Lozano 2021 | Use Ctrl+C to exit.""")
    key = input("Please introduce the key to use during this session:\n")
    while True:
        text = input(f"Write the text to cipher/decipher with the key -{key}-\n")
        print(porta_bellaso(key=key, dictionary=get_dictionaries(), text=text))

if __name__ == "__main__":
    arguments = docopt(doc=__doc__)
    if arguments["-i"] or arguments["--interactive"]:
        interactive()
        
    print(porta_bellaso(key=arguments["<KEY>"], dictionary=get_dictionaries(), text=arguments["<TEXT>"]))
