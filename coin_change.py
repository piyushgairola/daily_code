"""
Date: 22-7-2021
Problem: 322. Coin Change [https://leetcode.com/problems/coin-change/]
"""

def coinChange(coins,target):
    dp = [0]+[float('inf')]*(target)
    
    for t in range(1,target+1):
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], dp[t-coin]+1)  


    return dp[target] if dp[target]<float('inf') else -1



coins = [2,3,5,8]
amount = 10
print(coinChange(coins,amount))