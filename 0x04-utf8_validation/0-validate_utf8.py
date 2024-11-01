#!/usr/bin/python3 
"""UTF-8 Validation"""

def validUTF8(data):
    """a method that determines if a given data set represents a valid UTF-8 encoding."""
    nbytes = 0

    for num in data:
        byte = num & 0xFF
        
        if nbytes == 0:
            if (byte >> 5) == 0b110:
                nbytes = 1
            elif (byte >> 4) == 0b1110:
                nbytes = 2
            elif (byte >> 3) == 0b11110:
                nbytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            nbytes -= 1
    return nbytes == 0