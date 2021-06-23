from collections import defaultdict

def numMatchingSubsequence(s,words):
    word_dict = defaultdict(list)
    count = 0

    for word in words:
        k = word[0]                 ## keys are the starting character of the each word.
        word_dict[k].append(word)   ## based on the starting character, we append the word to the list


    for char in s:
        words_starting_char = word_dict[char]   ## the list of words which start with char           
        word_dict[char] = []

        for word in words_starting_char:    ## for each word, we will update word_dict
            if len(word) == 1:
                count+=1
            else:
                k = word[1]         ## new key, which is the next char in the word
                v = word[1]         ## new value, which is the word without char
                word_dict[k].append(word[1:])   ## update the word_dict


    return count



s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

print(numMatchingSubsequence(s,words))