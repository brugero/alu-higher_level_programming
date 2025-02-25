#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from ASCII value
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)
