"""
Date: 13-07-2021
Problem: 205. Isomorphic Strings [https://leetcode.com/problems/isomorphic-strings/]
"""

def isIsomorphic(s,t):
    char_map = {}

    for i in range(len(s)):
        if s[i] not in char_map.keys() and t[i] not in char_map.values():
            char_map[s[i]] = t[i]

        elif s[i] not in char_map.keys() and t[i] in char_map.values():
            return False

        elif char_map[s[i]] != t[i]:
            return False


    return True