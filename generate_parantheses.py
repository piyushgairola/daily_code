"""
Date: 16-06-2021
Author: Piyush Gairola
Problem: 22. Generate Parentheses [https://leetcode.com/problems/generate-parentheses/]
"""

def generateParantheses(n):
    def generate(s,l,r):
        if len(s) == 2*n:
            ans.append("".join(s))
            return
        
        if l<n:
            s.append("(")
            generate(s,l+1,r)
            s.pop()

        if r<l:
            s.append(")")
            generate(s,l,r+1)
            s.pop()


    ans = []
    generate([],0,0)
    return ans
