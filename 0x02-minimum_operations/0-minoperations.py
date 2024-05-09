#!/usr/bin/python3

"""
This script calculates the minimum number
of operations required to achieve
exactly n characters of 'H' in a text file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    required to achieve exactly n
    characters of 'H' in a text file.

    :param n: The desired number of 'H' characters.
    :type n: int
    :return: The minimum number of operations required.
    :rtype: int
    """
    if n <= 0:
        return 0

    operations = 0
    file_length = 1
    clipboard = 0

    while file_length < n:
        if n % file_length == 0:
            clipboard = file_length
        file_length += clipboard
        operations += 1

    return operations


if __name__ == "__main__":
    # Test cases
    n = 4
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
