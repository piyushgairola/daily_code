"""
Date: 08/07/2021
Problem: 718. Maximum Length of Repeated Subarray [https://leetcode.com/problems/maximum-length-of-repeated-subarray/]
"""

def findLength(num1,num2):
    n1,n2 = len(num1), len(num2)

    dp = [[0]*(n1+1) for _ in range(n2+1)]
    ans = 0
    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if num1[j-1] == num2[i-1]:
                dp[i][j] = dp[i-1][j-1] +1

            ans = max(ans,dp[i][j])


    return ans