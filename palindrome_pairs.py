"""
Date: 13-06-2021
Author: Piyush Gairola
Problem: 336. Palindrome Pairs [https://leetcode.com/problems/palindrome-pairs/]
"""



def palindromePairs(words):
    word_dict = {word[::-1]:i for i,word in enumerate(words)}
    ans = []

    for i,word in enumerate(words):
        for j in range(len(word)+1):
            prefix = word[:j]
            postfix = word[j:]

            if prefix in word_dict and word_dict[prefix] != i and postfix == postfix[::-1]:
                ans.append([i,word_dict[prefix]])

            if j>0 and postfix in word_dict and word_dict[postfix] != i and prefix == prefix[::-1]:
                ans.append([word_dict[postfix], i])


    return ans