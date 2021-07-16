"""
Date: 16-07-2021
Problem: 791. Custom Sort String [https://leetcode.com/problems/custom-sort-string/]
"""

def customSortString(order,s):
    char_map = {}
    res = []
    for i in s:
        if i not in char_map:
            char_map[i] = 1
        else:
            char_map[i] += 1

    for c in order:
        if c in char_map:
            res.append(c*char_map.pop(c))

    for c in char_map:
        res.append(c*char_map[c])

    return "".join(res)