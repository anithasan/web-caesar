import collections
import string

def alphabet_position(letter):
    letter = letter.lower()
    con_letter = list(string.ascii_lowercase).index(letter)
    return con_letter


def rotate_character(char, rot):
    lower_case = collections.deque(string.ascii_lowercase)
    upper_case = collections.deque(string.ascii_uppercase)


    if char.isalpha() == False:
        return char
    elif char in lower_case:
        rot_index = alphabet_position(char) + int(rot)
        if rot_index < 26:
            return lower_case[rot_index]
        else:
            return lower_case[rot_index % 26]

    elif char in upper_case:
        rot_index = alphabet_position(char) + rot
        if rot_index < 26:
            return upper_case[rot_index]
        else:
            return upper_case[rot_index % 26]

def encrypt(text, rot):

    rot = int(rot)
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)

    return encrypted
