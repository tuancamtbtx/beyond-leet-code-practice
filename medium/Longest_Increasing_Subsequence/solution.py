def findLIS(s):
    n=len(s)
    #dp[i] stores the length of the longest increasing subsequence ending at element i
    dp=[1 for i in range(n)]
    
    for i in range(1,n):
        for j in range(i):
            #If current element i is greater than element j, update dp[i]
            if(s[i] > s[j]):
                dp[i] = max(dp[i],dp[j]+1)
    ret = 1
    for i in range(n):
        ret = max(ret,dp[i])
    return ret