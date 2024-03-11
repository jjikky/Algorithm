def solution(strArr):
    dp=[0]*(len(strArr)+1)
    for i in strArr:
        dp[len(i)]+=1
    return max(dp)