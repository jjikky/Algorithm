def solution(array):
    dp=[0]*1001
    for i in array:
        dp[i]+=1
    max_v=max(dp)
    answer = dp.index(max_v)
    dp[answer]=0
    if max_v==max(dp):
        return -1
    return answer