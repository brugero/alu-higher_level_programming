#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        result += uppercase_char
    print("{}".format(result))
