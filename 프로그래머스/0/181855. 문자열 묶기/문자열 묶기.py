def solution(strArr):
    arr = list(map(lambda x:len(x),strArr))
    dp=[0]*(len(strArr)+1)
    for i in arr:
        dp[i]+=1
    answer = max(dp)
    return answer