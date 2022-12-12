import sys


class Dictionary():

    def __init__(self, key) -> None:
        self.key = key
        self.dictionary = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def init_dict(self):
        final_dict = {}.fromkeys(self.dictionary)
        for key in final_dict.keys():
            position = (self.dictionary.index(key) + self.key) % len(self.dictionary)
            final_dict[key] = self.dictionary[position]
        return final_dict


if __name__ == "__main__":
    key = int(sys.argv[1])
    clear_text = sys.argv[2].upper()
    if len(sys.argv) == 4:
        mode = sys.argv[3]
    else:
        mode = None
    dic = Dictionary(key).init_dict()
    cipher = ''
    for character in clear_text:
        if mode == '-v':
            print(f"Clear char : {character}    Cypher char: {dic.get(character) if character != ' ' else ' '}")
        if character == ' ':
            cipher += ' '
            continue
        cipher += dic.get(character)
    print(cipher)
