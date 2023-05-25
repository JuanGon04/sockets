substitution_table = {
        'a': 'x',
        'b': 'y',
        'c': 'z',
        'd': 'm',
        'e': 'n',
        'f': 'o',
        'g': 'p',
        'h': 'q',
        'i': 'r',
        'j': 's',
        'k': 't',
        'l': 'u',
        'm': 'v',
        'n': 'w',
        'o': 'a',
        'p': 'b',
        'q': 'c',
        'r': 'd',
        's': 'e',
        't': 'f',
        'u': 'g',
        'v': 'h',
        'w': 'i',
        'x': 'j',
        'y': 'k',
        'z': 'l',
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
        'D': 'M',
        'E': 'N',
        'F': 'O',
        'G': 'P',
        'H': 'Q',
        'I': 'R',
        'J': 'S',
        'K': 'T',
        'L': 'U',
        'M': 'V',
        'N': 'W',
        'O': 'A',
        'P': 'B',
        'Q': 'C',
        'R': 'D',
        'S': 'E',
        'T': 'F',
        'U': 'G',
        'V': 'H',
        'W': 'I',
        'X': 'J',
        'Y': 'K',
        'Z': 'L'
    }


def encrypt_substitution(message):
    encrypted_message = ""

    for char in message:
        encrypted_message += substitution_table.get(char, char)

    return encrypted_message

def decrypt_substitution(encrypted_message):
    decryption_table = {value: key for key, value in substitution_table.items()}
    decrypted_message = ""

    for char in encrypted_message:
        decrypted_message += decryption_table.get(char, char)

    return decrypted_message



