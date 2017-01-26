def alphabet_position(letter):
    letter = letter.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if letter in alphabet:
        letter_value = alphabet.index(letter)

    return letter_value

def rotate_character(char, rot):

    l_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    u_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if not char.isalpha():
        return char
    char_value = alphabet_position(char)
    rot_char_value = (char_value + rot)%26

    if char in l_alphabet:
        rot_char = l_alphabet[rot_char_value]

    if char in u_alphabet:
        rot_char = u_alphabet[rot_char_value]

    return rot_char

def encrypt(text, rot):
    encrypted_text = ''

    for char in range(len(text)):
        encrypted_text += rotate_character(text[char], rot)

    return encrypted_text
