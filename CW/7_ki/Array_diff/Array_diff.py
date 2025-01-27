# task Array.diff
# Level 6 kyu
# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
# CW Algorithms


def array_diff(a, b):
    result = []
    b_set = set(b)

    for x in a:
        if x not in b_set:
            result.append(x)

    return result
