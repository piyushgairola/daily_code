"""
Date: 21-06-2021
Author: Piyush Gairola
Problem: 118. Pascal's Triangle [https://leetcode.com/problems/pascals-triangle/]
"""

def generate(numRows):
    res = []

    for i in range(numRows):
        temp_ans = []
        for j in range(i+1):
            if j==0 or j==i:
                temp_ans.append(1)

            else:
                a = res[i-1][j-1]
                b = res[i-1][j]
                temp_ans.append(a+b)

        res.append(temp_ans)

    return res