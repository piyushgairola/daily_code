"""
Date: 28/06/2021
Problem: 1047. Remove All Adjacent Duplicates In String [https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/]
"""

def removeDuplicates(s):
    temp = "#"
    for i in s:
        if i == temp[-1]:
            temp = temp[:-1]
        else:
            temp += i

    return temp[1:]