#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    keys = set([0])
    n_boxes = len(boxes)

    while True:
        prev_keys = keys.copy()

        for i in range(n_boxes):
            if i in keys:
                keys.update(boxes[i])

        if keys == prev_keys:
            break

    return len(keys) == n_boxes
