def longestSubsequence(arr):
    n = len(arr)
    dp = [1]*n
    pos = [-1]*n

    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i] and dp[i]<dp[j]+1:
                dp[i] = dp[j] + 1
                pos[i] = j


    ans,idx = dp[0],0
    for i in range(1,n):
        if ans<dp[i]:
            ans = dp[i]
            idx = i


    seq = []
    while(idx != -1):
        seq.insert(0,arr[idx])
        idx = pos[idx]


    return seq

arr = [0,1,0,3,2,3]
print(longestSubsequence(arr))