"""
Date: 15-06-2021
Author: Piyush Gairola
Problem: 1718. Construct the Lexicographically Largest Valid Sequence [https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/]
"""



class Solution:
    def constructDistancedSequence(self,n):
        def dfs(idx):
            if idx == self.m:
                return all(self.ans)

            if self.ans[idx]:
                return dfs(idx+1)

            for x in range(n,0,-1):
                j = idx if x==1 else idx+x

                if j<self.m and not self.ans[j] and not self.visited[x]:
                    self.ans[idx], self.ans[j] = x, x
                    self.visited[x] = True
                    
                    if dfs(idx+1):
                        return True
                    self.ans[idx], self.ans[j] = 0,0
                    self.visited[x] = False

            return False

        self.m = 2*n-1
        self.ans = [0]*self.m
        self.visited = [False]*(n+1)

        dfs(0)

        return self.ans