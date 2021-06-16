"""
Date: 16-06-2021
Author: Piyush Gairola
Problem: 1723. Find Minimum Time to Finish All Jobs [https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/]
"""

class Solution:
    def minimumTimeRequired(self,jobs,k):
        n_jobs = len(jobs)
        jobs.sort(reverse=True)
        worker = [0]*k
        self.ans = sum(jobs)

        def dfs(idx):
            if idx == n_jobs:
                self.ans = min(self.ans, max(worker))
                return
            
            for w_idx in range(k):
                if worker[w_idx] + jobs[idx] < self.ans:
                    worker[w_idx] += jobs[idx]
                    dfs(idx+1)
                    worker[w_idx] -= jobs[idx]

                if worker[w_idx] == 0:
                    break

            return False

        dfs(0)
        return self.ans