#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    if not boxes:
        return False

    n = len(boxes)
    keys = set([0])  # Start with the key to the first box

    while keys:
        new_keys = set()
        for key in keys:
            for box in boxes[key]:
                if box < n and box not in keys:
                    new_keys.add(box)
        if not new_keys:
            break
        keys |= new_keys

    return len(keys) == n
