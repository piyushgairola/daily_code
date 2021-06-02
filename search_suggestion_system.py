"""
Date: 02-06-2021
Author: Piyush Gairola
Problem: 1268. Search Suggestions System [https://leetcode.com/problems/search-suggestions-system]
"""

def suggestedProducts(products,searchWord):
    products.sort()
    n = len(products)
    prefix = ""
    ans = []
    for c in searchWord:
        temp = []
        prefix += c
        prod_idx = binarySearch(products, prefix)

        ans.append([products[i] for i in range(prod_idx, min(n,prod_idx+3)) if products[i].startswith(prefix)])

    return ans

def binarySearch(products,prefix):
    low = 0
    high = len(products)

    while low<high:
        mid = (low+high)//2
        if products[mid]<prefix:
            low = mid+1
        else:
            high = mid

    return low

