"""
Date: 05-06-2021
Author: Piyush Gairola
Problem: 1383. Maximum Performance of a Team [https://leetcode.com/problems/maximum-performance-of-a-team/]
"""

import heapq

def maxPerformance(n,speed,efficiency,k):
    heap = []
    speed_sum = 0
    ans = -1

    for e,s in sorted(zip(efficiency,speed), reverse=True):
        if len(heap)<k:
            heapq.heappush(heap,s)
            speed_sum += s
        else:
            least_speed = heap.heappushpop(heap,s)      ##  sliding window approach
            speed_sum += (s-least_speed)
        
        ans = max(ans, e*speed_sum)

    return ans%(10**9 + 7)