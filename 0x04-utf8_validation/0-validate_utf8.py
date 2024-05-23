#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
    data (list): A list of integers representing bytes of data.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_bytes = 0

    mask_1 = 1 << 7  # 10000000
    mask_2 = 1 << 6  # 01000000

    for byte in data:
        # Get the most significant byte
        mask_byte = 1 << 7

        if number_bytes == 0:
            # Count how many 1s at the beginning of the byte
            while mask_byte & byte:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            # For UTF-8 encoding, bytes count should be between 2 and 4
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # If this byte is not a valid continuation byte, return False
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        # We processed one byte, decrease the byte count
        number_bytes -= 1

    # If we finish processing and have bytes left, it means invalid UTF-8
    return number_bytes == 0


# Test cases
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False

    data4 = [197, 130, 1]
    print(validUTF8(data4))  # True

    data5 = [235, 140, 4]
    print(validUTF8(data5))  # False
